import pytest
import re
from subprocess import check_output
from week_3_lab import tokenize

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


def test_tokenize_raven_1_line_is_list():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list representing continuous blocks of texts (i.e. no white spaces)
    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokenize_text = tokenize(text)
    assert isinstance(tokenize_text, list), f"tokenize failed to return list on sample text: {text}"
    
def test_tokenize_raven_1_line_correct_number_words():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list representing continuous blocks of texts (i.e. no white spaces)
    
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokenize_text = tokenize(text)
    assert len(tokenize_text) == 25, f"tokenize failed to split only on white space on sample text: {text}"
    

@pytest.mark.xfail
def test_tokenize_raven_1_line_with_separate_punctuation():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list that tokenizes on words and punctuation for ending sentences or separating parts of a sentence (".",",",etc.) -- not currently implemented
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokenize_text = tokenize(text)
    assert len(tokenize_text) == 29, f"tokenize failed to split on white space and certain punctuation on sample text: {text}"
    
def test_tokenize_raven_is_list(read_raven):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list representing continuous blocks of texts (i.e. no white spaces)
    tokenize_text = tokenize(read_raven)
    assert isinstance(tokenize_text, list), f"tokenize failed to return list on sample file: pg17192.txt"
    


def test_tokenize_raven_correct_number_words(read_raven):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list that contains all words in the __text__ as a return
    tokenize_text = tokenize(read_raven)
    bash_wc = int(check_output(["wc", "-w", "pg17192.txt"]).split()[0]) 
    assert len(tokenize_text) == bash_wc, f"tokenize failed to return same number of words as bash command wc on sample file: pg17192.txt"
    

@pytest.mark.parametrize("book_file",["pg17192.txt","pg932.txt","pg1063.txt","pg10031.txt"])
def test_tokenize_is_list_parameterize(book_file):
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list representing continuous blocks of texts (i.e. no white spaces)
    tokenize_text = tokenize(read_book(book_file))
    assert isinstance(tokenize_text, list), f"tokenize failed to return list on sample file: {book_file}"


def test_tokenize_all_english_correct_num_words():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list that contains all words in the __text__ as a return
    tokenize_text = tokenize(read_all_books())
    bash_wc = int(check_output(["wc", "-w", "pg_17192_932_1063_10031.txt"]).split()[0])
    assert len(tokenize_text) == bash_wc, f"tokenize failed to return same number of words as bash command wc on sample file with all English texts"


def test_tokenize_french_1_line_is_list():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get a list representing continuous blocks of texts (i.e. no white spaces)

    text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    tokenize_text = tokenize(text)
    assert isinstance(tokenize_text, list), f"tokenize failed to return list on sample text: {text}"
