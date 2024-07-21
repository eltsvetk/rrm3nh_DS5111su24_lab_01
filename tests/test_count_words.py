import pytest
import re
import os,sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from week_3_lab import *



@pytest.fixture
def read_raven():
    f = open("pg17192.txt", "r")
    all_text = f.read()
    f.close()
    return(all_text)

def read_all_books():
    book_list = ["pg17192.txt","pg932.txt","pg1063.txt","pg10031.txt"]
    all_text = ""
    for book in book_list:
        f = open(book, "r")
        book_text = f.read()
        f.close()
        all_text = "\n".join([all_text,book_text])
    return(all_text)


def read_book(book_file):
    f = open(book_file,"r")
    all_text = f.read()
    f.close()
    return(all_text)


def test_count_words_raven_1_line_is_dict():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary with the counts of each unique word (not case sensitive)    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_count = count_words(text)
    assert isinstance(test_count, dict), f"count_words failed to return dict on sample text: {text}"
    
def test_count_words_raven_1_line_is_dict_unique_words():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary with the length representing the number of unique words (case sensitive, will treat punctuation after word as part of word)
    # Note will need to clean text to truly get unique words
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_count = count_words(text)
    assert len(test_count) == 23, f"count_words failed to identify unique words in sample text: {text}"

def test_count_words_raven_1_line_is_dict_count_that():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary that counts unique words that ignores case
    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_count = count_words(text)
    assert test_count["that"] == 1, f"count_words failed to correct count \'that\' in sample text: {text}"
    
@pytest.mark.xfail
def test_count_words_raven_1_line_with_count_punctuation():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary that counts words and punctuation for ending sentences or separating parts of a sentence (".",",",etc.) -- not currently implemented
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_count = count_words(text)
    assert test_count["that"] == 2, f"count_words failed to count correct count of \'that\' in sample text: {text}"
    assert test_count[","] == 3, f"count_words failed to count correct count of  \',\' in sample text: {text}"
    assert test_count["."] == 1, f"count_words failed to count  correct count of  \'.\' in sample text: {text}"


def test_count_words_raven_count_that(read_raven):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a count of the word that
    test_count = count_words(read_raven)
    assert test_count["that"] == 100, f"count_words failed to count correct count of \'that\' in sample text: pg17192.txt. Go back and calculate correct count of  word \'that\'"


@pytest.mark.parametrize("book_file",["pg17192.txt","pg932.txt","pg1063.txt","pg10031.txt"])
def test_count_words_dict_parametrize(book_file):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary with the counts of each unique word (not case sensitive)    
    test_count = count_words(book_file)
    assert isinstance(test_count, dict), f"count_words failed to return dict on sample text: {book_file}"

def test_count_words_all_english_dict():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary with the counts of each unique word (not case sensitive) 
    test_count = count_words(read_all_books())
    assert isinstance(test_count, dict), f"count_words failed to return dict on all English texts"

def test_count_words_french_1_line_dict():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `count_words()` function
    # I should get a dictionary with the counts of each unique word (not case sensitive)

    text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    test_count = count_words(text)
    assert isinstance(test_count, dict), f"count_words failed to return dict on sample text: {text}"

@pytest.mark.integration
def test_count_words_complex_punctuation():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` followed by the `count_words()` function
    # I should get a dictionary that counts unique words (not case sensitive)
    # Note that count_words() function tokenizes a string using the relevant functions, so each test of count_words() is an integration test
    text = "But!the,Raven,.sitting lonely on,the placid bust,--spoke only That one word,?as if his soul in,that one word he did outpour."
    cleaned_text = clean_text(text)
    test_count = count_words(cleaned_text)
    assert test_count["that"] == 2, f"count_words failed to correctly count of \'that\' in sample text: {text}"
    assert "-" not in test_count.keys(), f"clean_text failed to correctly clean the text supplied to count_words in sample text: {text}"
    assert test_count["the"] == 2, f"count_words failed to correctly count \'the\' in sample text: {text}"
