import streamlit as st
import pandas as pd
import pickle

#recommendations model
def recommendations(title, cos_sim, indices, df_list):
    recommend_movie = []

    idx = indices[indices == title].index[0]
    score_series = pd.Series(cos_sim[idx]).sort_values(ascending=False)
    top_10_indexes = list(score_series.iloc[1:11].index)

    for i in top_10_indexes:
        recommend_movie.append(list(df_list.index)[i])

    return recommend_movie

#load data
def load_data():
    with open('df.pkl', 'rb') as file:
        df = pickle.load(file)

    with open('cos_sim.pkl', 'rb') as file:
        cos_sim = pickle.load(file)

    with open('indices.pkl', 'rb') as file:
        indices = pickle.load(file)

    with open('df_list.pkl', 'rb') as file:
        df_list = pickle.load(file)

    return df, cos_sim, indices, df_list

#input data
def main():
    st.title('Movie/Series Recommendation System')
    
    #load data
    df, cos_sim, indices, df_list = load_data()

    # Add user input
    user_input = st.text_input ('Input title')
    
    if st.button('Make Recommendations'):
        recommendations_list = recommendations(user_input, cos_sim, indices, df_list)
        st.write('')
        st.write('**Recommended Movies/Series:**')
        for title_film in recommendations_list:
            st.write('-',title_film)

if __name__ == '__main__':
    main()