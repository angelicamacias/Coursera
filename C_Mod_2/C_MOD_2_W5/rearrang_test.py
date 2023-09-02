#!/usr/bin/env python 

from rearrang import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
#assertEqual= to verify that what we expected is exactly what we got both of the arguments are equal 

    # in the case of the empty sring 
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase = "Billy"
        expected = "Billy"
        self.assertEqual(rearrange_name(testcase), expected)
unittest.main()