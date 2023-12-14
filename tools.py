import statistics


def get_values(rows, column):
    """
    Extracts and returns a list of numeric values from a specific column in a list of dictionaries.

    Parameters:
    - rows (list of dict): A list containing dictionaries representing rows of data.
    - column (str): The column key from which numeric values will be extracted.

    Returns:
    - list of float: A list containing the numeric values from the specified column.

    """

    # # remove

    # arr = []
    # for row in rows:
    #     if (row[column] is None):
    #         continue
    #     arr.append(float(row[column]))

    # return arr

    # # stop

    return [float(row[column]) for row in rows]


def get_column_mean(rows, column):
    """
    Calculate the mean of a specified column.

    """
    values = get_values(rows, column)

    mean = statistics.mean(values)

    return mean


def get_column_median(rows, column):
    """
    Calculate the median of a specified column.
    """
    values = get_values(rows, column)

    median = statistics.median(values)

    return median


def get_column_mode(rows, column):
    """
    Find the mode of a specified column.

    """
    values = get_values(rows, column)

    mode = statistics.mode(values)

    return mode


def get_column_stdev(rows, column):
    """
    Calculate the standard deviation of a specified column.

    """
    values = get_values(rows, column)

    stdev = statistics.stdev(values)

    return stdev


def get_column_min(rows, column):
    """
    Find the minimum value of a specified column.

    """
    values = get_values(rows, column)

    min_value = min(values)

    return min_value


def get_column_max(rows, column):
    """
    Find the maximum value of a specified column.

    """
    values = get_values(rows, column)

    max_value = max(values)

    return max_value


def get_column_range(rows, column):
    """
    Calculate the range of a specified column.

    """
    values = get_values(rows, column)

    min_value = min(values)
    max_value = max(values)
    range_value = max_value - min_value

    return range_value
