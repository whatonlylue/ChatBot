import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

text = """They had no proof. He knew that they knew he had done it but they didn't have any proof. 
It was a huge distinction and it was the difference between him keeping his freedom or being locked away for decades. 
They continued to question him, probing him for information that they could use against him or find the proof they 
needed to put him away. He smiled and continued to block their every inquiry by feigning his innocence for a crime 
they all knew he committed. """


text_split_up = word_tokenize(text)
text_id = nltk.pos_tag(text_split_up)

new_text_id = []
for word in text_id:
    
    if word[-1] == 'JJ':
        new_word = lemmatizer.lemmatize(word[0], pos="a")
        new_text_id.append(new_word)
    else:
        new_text_id.append(word[0]) 

print(new_text_id)