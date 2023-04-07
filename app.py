import streamlit as st
import pickle
import altair as alt
import pandas as pd

popular_upload = pickle.load(open('./popular', 'rb'))
recommend_dict = pickle.load(open('./recommend_dict', 'rb'))
recommend_upload = pd.DataFrame(recommend_dict)
new_df = pd.concat([recommend_upload['antecedents'], recommend_upload['consequents']], ignore_index=True)

st.title('YumMatch :yum:')

st.header('Food Recommender System')
option = st.selectbox(
    'Finding Something Yummy?',
    new_df.unique()
)
if st.button('Recommend'):
    st.table(recommend_upload.loc[recommend_upload['antecedents'] == option])
    st.table(recommend_upload.loc[recommend_upload['consequents'] == option])

st.header('Popular Combos')
st.table(popular_upload)

st.header('Summary')
st.markdown('- Prepocessed a dataset that had client_id, order_id, item_name, quantity, price & date with 687911 entries.')
st.markdown('- Depending on the order_id and the date, we found out that what are the meals that are eaten together.')
st.markdown('- Depending on the above data, we found the data for the most popular meal combos.')
st.markdown('- With the help of Association Rules using Apriori, we found out that what meals will the customers like to have together.')
st.markdown('- We then deployed the app with the help of streamlit using localtunnel (Used colab because too many iterations were incompatible with the local GPU)')
