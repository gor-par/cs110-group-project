from datetime import datetime


def month_range(start, end):
    if start < end:
        return range(start, end + 1)
    else:
        return [*range(start, 13), *range(1, end + 1)]


def is_equal(value, target, format=None):
    if format is None:
        if type(target) is list:
            return value in target

        return value == target

    value_date = datetime.strptime(value, format).date(),
    target_date = datetime.strptime(target, format).date(),
    return value_date == target_date


def is_larger(value, target):
    return value > target


def is_smaller(value, target):
    return value < target


def is_before(value, target, format):
    value_date = datetime.strptime(value, format).date(),
    target_date = datetime.strptime(target, format).date(),
    print(value_date, target_date, value_date < target_date)
    return value_date < target_date


def is_after(value, target, format):
    value_date = datetime.strptime(value, format).date(),
    target_date = datetime.strptime(target, format).date(),
    return value_date > target_date


def is_during(value, range, format):
    value_month = datetime.strptime(value, format).month
    return value_month in month_range(*range)


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
