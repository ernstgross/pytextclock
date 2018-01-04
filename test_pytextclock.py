#!/usr/bin/env python

import unittest
import pytextclock
from pytextclock import get_text_time

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
        
if __name__ == '__main__':
    unittest.main()
