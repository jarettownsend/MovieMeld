import streamlit as st
import pandas as pd
from moving_ranking import rank_movies

df = pd.read_csv('cleaned_movies.csv')

GENRE_OPTIONS = ['Drama', 'Crime', 'Action', 'Adventure', 'Biography', 'History',
       'Sci-Fi', 'Romance', 'Western', 'Fantasy', 'Comedy', 'Thriller',
       'Animation', 'Family', 'War', 'Mystery', 'Music', 'Horror',
       'Musical', 'Sport']

RUNTIME_PREFS = ['Medium', 'Very Short', 'Short', 'Long', 'Very Long']

RELEASE_CATEGORIES = ['Modern', 'Classic', 'All']

REVIEW_PREFS = ['Neutral', 'Critics', 'Audience']


st.title('🎬 Movie Matcher!')

st.header('User Preferences')

col1, col2 = st.columns(2)

with col1:
    st.subheader('User 1')
    genre1_user1 = st.selectbox('User 1 - Favorite Genre 1', GENRE_OPTIONS)
    genre2_user1 = st.selectbox('User 1 - Favorite Genre 2', GENRE_OPTIONS)
    genre3_user1 = st.selectbox('User 1 - Favorite Genre 3', GENRE_OPTIONS)
    review_pref_user1 = st.selectbox('User 1 - Reviews Preference', REVIEW_PREFS)
    runtime_pref_user1 = st.selectbox('User 1 - Runtime Preference', RUNTIME_PREFS)
    release_cat_user1 = st.selectbox('User 1 - Release Category', RELEASE_CATEGORIES)

with col2:
    st.subheader('User 2')
    genre1_user2 = st.selectbox('User 2 - Favorite Genre 1', GENRE_OPTIONS)
    genre2_user2 = st.selectbox('User 2 - Favorite Genre 2', GENRE_OPTIONS)
    genre3_user2 = st.selectbox('User 2 - Favorite Genre 3', GENRE_OPTIONS)
    review_pref_user2 = st.selectbox('User 2 - Reviews Preference', REVIEW_PREFS)
    runtime_pref_user2 = st.selectbox('User 2 - Runtime Preference', RUNTIME_PREFS)
    release_cat_user2 = st.selectbox('User 2 - Release Category', RELEASE_CATEGORIES)

# Button to trigger recommendation
if st.button('Find Movies'):
    inputs_1 = {
        'genre1': genre1_user1,
        'genre2': genre2_user1,
        'genre3': genre3_user1,
        'review_preference': review_pref_user1,
        'runtime_preference': runtime_pref_user1,
        'release_category': release_cat_user1
    }
    inputs_2 = {
        'genre1': genre1_user2,
        'genre2': genre2_user2,
        'genre3': genre3_user2,
        'review_preference': review_pref_user2,
        'runtime_preference': runtime_pref_user2,
        'release_category': release_cat_user2
    }

    ranked_movies = rank_movies(df.copy(), inputs_1, inputs_2)
    
    top_10 = ranked_movies.head(10)
    if not top_10.empty:
        random_top_3 = top_10.sample(min(3, len(top_10)))
        st.success('Here are 3 movie recommendations for you:')
        st.dataframe(random_top_3[['Series_Title', 'Overview', 'Director']])
    else:
        st.warning('No movies found matching your preferences. Try adjusting your inputs!')