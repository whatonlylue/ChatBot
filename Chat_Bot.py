
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


# Lemmatizes all words in the text, does a special lemmatizer for adjectives because they are missed by the regular settings
def text_cleaner(text):
    # This parses the text word by word in a list
    text_split_up = word_tokenize(text)
    # Cleans Text
    for word in text_split_up:
        if word == '``' or word == ';' or word =='.':
            text_split_up.remove(word)
    return text_split_up

trigram_text = ngrams(text_cleaner(text), 3)
trigram_text_frq = Counter(trigram_text)

def generate_text(ngram_text_frq):
    new_sentence = " "
    new_ngram_ratio = ngram_text_frq.most_common()
    first_word = "the"
    for i in range(5):
        current_ngrams = [ngram for ngram in new_ngram_ratio if ngram[0][0] == first_word]
        next_word = random.choice(current_ngrams)
        new_sentence += " " + next_word[0][0] + " " + next_word[0][1]
        first_word = next_word[0][-1]
            
                
    print(new_sentence)
        
generate_text(trigram_text_frq)


