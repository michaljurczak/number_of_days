import pytest
from calendar import IllegalMonthError

from src.number_of_days import get_no_of_days_basic, get_no_of_days_extended, InvalidDateFormat

@pytest.mark.parametrize(
    'date, expected_number_of_days, throw_ex, ex_type', [
        ('2020-02', 29, False, None),
        ('9999-02', 28, False, None),
        ('0000-02', 29, False, None),
        (None, None, True, TypeError),
        (22, None, True, TypeError),
        ('2020.2-02', None, True, InvalidDateFormat),
        ('2020.2-11.5', None, True, InvalidDateFormat),
        ('0000/02', None, True, InvalidDateFormat),
        ('0000\\02', None, True, InvalidDateFormat),
        ('0000 02', None, True, InvalidDateFormat),
        ('0000 -02', None, True, InvalidDateFormat),
        ('0000--02', None, True, InvalidDateFormat),
        ('0-5', None, True, InvalidDateFormat),
        ('-1500-5', None, True, InvalidDateFormat),
        ('999999999-5', None, True, InvalidDateFormat),
        ('-999999999-5', None, True, InvalidDateFormat),
        ('2aa0-2', None, True, InvalidDateFormat),
        ('2aa0/2', None, True, InvalidDateFormat),
        ('2aa0\\2', None, True, InvalidDateFormat),
        ('2aa0x2', None, True, InvalidDateFormat),
        ('2aa0.2', None, True, InvalidDateFormat),
        ('2aa.2', None, True, InvalidDateFormat),
        ('2020-222', None, True, InvalidDateFormat),
        ('-2020-222', None, True, InvalidDateFormat),
        ('aaaa-asdds', None, True, InvalidDateFormat),
        ('-', None, True, InvalidDateFormat),
        ('-5', None, True, InvalidDateFormat),
        ('2020-', None, True, InvalidDateFormat),
        ('2020-a', None, True, InvalidDateFormat),
        ('', None, True, InvalidDateFormat),
        ('2020-00', None, True, IllegalMonthError),
        ('2020-25', None, True, IllegalMonthError),
    ]
)
def test_number_of_days_basic(date, expected_number_of_days, throw_ex, ex_type):
    if throw_ex:
        with pytest.raises(ex_type):
            get_no_of_days_basic(date)
    else:
        assert get_no_of_days_basic(date) == expected_number_of_days

@pytest.mark.parametrize(
    'date, expected_number_of_days, throw_ex, ex_type', [
        ('2020-2', 29, False, None),
        ('0-5', 31, False, None),
        ('9999-5', 31, False, None),
        ('999999999-5', 31, False, None),
        ('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999-5', 31, False, None),
        ('-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999-5', 31, False, None),
        (None, None, True, TypeError),
        (22.5, None, True, TypeError),
        ('2020.2-11.5', None, True, InvalidDateFormat),
        ('2020-11.5', None, True, InvalidDateFormat),
        ('2020--2', None, True, InvalidDateFormat),
        ('2020 - 2', None, True, InvalidDateFormat),
        ('2aa0-2', None, True, InvalidDateFormat),
        ('2aa0/2', None, True, InvalidDateFormat),
        ('2aa0\\2', None, True, InvalidDateFormat),
        ('2aa0x2', None, True, InvalidDateFormat),
        ('2aa0.2', None, True, InvalidDateFormat),
        ('2020-222', None, True, InvalidDateFormat),
        ('-2020-222', None, True, InvalidDateFormat),
        ('aaaa-asdds', None, True, InvalidDateFormat),
        ('-', None, True, InvalidDateFormat),
        ('-5', None, True, InvalidDateFormat),
        ('2020-', None, True, InvalidDateFormat),
        ('2020-a', None, True, InvalidDateFormat),
        ('', None, True, InvalidDateFormat),
        ('2020-0', None, True, IllegalMonthError),
        ('2020-25', None, True, IllegalMonthError),
    ]
)
def test_number_of_days_extended(date, expected_number_of_days, throw_ex, ex_type):
    if throw_ex:
        with pytest.raises(ex_type):
            get_no_of_days_extended(date)
    else:
        assert get_no_of_days_extended(date) == expected_number_of_days