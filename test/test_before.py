#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dateregex.before import _year_regex_before, _month_regex_before, _day_regex_before
import re
import unittest


class TestBeforeRegex(unittest.TestCase):

    """Tests regexes for dates before a given date"""

    def test_year_regex_for_XX1_cent(self):
        year_regex = _year_regex_before('2019')
        year_regex = '^' + year_regex + '$'

        self.assertRegexpMatches('2018-12-31', year_regex)
        self.assertRegexpMatches('2011-01-25', year_regex)
        self.assertRegexpMatches('1066-01-01', year_regex)
        self.assertRegexpMatches('476-12-25', year_regex)
        self.assertRegexpMatches('33-12-25', year_regex)

        self.assertNotRegexpMatches('2019-01-01', year_regex)
        self.assertNotRegexpMatches('3019-01-01', year_regex)
        self.assertNotRegexpMatches('2119-01-01', year_regex)
        self.assertNotRegexpMatches('2029-01-01', year_regex)
        self.assertNotRegexpMatches('2030-01-01', year_regex)
        self.assertNotRegexpMatches('12019-01-01', year_regex)

    def test_year_regex_for_3_digit_year(self):
        year_regex = _year_regex_before('100')
        year_regex = '^' + year_regex + '$'

        for i in range (1,100):
            self.assertRegexpMatches(str(i) + '-02-29', year_regex)

        for i in range (100,200):
            self.assertNotRegexpMatches(str(i) + '-02-29', year_regex)


    def test_min_year_regex(self):
        year_regex = _year_regex_before('1')
        self.assertIsNone(year_regex)


    def test_min_month_regex(self):
        month_regex = _month_regex_before('2016', '01')
        self.assertIsNone(month_regex)

    def test_extensive_month_regex(self):
        for test_month in range(2,13):
            month_regex = _month_regex_before('2016', '%.2d' % test_month)
            month_regex = '^' + month_regex + '$'


            for month in range(1, test_month):
                self.assertRegexpMatches('2016-%.2d-31' % month, month_regex)

            for month in range(test_month, 13):
                self.assertNotRegexpMatches('2016-%.2d-01' % month, month_regex)

    def test_feb_month_regex(self):
        month_regex = _month_regex_before('2016', '02')
        month_regex = '^' + month_regex + '$'

        self.assertRegexpMatches('2016-01-01', month_regex)
        self.assertRegexpMatches('2016-01-31', month_regex)

        for month in range(2, 13):
            self.assertNotRegexpMatches('2016-%.2d-31' % month, month_regex)

    def test_tenth_month_regex(self):
        month_regex = _month_regex_before('2016', '10')
        month_regex = '^' + month_regex + '$'

        for month in range(2, 10):
            self.assertRegexpMatches('2016-%.2d-31' % month, month_regex)

        self.assertNotRegexpMatches('2016-10-01', month_regex)
        self.assertNotRegexpMatches('2016-11-01', month_regex)
        self.assertNotRegexpMatches('2016-12-01', month_regex)


    def test_last_month_regex(self):
        month_regex = _month_regex_before('2016', '12')
        month_regex = '^' + month_regex + '$'

        for month in range(2, 12):
            self.assertRegexpMatches('2016-%.2d-31' % month, month_regex)

        self.assertNotRegexpMatches('2016-12-01', month_regex)

    def test_first_day_regex(self):
        day_regex = _day_regex_before('2016', '12', '01')
        self.assertIsNone(day_regex)

    def test_31_day_regex(self):
        for i in range(2, 32):
            day_regex = _day_regex_before('2016', '01', '%.2d' % i)
            day_regex = '^' + day_regex + '$'
            for j in range(1,i):
                self.assertRegexpMatches('2016-01-%.2d' % j, day_regex)
            for j in range(i, 32):
                self.assertNotRegexpMatches('2016-01-%.2d' % j, day_regex)

    def test_feb_day_regex(self):
        for i in range(2, 29):
            day_regex = _day_regex_before('2016', '02', '%.2d' % i)
            day_regex = '^' + day_regex + '$'
            for j in range(1,i):
                self.assertRegexpMatches('2016-02-%.2d' % j, day_regex)
            for j in range(i, 29):
                self.assertNotRegexpMatches('2016-02-%.2d' % j, day_regex)

    def test_30_day_regex(self):
        for i in range(2, 31):
            day_regex = _day_regex_before('2046', '04', '%.2d' % i)
            day_regex = '^' + day_regex + '$'
            for j in range(1,i):
                self.assertRegexpMatches('2046-04-%.2d' % j, day_regex)
            for j in range(i, 31):
                self.assertNotRegexpMatches('2046-04-%.2d' % j, day_regex)
