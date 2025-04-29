import streamlit as st
import pandas as pd
from moving_ranking import rank_movies

df = pd.read_csv('cleaned_movies.csv')

GENRE_OPTIONS = ['Drama', 'Comedy', 'Action', 'Adventure', 'Biography', 'History',
       'Sci-Fi', 'Romance', 'Western', 'Fantasy', 'Thriller', 'Crime',
       'Animation', 'Family', 'War', 'Mystery', 'Music', 'Horror',
       'Musical', 'Sport']

RUNTIME_PREFS = ['Very Short', 'Short', 'Medium', 'Long', 'Very Long']

RELEASE_CATEGORIES = ['Modern', 'Classic', 'All']

REVIEW_PREFS = ['Neutral', 'Critics', 'Audience']


st.title('🎬 Movie Matcher!')

st.header('User Preferences')

col1, col2 = st.columns(2)

with col1:
    st.subheader('User 1')
    genre1_user1 = st.selectbox('Favorite Genre 1 ', GENRE_OPTIONS, index=0)
    genre2_user1 = st.selectbox('Favorite Genre 2 ', GENRE_OPTIONS, index=1)
    review_pref_user1 = st.selectbox('Reviews Preference ', REVIEW_PREFS)
    runtime_pref_user1 = st.selectbox('Runtime Preference ', RUNTIME_PREFS, index=2)
    release_cat_user1 = st.selectbox('Release Category ', RELEASE_CATEGORIES, index=2)

with col2:
    st.subheader('User 2')
    genre1_user2 = st.selectbox('Favorite Genre 1', GENRE_OPTIONS, index=0)
    genre2_user2 = st.selectbox('Favorite Genre 2', GENRE_OPTIONS, index=1)
    review_pref_user2 = st.selectbox('Reviews Preference', REVIEW_PREFS)
    runtime_pref_user2 = st.selectbox('Runtime Preference', RUNTIME_PREFS, index=2)
    release_cat_user2 = st.selectbox('Release Category', RELEASE_CATEGORIES, index=2)

# Button to trigger recommendation
if st.button('Find Movies'):
    inputs_1 = {
        'genre1': genre1_user1,
        'genre2': genre2_user1,
        'review_preference': review_pref_user1,
        'runtime_preference': runtime_pref_user1,
        'release_category': release_cat_user1
    }
    inputs_2 = {
        'genre1': genre1_user2,
        'genre2': genre2_user2,
        'review_preference': review_pref_user2,
        'runtime_preference': runtime_pref_user2,
        'release_category': release_cat_user2
    }

    ranked_movies = rank_movies(df.copy(), inputs_1, inputs_2)
    
    top_10 = ranked_movies.head(10)
    if not top_10.empty:
        random_top_3 = top_10.sample(min(3, len(top_10)), random_state=42)
        for _, row in random_top_3.iterrows():
            cols = st.columns([1, 5]) 
            with cols[0]:
                st.image(row['Poster_Link'], use_container_width=True)
            with cols[1]:
                st.markdown(f"""
                    <h5 style='margin-bottom: 0.2rem; line-height: 0.2;'>{row['Series_Title']} 
                        <span style='font-size: 0.8rem; color: grey;'>({row['Genre']})</span>
                    </h5>
                    <div style='display: flex; justify-content: space-between; font-size: 0.9rem; color: grey;'>
                        <p style='margin: 0;'>Director: {row['Director']}</p>
                        <p style='margin: 0;'>Runtime: {int(row['Runtime_int'])} minutes</p>
                    </div>
                """, unsafe_allow_html=True)
                st.write(f"{row['Overview']}")
    else:
        st.warning('No movies found matching your preferences. Try adjusting your inputs!')