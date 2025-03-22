"""
Tests for Exercise 3: Custom Module Development
"""
import pytest
from exercises.exercise3 import *

def test_reverse_string():
    """Test string reversal"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("123") == "321"

def test_count_vowels():
    """Test vowel counting"""
    assert count_vowels("hello") == 2
    assert count_vowels("HELLO") == 2
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0

def test_capitalize_words():
    """Test word capitalization"""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("") == ""
    assert capitalize_words("a b c") == "A B C"

def test_remove_duplicates():
    """Test duplicate removal"""
    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("bookkeeper") == "bokepr"
    assert remove_duplicates("") == ""
    assert remove_duplicates("aaa") == "a"

def test_is_palindrome():
    """Test palindrome checking"""
    assert _is_palindrome("radar") is True
    assert _is_palindrome("hello") is False
    assert _is_palindrome("") is True
    assert _is_palindrome("a") is True

def test_count_substring():
    """Test substring counting"""
    assert _count_substring("hello hello", "hello") == 2
    assert _count_substring("aaa", "aa") == 2
    assert _count_substring("", "a") == 0
    assert _count_substring("hello", "") == 0

def test_main_function(capsys):
    """Test the main function's output"""
    main()
    captured = capsys.readouterr()
    assert "Reversed string:" in captured.out
    assert "Vowel count:" in captured.out
    assert "Capitalized words:" in captured.out
    assert "Without duplicates:" in captured.out 