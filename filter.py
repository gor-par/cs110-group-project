from csv_reader import CsvReader


from typing import Literal, Optional
from filter_functions import functions, function_support_per_type as function_support


class FilterOption:
    def __init__(self,
                 filter_type: Literal['string', 'number', 'date'],
                 function: str,
                 column: str,
                 target,
                 format: Optional[str]
                 ):

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

    filtered_rows = []

    for row in raw_rows:
        if does_pass(row, options):
            filtered_rows.append(row)

    return filtered_rows


def does_pass(row, options):
    for option in options:

        if option.type == "date":
            if not option.function(row[option.column], option.target, option.format):
                return False
        else:
            if not option.function(row[option.column], option.target):
                return False

    return True
