import pandas as pd

def get_runtime_category(runtime, user_preference):
    """Determine how well a movie's runtime matches the user's preference"""
    runtime_categories = {
        'Very Short': (0, 45),
        'Short': (45, 90),
        'Medium': (90, 120),  
        'Long': (120, 150),  
        'Very Long': (150, float('inf'))  
    }

    min_runtime, max_runtime = runtime_categories[user_preference]
    if min_runtime <= runtime <= max_runtime:
        return 3 
    elif (min_runtime - 30 <= runtime <= min_runtime + 30) or (max_runtime - 30 <= runtime <= max_runtime + 30):
        return 2 
    else:
        return 1 
    
def apply_genre_score(row, user_inputs):
    """Calculate the genre score based on user preferences and movie genres"""
    movie_genres = row['Genre'].split(', ') if pd.notna(row['Genre']) else []
    genre_points = {'genre1': 5, 'genre2': 3}
    
    max_points = 0
    for genre_key, points in genre_points.items():
        preferred_genre = user_inputs.get(genre_key)
        if preferred_genre:
            if any(preferred_genre.lower() in mg.lower() for mg in movie_genres):
                max_points = max(max_points, points)
    return max_points

def rank_movies(df, inputs_1, inputs_2):
    """
    Rank movies based on content rating and genre preferences from two users.
    
    df: DataFrame of movies.
    inputs_1: Dictionary with user 1's preferences.
    inputs_2: Dictionary with user 2's preferences. 
    Example:
        {'review_preference': 'Audience', 
        'genre1':'Comedy', 
        'genre2':'Drama',
        'release_category': 'Recent',
        'runtime_preference': 'Medium',}
    
    Returns: Best movies based on inputs from both users.
    """
    df['score'] = 0

    release_category_1 = inputs_1.get('release_category', None)
    release_category_2 = inputs_2.get('release_category', None)

    if release_category_1 == release_category_2:
        if release_category_1 == 'Modern':
            df = df[df['Release_Category'] == 'Modern']
        elif release_category_1 == 'Classic':
            df = df[df['Release_Category'] == 'Classic']

    critic_preference_1 = inputs_1.get('review_preference', 'Neutral')
    critic_preference_2 = inputs_2.get('review_preference', 'Neutral')

    if critic_preference_1 == 'Critics' and critic_preference_2 == 'Critics':
        critic_weight, audience_weight = 0.7, 0.3
    elif critic_preference_1 == 'Audience' and critic_preference_2 == 'Audience':
        critic_weight, audience_weight = 0.3, 0.7
    elif (critic_preference_1 == 'Critics' and critic_preference_2 == 'Neutral') or (critic_preference_2 == 'Critics' and critic_preference_1 == 'Neutral'):
        critic_weight, audience_weight = 0.6, 0.4
    elif (critic_preference_1 == 'Audience' and critic_preference_2 == 'Neutral') or (critic_preference_2 == 'Audience' and critic_preference_1 == 'Neutral'):
        critic_weight, audience_weight = 0.4, 0.6
    else:
        critic_weight, audience_weight = 0.5, 0.5

    df['score'] += (critic_weight * df['Normalized_Meta_Score']) + (audience_weight * df['IMDB_Rating'])

    for user_inputs in [inputs_1, inputs_2]:
        df['score'] += df.apply(lambda row: apply_genre_score(row, user_inputs), axis=1)

    df['score'] += df['Runtime_int'].apply(lambda x: get_runtime_category(x, inputs_1['runtime_preference']))
    df['score'] += df['Runtime_int'].apply(lambda x: get_runtime_category(x, inputs_2['runtime_preference']))

    df_sorted = df.sort_values(by='score', ascending=False)

    return df_sorted