#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dateregex.before import _year_regex_before
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

