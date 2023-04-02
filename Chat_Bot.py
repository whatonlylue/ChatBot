
# nltk Citation: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
import nltk
# Brings the tokenizer from nltk kits, parses text into words
from nltk.tokenize import word_tokenize
# Brings the lemmatizer from nltk kits, simplifies words into there base form 
from nltk.stem import WordNetLemmatizer
# Activation of the lemmatizer
lemmatizer = WordNetLemmatizer()
# Bringing the n-grams model from nltk
from nltk.util import ngrams
# Imports a counter to count the created ngrams
from collections import Counter

text = """They had no proof. He knew that they knew he had done it but they didn't have any proof. 
It was a huge distinction and it was the difference between him keeping his freedom or being locked away for decades. 
They continued to question him, probing him for information that they could use against him or find the proof they 
needed to put him away. He smiled and continued to block their every inquiry by feigning his innocence for a crime 
they all knew he committed. """


# This is counts the total tokens in each text split by words, used later to compare to the ngram models to find a probability
def token_total(text):
    total = len(word_tokenize(text))
    return total
# Lemmatizes all words in the text, does a special lemmatizer for adjectives because they are missed by the regular settings
def text_cleaner(text):
    # This parses the text word by word in a list
    text_split_up = word_tokenize(text)
    # This then turns it into a 2d list buy appending what type of word to each list
    text_id = nltk.pos_tag(text_split_up)   
    new_text_id = []
    for word in text_id:
        if word[-1] == 'JJ':
            new_text_id.append(lemmatizer.lemmatize(word[0], pos="a"))
        else:
            new_text_id.append(lemmatizer.lemmatize(word[0])) 

    return new_text_id


bigram_text = ngrams(text_cleaner(text), 2)
bigram_text_frq = Counter(bigram_text)

trigram_text = ngrams(text_cleaner(text), 3)
trigram_text_frq = Counter(trigram_text)

print(trigram_text_frq)