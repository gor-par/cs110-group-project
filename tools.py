import csv
import statistics


def get_column_mean(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    mean = statistics.mean(values)

    return mean


def get_column_median(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    median = statistics.median(values)

    return median


def get_column_mode(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    mode = statistics.mode(values)

    return mode


def get_column_stdev(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    stdev = statistics.stdev(values)

    return stdev


def get_column_min(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    min_value = min(values)

    return min_value


def get_column_max(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    max_value = max(values)

    return max_value


def get_column_range(column, rows):
    values = [float(row[column]) for row in rows if row[column] is not None]

    min_value = min(values)
    max_value = max(values)
    range_value = max_value - min_value

    return range_value
