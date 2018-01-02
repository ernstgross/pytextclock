#!/usr/bin/env python

import unittest
from pytextclock import get_text_time

class TestPytextclock(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_text_time(self):
        self.assertEqual(get_text_time(00, 00), "null")
        self.assertEqual(get_text_time(00, 00), "null")
        self.assertEqual(get_text_time(11, 55), "fünf vor zwölf")
        self.assertEqual(get_text_time(11, 59), "fünf vor zwölf")
        self.assertEqual(get_text_time(12,  0), "zwölf")
        self.assertEqual(get_text_time(12,  4), "zwölf")
        self.assertEqual(get_text_time(12,  5), "fünf nach zwölf")

if __name__ == '__main__':
    unittest.main()
