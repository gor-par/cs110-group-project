from typing import Literal, Optional
from filter_functions import functions, \
    function_support_per_type as function_support


class FilterOption:
    '''
    a class for building data filtration queries

    Args:
    filter_type ("string" | "number" | "date"): data type of the column to
    filter with appropriate functions
    function (str): name of the function to use for filtration
    column (str): name of the column in the table
    target (any): the target for comparison
    [format (str)]: format of the date string, only for date types
    '''

    def __init__(self,
                 filter_type: Literal['string', 'number', 'date'],
                 function: str,
                 column: str,
                 target,
                 format: Optional[str] = None
                 ):
    '''
    Initialize a filter for a specific column based on type, function, and target.
    '''                

        self.type = filter_type

        if self.type == "date":
            if format is None:
                raise ValueError("Date type requires a format")
            else:
                self.format = format

        if function in function_support[self.type]:
            self.function = functions[function]
        else:
            raise ValueError(
                f' "{function}" comparison does not support {self.type} type'
            )

        if function == "during" and type(target) is not tuple:
            raise ValueError(
                "During comparison requires a tuple with two months"
            )

        self.column = column
        self.target = target


def filter(raw_rows: list, options: list[FilterOption]):
    '''
    filters the rows with the provided filter queries

    Args:
    raw_rows (list): list of objects to filter
    options (list[FilterOption]): FilterOption instance queries

    Returns a sublist of the original list
    '''
    filtered_rows = []

    for row in raw_rows:
        if does_pass(row, options):
            filtered_rows.append(row)

    return filtered_rows


def does_pass(row, options):
    '''
    helper function, returns True if row suffices all the filters,
    fires False with the first match
    '''
    for option in options:

        if option.type == "date":
            if not option.function(row[option.column],
                                   option.target,
                                   option.format):
                return False
        else:
            if not option.function(row[option.column], option.target):
                return False

    return True
