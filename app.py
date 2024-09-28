import streamlit as st
import dill as pickle
import requests
from pandas.core.strings.accessor import str_extractall
from select import select
import pandas as pd

try:
    def fetch_poster(movie_name):
        # my api  http://www.omdbapi.com/?i=tt3896198&apikey=57488d2a
        response = requests.get("https://www.omdbapi.com/?t={}&apikey=57488d2a".format(movie_name))
        data = response.json()
        # path = data["Poster"]
        # return path
        return data["Poster"]


    def recommend(movie):
        movie_index = movies[movies["original_title"] == movie].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]



        recommended_movies =[]
        recommended_movie_posters=[]
        poster_path=[]
        for i in movie_list:
            recommended_movies.append(movies.iloc[i[0]].original_title)
            poster_path.append(fetch_poster(movies.iloc[i[0]].original_title))

        return recommended_movies , recommended_movie_posters

    movie_dict= pickle.load(open("movie.pkl" , "rb"))
    movies = pd.DataFrame(movie_dict)
# movies["original_title"]

    similarity = pickle.load(open("similarity.pkl","rb"))




    st.title("Movies Recommendation system")



    out_list =["ayush ", "python-prog"]

    selected = st.selectbox( label = "type movie name here",options= movies["original_title"].values)

    if st.button(label="search now ", key=1, help="hit the button "):
        names, posters = recommend(selected)
        col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
    # st.header(names[0])
        st.image(fetch_poster(names[0]))
    with col2:
        st.text((names[1]))
        st.image(fetch_poster(names[1]))
    with col3:
        st.text(names[2])
        st.image(fetch_poster(names[2]))
    with col4:
        st.text(names[3])
        st.image(fetch_poster(names[3]))
    with col5:
        st.text(names[4])
        st.image(fetch_poster(names[4]))


except:
    st.write("Click on search button or  please try other movies ")









