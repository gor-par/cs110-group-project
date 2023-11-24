import csv
from csv_reader import CsvReader
from utils import get_input, ValidationState, InvalidFilenameError
import argparse


parser = argparse.ArgumentParser(
    description='Dsiplays a table with metadata and example rows'
)

parser.add_argument('source', help='Path to the unclean csv file')
parser.add_argument(
    'destination', help='Output path to the sanitized csv file')


column_means = {}
dataset_none_indices = {}


def cli():
    args = parser.parse_args()
    validation_state = validate_input(args)
    if not validation_state.ok:
        print(validation_state.message)
        return

    dataset = CsvReader(args.source)

    for column in dataset.fieldnames:
        column_means[column] = 0
        dataset_none_indices[column] = []

    (no_duplicates, duplicate_count) = drop_duplicates(dataset.rows)
    (no_nones, none_count) = handle_nulls(no_duplicates)
    write_csv(no_nones, args.destination, dataset.fieldnames)
    print(f'{duplicate_count} duplicates are dropped, {
        none_count} empty values are replaced with the mean')


def validate_input(args):
    '''
    Handles the improper arguments
    '''

    state = ValidationState()

    try:
        CsvReader.verify_path(args.source)
    except InvalidFilenameError as error:
        state.error(error.message + ", Source")

    if args.destination[-3:].lower() != 'csv':
        state.error('File is not CSV, Destination')

    return state


def drop_duplicates(rows):
    unique_rows_set = set()
    unique_rows = []

    for row in rows:
        row_tuple = tuple(row.values())

        if row_tuple not in unique_rows_set:
            unique_rows.append(row)
            unique_rows_set.add(row_tuple)

    duplicate_count = len(rows) - len(unique_rows)

    return (unique_rows, duplicate_count)


def handle_nulls(rows):
    find_nones(rows)
    count_column_means(rows)

    for row in rows:
        for column, value in row.items():
            if value is None:
                row[column] = column_means[column]

    none_count = sum(len(indices) for indices in dataset_none_indices.values())

    return (rows, none_count)


def find_nones(rows):
    for index, row in enumerate(rows):
        for column, value in row.items():
            if value is None:
                dataset_none_indices[column].append(index)


def count_column_means(rows):

    # makes sets from index lists to boost performance
    for column in dataset_none_indices:
        dataset_none_indices[column] = set(dataset_none_indices[column])

    # stores in the dict the sums of all those values,
    # which indexes are not in the None lists
    for index, row in enumerate(rows):
        for column in row:
            if type(row[column]) is str:
                continue
            if index not in dataset_none_indices[column]:
                column_means[column] += row[column]

    # calculates the means, using the number of all not None values
    for column, sum in column_means.items():
        column_means[column] = sum / \
            (len(rows) - len(dataset_none_indices[column]))


def write_csv(rows, path, fieldnames):
    with open(path, "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames)
        writer.writeheader()
        writer.writerows(rows)


cli()
