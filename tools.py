import statistics


def get_values(rows, column):

    return [float(row[column]) for row in rows]


def get_column_mean(rows, column):
    values = get_values(rows, column)

    mean = statistics.mean(values)

    return mean


def get_column_median(rows, column):
    values = get_values(rows, column)

    median = statistics.median(values)

    return median


def get_column_mode(rows, column):
    values = get_values(rows, column)

    mode = statistics.mode(values)

    return mode


def get_column_stdev(rows, column):
    values = get_values(rows, column)

    stdev = statistics.stdev(values)

    return stdev


def get_column_min(rows, column):
    values = get_values(rows, column)

    min_value = min(values)

    return min_value


def get_column_max(rows, column):
    values = get_values(rows, column)

    max_value = max(values)

    return max_value


def get_column_range(rows, column):
    values = get_values(rows, column)

    min_value = min(values)
    max_value = max(values)
    range_value = max_value - min_value

    return range_value
