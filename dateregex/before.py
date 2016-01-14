#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, timedelta, MINYEAR

def _year_regex_before(year):
    if int(year) <= MINYEAR: 
        return None
    year_regex = r'('
    year_regex += r'\d{1,%s}' % str(len(year) - 1) if len(year) > 1 else ''
    for idx, digit in enumerate(year):
        if digit != '0':
            regex = '|' + year[0:idx]
            regex += '0' if digit == '1' else '[0-%s]' % str(int(digit) - 1)
            if idx < len(year) - 1:
                regex += '\d{%s}' % (len(year) - (idx + 1)) 
            year_regex += regex

    year_regex += ')'
    return '-'.join((year_regex, r'\d{2}', r'\d{2}'))
    
def _month_regex_before(year, month):
    return None

def _day_regex_before(year, month, day):
    return None

def regex_date_before(given_date):
    year, month, day = given_date.isoformat().split('-')

    year_regex = _year_regex_before(year)
    month_regex = _month_regex_before(year, month)
    day_regex = _day_regex_before(year, month, day)

    date_regex = '(' + year_regex
    date_regex += ('|' + month_regex) if month_regex else ''
    date_regex += ('|' + day_regex) if day_regex else ''
    date_regex += ')'
    return date_regex
