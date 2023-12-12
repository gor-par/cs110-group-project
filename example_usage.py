from csv_reader import CsvReader
from filter import FilterOption, filter
from tools import get_column_mean, get_values


# Read as I want only the data from Norway and Sweden, for days when
# the minimal temperature was below -10, precipitation was above 3,
# for winter months starting from 2017
# filter_options = [
#     FilterOption("string", "equal", "country", ["Norway", "Sweden"], None),
#     FilterOption("number", "larger", "precipitation", 2, None),
#     FilterOption("number", "smaller", "tmin", -5, None),
#     FilterOption("date", "after", "date", '1/1/2017', '%m/%d/%Y'),
#     FilterOption("date", "during", "date", (12, 2), '%m/%d/%Y'),
# ]


# test = CsvReader('nordics_weather.csv')

# print(len(filter(test.rows, filter_options)))
# print(filter(test.rows, filter_options))

armenia_filter = [
    # FilterOption('string', 'equal', 'country', [
    #              'Azerbaijan', 'Armenia', 'Georgia']),
    # FilterOption('date', 'before', 'last_updated',
    #              '2023-11-01 00:00', '%Y-%m-%d %H:%M'),
    FilterOption('date', 'during', 'last_updated', (10, 10), '%Y-%m-%d %H:%M'),
    FilterOption('string', 'equal', 'country', 'Armenia'),
]

rwanda_filter = [
    FilterOption('date', 'during', 'last_updated', (10, 10), '%Y-%m-%d %H:%M'),
    FilterOption('string', 'equal', 'country', 'Rwanda'),
]

dataset = CsvReader('GlobalWeatherRepository.csv')

armenia_october = filter(dataset.rows, armenia_filter)
rwanda_october = filter(dataset.rows, rwanda_filter)

armenia_october_mean = get_column_mean(armenia_october, 'temperature_celsius')
rwanda_october_mean = get_column_mean(rwanda_october, 'temperature_celsius')

# print(get_values('temperature_celsius', armenia_october))


print(armenia_october_mean, rwanda_october_mean)
