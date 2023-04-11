
# nltk Citation: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
# https://www.nltk.org/install.html
import nltk
# Brings the tokenizer from nltk kits, parses text into words
from nltk.tokenize import word_tokenize
# Bringing the n-grams model from nltk
from nltk.util import ngrams
# Imports a counter to count the created ngrams
from collections import Counter
# Imports a masssive corpus of text, around 100,000 words, inorder to influence the probablity of the functions
import nltk.corpus
# Imports random from the python library, want to use it later to randomly chose words to use
import random


# The corups is inputed in as a list, but must be a string inorder to lemmatize, so its turned into a string here
text = " ".join(nltk.corpus.abc.words())


def text_cleaner(text):
    # This parses the text word by word in a list
    text_split_up = word_tokenize(text)
    # Cleans Text
    for word in text_split_up:
        if word == '``' or word == ';':
            text_split_up.remove(word)
    return text_split_up


# Parses the text again but in three string object, ex: the dog went to the park. [["The","dog","went"],["went","to","the"],["park"]]
trigram_text = ngrams(text_cleaner(text), 3)
trigram_text_frq = Counter(trigram_text)

# Generates a random sentence based off of random selection
def generate_text(ngram_text_frq):
    new_sentence = " "
    # takes the parameter ngram and sorts it by its frequency
    new_ngram_ratio = ngram_text_frq.most_common()
    first_word = "the"

    while "." not in new_sentence:
        # Creates a list comprehension of the all objects in the new_ngram_ratio, only including the ones starting with first_word 
        current_ngrams = [ngram for ngram in new_ngram_ratio if ngram[0][0] == first_word]
        next_word = random.choice(current_ngrams)
        new_sentence += " " + next_word[0][0] + " " + next_word[0][1]
        # updates first word so it can recreate a new list comprehension from the new_ngram_ratio starting with the updated word
        first_word = next_word[0][-1]


    # Cleans up the sentence by cuting off everything added by the period
    if "." in new_sentence:
        new_sentence = new_sentence[0:new_sentence.find(".")]
                    
    return new_sentence


# calls and prints the generate_text function with its specific perameter 
print(generate_text(trigram_text_frq))


