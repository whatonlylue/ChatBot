
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
# Imports a masssive corpus of text, around 100,000 words, inorder to influence the probablity of the functions
import nltk.corpus
# Imports random from the python library, want to use it later to randomly chose words to use
import random


# The corups is inputed in as a list, but must be a string inorder to lemmatize, so its turned into a string here
text = " ".join(nltk.corpus.brown.words())



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

    for word in new_text_id:
        if word == '``' or word == ';':
            new_text_id.remove(word)
    return new_text_id

bigram_text = ngrams(text_cleaner(text), 2)
bigram_text_frq = Counter(bigram_text)

trigram_text = ngrams(text_cleaner(text), 3)
trigram_text_frq = Counter(trigram_text)





def generate_text(bigram_text_frq,text):
    new_sentence = " "
    new_bigram_ratio = bigram_text_frq.most_common()
    first_word = random.choice(text)
    new_sentence += first_word
    for i in range(6):
        for fword in new_bigram_ratio:
            if fword[0][0] == first_word:
                new_sentence += " " + fword[0][1]+ " " + fword[0][-1]
                first_word = fword[0][-1]
                break
                
    print(new_sentence)
        
generate_text(trigram_text_frq,text_cleaner(text))


# def ratio_maker(ngram_text_frq,text):
#     total = token_total(text)
#     new_ngram = ngram_text_frq.most_common(10)
#     replaced_ngram = []
#     for list in new_ngram:
#         inner = []
#         inner.append(list[0])
#         inner.append(list[1] / total) 
#         replaced_ngram.append(inner)
#     return replaced_ngram

# print(ratio_maker(trigram_text_frq,text))
