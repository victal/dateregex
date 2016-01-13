#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, timedelta
import re


def __year_regex_after(year):
    year_regex = r'(\d+\d{%s}|' % len(year)
    for idx, digit in enumerate(year):
        if digit != '9':
            regex = year[0:idx]
            regex += '9' if digit == '8' else '[%s-9]' % str(int(digit) + 1)
            if idx < len(year) - 1:
                regex += '\d{%s}|' % (len(year) - (idx + 1)) 
            else: 
                regex += ')'

            year_regex += regex
    return '-'.join((year_regex, r'\d{2}', r'\d{2}'))


def __month_regex_after(year, month):
    if month == '12':
        return None

    digit1, digit2 = (x for x in month)
    if digit1 == '1':
        month_regex = r'12' if month == '11' else r'1[12]'
    else:
        month_regex = r'1[0-2]'
        if digit2 != '9':
            if digit2 == '8':
                month_regex = r'(' + month_regex + r'|09)'
            else:
                month_regex = r'(' + month_regex + r'|0[%s-9])' 
                month_regex = month_regex % str(int(digit2) + 1)
    return '-'.join((year, month_regex, r'\d{2}'))

def __day_regex_after(year, month, day):
    last_month_day = str((date(int(year), int(month) + 1, 1) - date.resolution).day)
    if day == last_month_day:
        return None
    day_regex = r'('
    digit1, digit2 = (d for d in day)
    last_digit1, last_digit2 = (d for d in last_month_day)
    if digit1 == last_digit1:
        day_regex = last_month_day if int(digit2) == int(last_digit2) - 1 else last_digit1 + r'[%s-%s]' % (str(int(digit2) + 1), last_digit2)
    else:
        day_regex = r'('
        day_regex += last_digit1 if int(digit1) == int(last_digit1) - 1 else r'[%s-%s]' % (str(int(digit1) + 1), last_digit1)
        day_regex +=r'\d'
        if digit2 < '9':
            day_regex += '|' + digit1
            day_regex += '9' if digit2 == '8' else r'[%s-9]' % str(int(digit1) + 1)

        day_regex += ')'
    return '-'.join((year, month, day_regex))


def regex_date_after(given_date):
    year, month, day = given_date.isoformat().split('-')

    year_regex = __year_regex_after(year)
    month_regex = __month_regex_after(year, month)
    day_regex = __day_regex_after(year, month, day)

    return  r'(' + '|'.join((year_regex, month_regex, day_regex)) + ')'



def __main():
    date_regex = regex_date_after(date.today())
    print(date_regex)
    pattern = re.compile(date_regex)


    d = date.today() + date.resolution
    assert pattern.match(date.strftime(d, '%Y-%m-%d')) is not None
    print(date.strftime(d, '%Y-%m-%d') + ' is okay')
    d += date.resolution

if __name__ == '__main__':
    __main()
