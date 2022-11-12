import json
import os
import re
import unittest
import os.path
from collections.abc import Mapping
from typing import Optional

from pywhat import regex_identifier
from pywhat.filter import Distribution, Filter
from pywhat.helper import (AvailableTags, CaseInsensitiveSet, InvalidTag,load_regexes)
from rich.console import Console
from rich.table import Table

class TestClass(unittest.TestCase):
    
    def test_get_tags(self):
        # dist = AvailableTags()
        # self.assertEqual(tag,dist.get_tags)
        tag = AvailableTags()
        result = tag.get_tags(self)
        self.assertEqual(result, self.tag)

    def test_issubset(self):
        caseset = CaseInsensitiveSet()
        result = caseset.issubset()
        self.assertTrue(result)

    def test_get_filter(self):
        filt = Filter()
        result = filt.get_filter(self) 
        self.assertEqual(result)

    def test_pretty_print(self):
        prnt = Printing()
        result = prnt.pretty_print (self)
        self.assertEqual(result)

    def test_check(self):
        ident = RegexIdentifier()
        result = ident.check(self)
        self.assertEqual(result)

    def test_clean_text(self):
        ident = RegexIdentifier
        result = ident.clean_text(self)
        self.assertEqual(result)
    

if __name__ == '__main__':
    unittest.main()
