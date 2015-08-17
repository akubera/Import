#
# test.py
#
"""
Tests for the Import package
"""

import Import
import sys

help(Import)

# def test_good_import():
#     Import . test

def test_import_lambda():
    Import . lambdas
    print(">>", sys.modules)
    lambdas.x('foo')
