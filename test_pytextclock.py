#!/usr/bin/env python
"""
This module implement the unit tests for the pytextclock module.
"""

__version__    = '0.1.1'
__author__     = 'Ernst Gross'
__email__      = "ernst@grossmusik.de"
__copyright__  = "Copyright 2018, The pyclocktext project"
__credits__    = ["Joachim Gross","Johannes Gross"]
__license__    = "MIT"
__status__     = "Development"

import unittest
import pytextclock
from pytextclock import get_text_time, get_leds_from_text, is_minute_separator_in, get_minute_separator, split_minutes_text_to_search

class TestPytextclock(unittest.TestCase):

    def setUp(self):
        pytextclock.init()
        pass

    def test_get_text_time(self):
        self.assertEqual(get_text_time( 0,  0), "null")
        self.assertEqual(get_text_time( 0,  4), "null")
        self.assertEqual(get_text_time( 0,  5), "fünf nach null")
        self.assertEqual(get_text_time(11, 55), "fünf vor zwölf")
        self.assertEqual(get_text_time(11, 59), "fünf vor zwölf")
        self.assertEqual(get_text_time(12,  0), "zwölf")
        self.assertEqual(get_text_time(12,  4), "zwölf")
        self.assertEqual(get_text_time(12,  5), "fünf nach zwölf")
        self.assertEqual(get_text_time(14, 30), "halb drei")
        self.assertEqual(get_text_time(14, 25), "fünfundzwanzig nach zwei")
        self.assertEqual(get_text_time(15, 10), "zehn nach drei")
        self.assertEqual(get_text_time(15, 19), "fünfzehn nach drei")
        self.assertEqual(get_text_time(15, 20), "zwanzig nach drei")
        self.assertEqual(get_text_time(17, 25), "fünfundzwanzig nach fünf")
        self.assertEqual(get_text_time(23, 59), "fünf vor zwölf")
        self.assertEqual(get_text_time(24, 00), "null")
        self.assertEqual(get_text_time(25, 00), "eins")
        self.assertEqual(get_text_time(25, 60), "eins")
        self.assertEqual(get_text_time(26, 70), "zehn nach zwei")
        self.assertEqual(get_text_time(26, 71), "zehn nach zwei")

    def test_is_minute_separator_in(self):
        self.assertFalse(is_minute_separator_in("fünf"))
        self.assertTrue (is_minute_separator_in("fünf vor fünf"))
        self.assertTrue (is_minute_separator_in("fünf nach fünf"))
        self.assertFalse(is_minute_separator_in("zwei bla sieben"))

    def test_get_minute_separator(self):
        self.assertEqual(get_minute_separator("zehn nach zwei"), "nach")
        self.assertEqual(get_minute_separator("zehn vor zwei"), "vor")

    def test_split_minutes_text_to_search(self):
        self.assertEqual(split_minutes_text_to_search("fünf"), ["fünf"])
        self.assertEqual(split_minutes_text_to_search("zehn"), ["zehn"])
        self.assertTrue("fünf" in split_minutes_text_to_search("fünfzehn"))
        self.assertTrue("zehn" in split_minutes_text_to_search("fünfzehn"))
        self.assertTrue("fünf"     in split_minutes_text_to_search("fünfundzwanzig"))
        self.assertTrue("und"      in split_minutes_text_to_search("fünfundzwanzig"))
        self.assertTrue("zwanzig"  in split_minutes_text_to_search("fünfundzwanzig"))

    def test_get_leds_from_text(self):
        self.assertEqual(get_leds_from_text("fünf" ), [11])
        self.assertEqual(get_leds_from_text("zwölf"), [18])
        self.assertEqual(get_leds_from_text("null" ), [19])
        self.assertEqual(get_leds_from_text("fünf nach fünf"), [0,6,11])
        self.assertEqual(get_leds_from_text("zehn nach zehn"), [1,6,16])
        self.assertEqual(get_leds_from_text("zwanzig vor zwölf"), [3,4,18])
        self.assertTrue( 0 in get_leds_from_text("fünfzehn nach null"))
        self.assertTrue( 1 in get_leds_from_text("fünfzehn nach null"))
        self.assertTrue( 6 in get_leds_from_text("fünfzehn nach null"))
        self.assertTrue(19 in get_leds_from_text("fünfzehn nach null"))


if __name__ == '__main__':
    unittest.main()
