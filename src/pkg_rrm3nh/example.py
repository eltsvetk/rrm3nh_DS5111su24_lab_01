"""This module provides functions for cleaning, parsing, counting words in the text."""

import re

def clean_text(a_text):
    """This function converts punctuation to white space and letters to lowercase in a_text."""
    print("Checking that input to clean_text() is string...")
    assert isinstance(a_text,str)
    print("passed")
    lower_case_a_text = a_text.lower()
    ## Remove anything that is not a lowercase letter, number, or white space character
    lower_case_a_text = re.sub(r"[^a-z0-9\s]"," ",lower_case_a_text)
    return lower_case_a_text


def tokenize(a_text):
    """This function splits a_text (type str) on white space, returns list of words."""
    print("Checking that input to tokenize() is string...")
    assert isinstance(a_text,str)
    print("passed")
    a_text_tokenized = re.split(r"\s+",a_text.strip())
    return a_text_tokenized

def count_words(a_text):
    """This function returns a dict with counts of all words found in a_text (type str)."""
    print("Checking that input to counts_words() is string...")
    assert isinstance(a_text,str)
    print("passed")
    tokenized_a_text = tokenize(a_text)
    word_count_dict = {}
    for word in tokenized_a_text:
        if word not in word_count_dict:
            word_count_dict[word] = 0
        word_count_dict[word] += 1
    return word_count_dict
