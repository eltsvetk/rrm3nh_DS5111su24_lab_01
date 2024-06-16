import re

def clean_text(a_text):
    print("Checking that input to clean_text() is string...")
    assert type(a_text) is str
    print("passed")
    
    lower_case_a_text = a_text.lower()
    ## Remove anything that is not a lowercase letter, number, or white space character
    lower_case_a_text = re.sub(r"[^a-z0-9\s]","",lower_case_a_text)
    
    return(lower_case_a_text)


def tokenize(a_text):
    print("Checking that input to tokenize() is string...")
    assert type(a_text) is str
    print("passed")
    
    a_text_tokenized = re.split(r"\s+",a_text)
    
    return(a_text_tokenized)

def count_words(a_text):
    print("Checking that input to counts_words() is string...")
    assert type(a_text) is str
    print("passed")
    
    clean_a_text = clean_text(a_text)
    tokenized_a_text = tokenize(clean_a_text)
    
    word_count_dict = {}
    for word in tokenized_a_text:
        if word not in word_count_dict:
            word_count_dict[word] = 0
        word_count_dict[word] += 1
    
    return(word_count_dict)

def main():
    test_case = "This [is] a {test}. case! <We are making?> sure that this will work okay-"
    
    test_clean = clean_text(test_case)
    print("Checking that return type from clean_text() is string...")
    assert type(test_clean) is str
    print("passed")
    print("Testing that clean_text() removes all punctuation...")
    assert re.match(r"[^a-z0-9\s]",test_clean) is None
    print("passed")
    print("Testing that all letters are lower case...")
    assert re.match(r"[A-Z]",test_clean) is None
    print("passed")
    print("")
    
    tokenized_test = tokenize(test_clean)
    print("Checking that return type from tokenize() is list...")
    assert type(tokenized_test) is list
    print("passed")
    print("Testing that tokenize() splits into correct number of words...")
    assert len(tokenized_test) == 14
    print("passed")
    print("")

    test_count = count_words(test_case)
    print("Checking that return type from counts_words() is dict...")
    assert type(test_count) is dict
    print("passed")
    print("Testing that count_words() dictionary has the correct number of keys...")
    assert len(test_count.keys()) == 13
    print("passed")
    print("Testing that count_words() correctly gets number of words...")
    assert test_count["this"] == 2
    assert test_count["a"] == 1
    print("passed")
    print("Testing that count_words() does not have an punctuation keys...")
    for punctuation in [".","?","!",";",",","-","_","/",":","$","|",">","<","[","]","{","}"]:
        assert punctuation not in test_count.keys()
    print("passed")


if __name__ == "__main__":
    main()

    



