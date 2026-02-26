import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommendation System")

# Movie select box
selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['title'])

    return recommended_movies


# Button
if st.button("Recommend"):
    recommendation = recommend(selected_movie)

    st.subheader("Similar Movies:")
    for movie in recommendation:
        st.write(movie)
        