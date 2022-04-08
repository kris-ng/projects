import streamlit as st
import requests
import pandas as pd
import numpy as np
import pickle
from collections import Counter
model = pickle.load(open('TF-SVC.p', 'rb'))

st.title("Finding the mental state of reddit user")

user_input = st.text_input("Enter Reddit User")
api=(f'https://api.pushshift.io/reddit/search/submission/?author={user_input}&sort=asc&size=100')
st.write(f'The Reddit User selected: {user_input}')

if user_input:
    text_list = []
    with st.spinner('Collecting data in progress...Wait for it...'):
        for num in range(len(requests.get(api).json()['data'])):
            text_list.append(requests.get(api).json()['data'][num]['selftext'])
    st.success('Data Collection Completed!')

    df = pd.DataFrame({'text':text_list, 'label':np.nan})
    df = df.replace('', np.nan)
    df = df[df['text'].notna()]
    df = df[df["text"].str.contains("removed")==False]
    df.reset_index(drop=True,inplace=True)

    st.write("Predicting in progress...")
    my_bar = st.progress(0)
    for predict in range(len(df)):
        df['label'][predict]=model.predict([df['text'][predict]])
        my_bar.progress(int(predict/len(df)*100))
    df['label']=df['label'].map({1 : 'sadness', 2 : 'fear', 3: 'disgust', 4: 'anger', 5: 'neutral',
       6: 'surprise', 7:'joy'})

    st.write("The data display is now shown below:")
    st.dataframe(df)
    
    st.write(Counter(df['label']))