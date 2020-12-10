import streamlit as st
from textblob import TextBlob
st.title("Sentiment Analysis App")
msg = st.text_area("Please add some data here")
isclicked = st.button("analyse the data")
if isclicked and msg:
    with st.spinner("analysing"):
        blob = TextBlob(msg)
        result = {'pos':{},'neg':{},'neutral':{}}
        total_pol = []
        for sentence in blob.sentences:
            pol = sentence.sentiment.polarity
            total_pol.append(pol)
            if pol>0:
                result['pos'][str(sentence)] = pol
            elif pol<0:
                result['neg'][str(sentence)] = pol
            else:
                result['neutral'][str(sentence)] = pol
    st.write(result)
    avg_pol = sum(total_pol)/len(total_pol)
    if avg_pol>0:
        ans = 'positive'
    elif avg_pol<0:
        ans = 'negative'
    else:
        ans = 'neutral'
    st.success(f'Data has {avg_pol} average polarity which makes it {ans}')
