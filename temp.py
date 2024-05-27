import pickle
import streamlit as st
import requests
import pandas as pd 

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie /{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[0])), reverse=True, key = lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].title
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters
        



st.title('Movie Recommendation System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values)


if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[4])
        st.image(posters[4])
    with col5:
        st.text(names[4])
        st.image(posters[4])




