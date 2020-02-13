import re

from calendar import monthrange


class InvalidDateFormat(Exception):
    pass


def get_no_of_days_basic(date):
    """
    Function that returns number of days in given month and year
    @param date: only supports 'yyyy-mm' date format
    @return: number of days in given month
    @raise InvalidDateFormat: rasises exception when date format is differen than 'yyyy-mm'
    @raise calendar.IllegalMonthError when number of given month is greater than 12 or less than 0
    """
    formatted_date = re.search(r'^(\d{4})-(\d{2})$', date)
    
    if not formatted_date:
        raise InvalidDateFormat('Entered invalid date format!')

    year = int(formatted_date.group(1))
    month = int(formatted_date.group(2))

    # monthrange returns [weekday of first day of the month, number of days in month]
    return monthrange(year, month)[1]


def get_no_of_days_extended(date):
    """
    Function that returns number of days in given month and year
    @param date: supports date format:
        'years-months', where:
            - years and be 1 in length or more
            - negative years are interpreted as BC years
            - months can be 1 or 2 long
    @return: number of days in given month
    @raise InvalidDateFormat: rasises exception when date format is differen than 'yyyy-mm'
    @raise calendar.IllegalMonthError when number of given month is greater than 12 or less than 0
    """
    formatted_date = re.search(r'^-?(\d+)-(\d{1,2})$', date)
    
    if not formatted_date:
        raise InvalidDateFormat('Entered invalid date format!')

    year = int(formatted_date.group(1))
    month = int(formatted_date.group(2))

    # monthrange returns [weekday of first day of the month, number of days in month]
    return monthrange(year, month)[1]

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('leap')
            else:
                print('not leap')
        else:
            print('leap year')
    else:
        print('not leap year')