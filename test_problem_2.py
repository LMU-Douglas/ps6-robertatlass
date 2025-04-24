import pytest
from intuitive_abbreviations import *
# -------------------------------
# Tests for Problem 2: Intuitive Abbreviations
# -------------------------------

def test_intuitive_yes():
    assert is_intuitive("Oxygen", "Ogn") == "YES"

def test_intuitive_no():
    assert is_intuitive("Oxygen", "Od") == "NO"

def test_order():
    assert is_intuitive("Carbon", "bC") == "YES"

def test_letters_not_in_name():
    assert is_intuitive("Helium", "Hz") == "NO"

def test_duplicate_letters():
    assert is_intuitive("Sodium", "Sooo") == "YES"