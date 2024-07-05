import pytest
import re
import os,sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from week_3_lab import clean_text


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

def test_clean_text_raven_1_line_is_string():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string
    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_clean = clean_text(text)
    assert isinstance(test_clean, str), f"clean_text failed to return string (str) on sample text: {text}"
    

def test_clean_text_raven_1_line_no_upper_case():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string with no upper case letters as return
    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_clean = clean_text(text)
    assert re.search(r"[A-Z]",test_clean) is None, f"clean_text failed to convert all upper case to lower case in sample text: {text}"
    

def test_clean_text_raven_1_line_no_punctuation():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string with no punctuation as return
    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_clean = clean_text(text)
    assert re.search(r"[^a-z0-9\s]",test_clean) is None, f"clean_text failed to remove all punctuation in sample text: {text}"
    



@pytest.mark.xfail
def test_clean_text_raven_1_line_with_proper_nouns():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase except in the case of proper nouns (e.g., Elena) -- not currently implemented
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    test_clean = clean_text(text)
    assert re.search(r"Raven",test_clean) is not None, f"clean_text failed to correctly identify Raven as proper noun: {text}"
    

def test_clean_text_raven_is_str(read_raven):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase and no punctuation
    test_clean = clean_text(read_raven)
    assert isinstance(test_clean, str), f"clean_text failed to return string (str) on sample file: pg17192.txt"
    


def test_clean_text_raven_no_punctuation(read_raven):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string with no punctuation as return
    test_clean = clean_text(read_raven)
    assert re.search(r"[^a-z0-9\s]",test_clean) is None, f"clean_text failed to return string (str) on sample file: pg17192.txt"


@pytest.mark.parametrize("book_file",["pg17192.txt","pg932.txt","pg1063.txt","pg10031.txt"]) 
def test_clean_text_is_str_parametrize(book_file):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase and no punctuation
    test_clean = clean_text(read_book(book_file))
    assert isinstance(test_clean, str), f"clean_text failed to return string (str) on sample file: {book_file}"


def test_clean_text_all_english_no_punctuation():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string with no punctuation as return
    test_clean = clean_text(read_all_books())
    assert re.search(r"[^a-z0-9\s]",test_clean) is None, f"clean_text failed to return string (str) on sample file with all English texts"    

def test_clean_text_french_1_line_is_str():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase and no punctuation
    text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    test_clean = clean_text(text)
    assert isinstance(test_clean, str), f"clean_text failed to return string (str) on sample text: {text}"


@pytest.mark.skip(reason="no way of currently testing clean_text on Japanese characters")
def test_clean_text_japanese():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase and no punctuation
    #test_clean = clean_text("path to file with Japanese text")
    assert re.search(r"[^a-z0-9\s]",test_clean) is None, f"clean_text failed to return string (str) on sample file with Japanese characters"

@pytest.mark.skipif(sys.version_info[0:2] < (3,12),reason="This function has only been tested on python 3.12")
def test_clean_text_french_1_line_is_str_version():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase and no punctuation
    text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    test_clean = clean_text(text)
    assert isinstance(test_clean, str), f"clean_text failed to return string (str) on sample text: {text}"


@pytest.mark.skipif(sys.platform != "linux",reason="This function has only been tested on Linux based OS")
def test_clean_text_french_1_line_is_str_os():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `clean_text()` function
    # I should get a string all lowercase and no punctuation
    text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    test_clean = clean_text(text)
    assert isinstance(test_clean, str), f"clean_text failed to return string (str) on sample text: {text}"

