from datetime import datetime


def month_range(start, end):
    """
    Generate a range of months between start and end (inclusive).

    Args:
        start (int): Start month.
        end (int): End month.

    Returns:
        range: A range of months.
    """
    return range(start, end + 1) if start < end else [*range(start, 13), *range(1, end + 1)]


def is_equal(value, target, format=None):
    """
    Check if a value is equal to the target.

    Args:
    value: The value to compare.
    target: The target value or a list of target values.
    format (str): Optional datetime format for date comparison.

    Returns:
    bool: True if equal, False otherwise.
    """
    if format is None:
        return value in target if type(target) is list else value == target

    value_date, target_date = datetime.strptime(value, format).date(), datetime.strptime(target, format).date()
    return value_date == target_date


def is_larger(value, target):
    """
    Check if a value is larger than the target.

    Args:
    value: The value to compare.
    target: The target value.

    Returns:
    bool: True if larger, False otherwise.
    """
    return value > target


def is_smaller(value, target):
    """
    Check if a value is smaller than the target.

    Args:
    value: The value to compare.
    target: The target value.

    Returns:
    bool: True if smaller, False otherwise.
    """
    return value < target


def is_before(value, target, format):
    """
    Check if a date value is before the target date.

    Args:
        value (str): The date value to compare.
        target (str): The target date.
        format (str): Datetime format for date comparison.

    Returns:
    bool: True if before, False otherwise.
    """
    value_date, target_date = datetime.strptime(value, format).date(), datetime.strptime(target, format).date()
    return value_date < target_date


def is_after(value, target, format):
    """
    Check if a date value is after the target date.

    Args:
    value (str): The date value to compare.
    target (str): The target date.
    format (str): Datetime format for date comparison.

    Returns:
    bool: True if after, False otherwise.
    """
    value_date, target_date = datetime.strptime(value, format).date(), datetime.strptime(target, format).date()
    return value_date > target_date


def is_during(value, date_range, format):
    """
    Check if a date value is within the specified range.

    Args:
    value (str): The date value to compare.
    date_range (tuple): Start and end months of the range.
    format (str): Datetime format for date comparison.

    Returns:
    bool: True if during the range, False otherwise.
    """

    value_month = datetime.strptime(value, format).month
    return value_month in month_range(*date_range)



function_support_per_type = {
    'string': ['equal'],
    'number': ['equal', 'larger', 'smaller'],
    'date': ['equal', 'after', 'during', 'before'],
}

functions = {
    'equal': is_equal,
    'after': is_after,
    'before': is_before,
    'during': is_during,
    'larger': is_larger,
    'smaller': is_smaller
}
