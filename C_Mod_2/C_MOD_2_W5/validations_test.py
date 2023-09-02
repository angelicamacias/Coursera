#!/usr/bin/env python

import unittest
from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)
    
    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)
    
    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)
    
    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)
                    #first: pass the error that we expect the function to raise
                    #then the function name followed by any parameters that need to be passed that function

unittest.main()
