#importing required libraries
import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies.pkl','rb')) #loading movies.pkl file in movies_dict variable
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl','rb')) #loading similarity.pkl file in variable similarity



#fetching posters from api
def fetch_poster(movie_id) :
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ab13ab7a69c40bc380b19d94a22601cb&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


#function which return top 10 similar movies
def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11] #getting 10 similar movies

     recommended_movies = [] # making a empty list named recommended_movies
     recommended_movies_posters = []  # making a empty list named recommended_movie_posters
     for i in movies_list:
         movie_id = movies.iloc[i[0]].movie_id

         recommended_movies.append(movies.iloc[i[0]].title)  # appending titles of top 10 similar movies
         recommended_movies_posters.append((fetch_poster(movie_id)))  # appending posters of top 10 similar movies
     return recommended_movies,recommended_movies_posters




st.title('Movie Recommender System') #Giving title to the website

#Giving a dropdown list
selected_movie_name = st.selectbox\
('Select a movie from the list',
(movies['title'].values))


if st.button('Recommend'):
   names,posters = recommend(selected_movie_name)

#creating 10 columns having name and poster of the movie in each column
   col1, col2, col3, col4 = st.columns(4)

   with col1:
       st.text(names[0])
       st.image(posters[0])



   with col2:
        st.text(names[1])
        st.image(posters[1])



   with col3:
        st.text(names[2])
        st.image(posters[2])

   with col4:
        st.text(names[3])
        st.image(posters[3])

   col1, col2, col3, col4 = st.columns(4)

   with col1:
       st.text(names[4])
       st.image(posters[4])

   with col2:
       st.text(names[5])
       st.image(posters[5])

   with col3:
       st.text(names[6])
       st.image(posters[6])

   with col4:
       st.text(names[7])
       st.image(posters[7])

   col1, col2 = st.columns(2)

   with col1:
       st.text(names[8])
       st.image(posters[8])

   with col2:
       st.text(names[9])
       st.image(posters[9])

