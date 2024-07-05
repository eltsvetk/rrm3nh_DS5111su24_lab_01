Here we run tests on 3 functions: clean_text, tokenize and count_words. We do so on the Raven single file, all 4 english titles, the French version of the Raven, and finally all of them together.

The clean_text function takes a string and returns all lowercase words, while also throwing out punctation. The tokenize function takes a string and returns a python list, where each item is a word in a file. The count_words function takes a string and returns a dictionary with the words as keys and their counts as values. 

We test the clean_text function by the following tests:
* When given a string of text with words, do we successfully return a string
* When given a string of text with words, do we successfully return a string with no upper case letters
* When given a string of text with words, do we successfully return a string with no punctuation
* We also have a test that we expect to fail by testing if we return a string with all lowercase words except in the case of proper nouns. This has not been implemented in the function so we expect it to fail.
* There are 2 tests on the Raven single file, testing whether we return a string with all lowercase and no punctuation, and then testing if we return a string with no punctuation
* There is 1 test on all titles (English and French) and testing whether  we return a string that is all lowercase and no punctuation
* There is 1 test on all English titles testing whether we return a string with no punctuation
* There is 1 test on the French version testing whether we return a string with all lowercase and no punctation

Next we get fancy:
*  We have a test that hypothetically is expected to pass but can't be run because the test is on a Japanese version that we don't have yet, so it skips. 
* Then we have a test that requires a certain version of python, if less then it skips
* Similarly, have a test that requires a Linux based OS, otherwise it skips and gives warning message


We test the count_words function by the following tests:
* When given a string of text with words, should successfully return a dictionary with counts of each unique word
* When given a string of text, should return a dictionary with the length representing the number of unique words
* When given a string of text, should get a count of how many times the function counts the word 'that' and we test whether that number is right
* We have a test that we expect to fail because it is test should return a list that counts words and punctuation for ending sentences or separating parts of a sentence (".",",",etc.). However the function does not currently have this implemented, so we expect it to fail. 
* There is 1 test on the single Raven file. Similarly to the previous one, we expect it to fail. We should get a count of the word 'that' and it will be incorrect to the one inputted. Will provide message to go back and count the correct number of the word 'that' in the Raven file. 
* There is 1 test on all titles (English and French) and testing if we return a dictionary with counts of each unique word on the sample text
* there is 1 test on all English titles and testing if we return a dictionary with counts of each unique word
* There is 1 test on the French version that is testing if we return a dictionary with counts of each unique word

We test the tokenize function by the following tests:
* When given a string of text, testing if we receive a list representing continuous blocks of texts. 
* The following test has a similar goal but also testing if we return the correct number of items in a list.
* Next test is expected to fail. We are testing if we return a list that tokenizes on words and punctuation, which is not currently implemented
* There are 2 tests on the Raven file. First test is testing if we return a list representing continuous blocks of texts. 
* More fancy: Next test on Raven file is testing if we return the same number of words as bash command wc on the Raven file
* There is 1 test on all titles (English and French) and testing if we return a list representing continuous blocks of texts.
* More fancy: There is 1 test on all English titles and testing if we return the same number of words as bash command wc on all English texts 
* There is 1 test on the French version that is testing if we return a list representing continuous blocks of texts. 
