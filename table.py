from csv_reader import CsvReader
from utils import get_input, ValidationState, InvalidFilenameError
import argparse

parser = argparse.ArgumentParser(
    description='Dsiplays a table with metadata and example rows'
)

parser.add_argument('path', help='Path to the csv file')
parser.add_argument('-cl', '--column-length', default="10", type=int,
                    help='Table column length, from 6 to 18, default 10')


def cli():
    args = parser.parse_args()
    validation_state = validate_input(args)
    if not validation_state.ok:
        print(validation_state.message)
        return

    # All the invalid file errors were handled above
    dataset = CsvReader(args.path)

    draw_table(dataset, args.column_length)


def validate_input(args):
    '''
    Handles the improper arguments
    '''

    state = ValidationState()

    if args.column_length > 18:
        args.column_length = 18

    if args.column_length < 6:
        args.column_length = 6

    try:
        CsvReader.verify_path(args.path)
    except InvalidFilenameError as error:
        state.error(error.message)

    return state


def draw_table(dataset, column_length=10):
    '''
    creates and prints a table representation of the given dataset

    Args:
    dataset (CsvReader): source csv data
    column_length (int): length of the columns, default = 10

    '''

    # Variable that tells to shorten the table if it has more than 10 columns
    is_table_long = False
    field_count = dataset.column_count

    if dataset.column_count > 10:
        field_count = 11
        is_table_long = True

    table_length = field_count * (column_length + 1) + 1

    row_break = "\n" + ("-" * table_length) + "\n" + "|"
    table = row_break

    table = add_metadata(table, dataset, table_length)

    table += row_break

    table = add_table_headings(
        table, dataset.fieldnames, column_length, is_table_long)

    table += row_break

    table = populate_table(
        table, dataset.rows[:5], column_length, row_break, is_table_long)

    for i in range(field_count):
        table += format_to_length_n('...', column_length) + "|"
    table += row_break

    table = populate_table(
        table, dataset.rows[-5:], column_length, row_break, is_table_long)

    print(table[:-1])


def add_metadata(table, dataset, table_length):
    '''
    Adds the first line with the name, row and column count

    Args:
    table (str): the ascii table to manipualte
    dataset (CsvReader): metadata holder
    table_length: length of the table, including the edges

    '''
    metadata_row = f'{dataset.filename}:' \
                   f' {dataset.length} Rows, {dataset.column_count} Columns'
    table += format_to_length_n(metadata_row, table_length - 2) + "|"

    return table


def add_table_headings(table, fieldnames, column_length, is_table_long):
    '''
    Adds headings to the table

    Args:
    table (str): the ascii table to manipualte
    fieldnames (list<str>): the fieldnames to add...
    columng_length (int): length of one column
    is_table_long (bool): if true, will only print the first and last five field names

    Returs:
    str: the edited table
    '''
    names = shorten_list(fieldnames) if is_table_long else fieldnames

    for name in names:
        name = format_to_length_n(name.capitalize(), column_length)
        table += name + '|'

    return table


def populate_table(table, rows, column_length, row_break, is_table_long):
    '''
    Adds new rows to the table

    Args:
    table (str): the ascii table to manipualte
    rows (list): the dataset entries to add to the table
    columng_length (int): length of one column
    row_break (str): string of the row break
    is_table_long (bool): if true, will only print the first and last five elements of each row

    Returs:
    str: the edited table
    '''
    for row in rows:
        values = shorten_list(row) if is_table_long else row.values()

        for value in values:
            table += format_to_length_n(str(value), column_length) + "|"
        table += row_break

    return table


def format_to_length_n(string, length):
    '''
    Returns a formatted string of the given length, using spaces and dots

    Args:
    string (str): value to format
    length (int): final length

    Returns:
    str: the formatted string 

    '''

    if len(string) < length:
        return string + " " * (length - len(string))
    elif len(string) > length:
        return string[:(length - 3)] + '...'
    else:
        return string


def shorten_list(array):
    '''
    Returns the first and last five array elements, with an "..." element in between

    Args:
    array (iterable)
    '''
    if type(array) is not list:
        array = list(array.values())
    return [*array[:5], "...", *array[-5:]]


cli()
