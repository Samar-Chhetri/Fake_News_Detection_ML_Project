import streamlit as st
import pickle
import pandas as pd
import nltk
import string

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps = PorterStemmer()


# Function for text preprocessing
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for j in text:
        if j not in stopwords.words('english') and j not in string.punctuation:
            y.append(j)
            
    text = y[:]
    y.clear()
    
    for k in text:
        y.append(ps.stem(k))
        
    return " ".join(y)




# Load saved model
tfidf = pickle.load(open('model/vectorizer.pkl', 'rb'))
model = pickle.load(open('model/model.pkl', 'rb'))


st.title("Fake News Detection")


input_sms = st.text_area("Enter the News")

if st.button('Predict'):

    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Result :  The News looks SPAM")
    else:
        st.header("Result :  The News does NOT look SPAM")



