# -*- coding: utf-8 -*-
# Copyright (c) 2018, Libermatic and Contributors
# See license.txt

from __future__ import unicode_literals
import unittest
from mss_customization.utils.transform \
    import make_period, get_bound_dates, month_diff, update
from datetime import date


class TestTransform(unittest.TestCase):
    def test_make_period(self):
        self.assertEqual(make_period('2017-12-12'), '2017-12-12 - 2018-01-11')

    def test_make_period_with_dateobj(self):
        self.assertEqual(
            make_period(date(year=2017, month=12, day=12)),
            '2017-12-12 - 2018-01-11'
        )

    def test_get_bound_dates(self):
        self.assertEqual(
            get_bound_dates('2017-12-12 - 2018-01-11'),
            {'start_date': '2017-12-12', 'end_date': '2018-01-11'},
        )

    def test_get_bound_dates_as_date(self):
        self.assertEqual(
            get_bound_dates('2017-12-12 - 2018-01-11', as_date=True),
            {
                'start_date': date(year=2017, month=12, day=12),
                'end_date': date(year=2018, month=1, day=11),
            },
        )

    def test_month_diff(self):
        self.assertEqual(month_diff('2017-12-12', '2017-10-10'), 2)

    def test_month_diff_within_a_month(self):
        self.assertEqual(month_diff('2017-12-12', '2017-11-15'), 0)

    def test_month_diff_negative(self):
        self.assertEqual(month_diff('2017-12-12', '2018-02-15'), -2)

    def test_update(self):
        input = {'name': 'Nemo'}
        output = update('ship', 'Nautilus')(input)
        self.assertEqual(input, {'name': 'Nemo'})
        self.assertEqual(output, {'name': 'Nemo', 'ship': 'Nautilus'})
