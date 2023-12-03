from csv_reader import CsvReader
from filter import FilterOption, filter


# Read as I want only the data from Norway and Sweden, for days when
# the minimal temperature was below -10, precipitation was above 3,
# for winter months starting from 2017
filter_options = [
    FilterOption("string", "equal", "country", ["Norway", "Sweden"], None),
    FilterOption("number", "larger", "precipitation", 2, None),
    FilterOption("number", "smaller", "tmin", -5, None),
    FilterOption("date", "after", "date", '1/1/2017', '%m/%d/%Y'),
    FilterOption("date", "during", "date", (12, 2), '%m/%d/%Y'),
]


test = CsvReader('nordics_weather.csv')

print(len(filter(test.rows, filter_options)))
# print(filter(test.rows, filter_options))
