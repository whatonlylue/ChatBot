
# nltk Citation: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
import nltk
# Brings the tokenizer from nltk kits, parses text into words
from nltk.tokenize import word_tokenize
# Brings the lemmatizer from nltk kits, simplifies words into there base form 
from nltk.stem import WordNetLemmatizer
# Activation of the lemmatizer
lemmatizer = WordNetLemmatizer()

text = """They had no proof. He knew that they knew he had done it but they didn't have any proof. 
It was a huge distinction and it was the difference between him keeping his freedom or being locked away for decades. 
They continued to question him, probing him for information that they could use against him or find the proof they 
needed to put him away. He smiled and continued to block their every inquiry by feigning his innocence for a crime 
they all knew he committed. """

# This parses the text word by word in a list
text_split_up = word_tokenize(text)
# This then turns it into a 2d list buy appending what type of word to each list
text_id = nltk.pos_tag(text_split_up)

new_text_id = []
# Lemmatizes all words in the text, does a special lemmatizer for adjectives because they are missed by the regular settings
for word in text_id:
    if word[-1] == 'JJ':
        new_text_id.append(lemmatizer.lemmatize(word[0], pos="a"))
    else:
        new_text_id.append(lemmatizer.lemmatize(word[0])) 

print(new_text_id)