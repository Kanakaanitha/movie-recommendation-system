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
    similarity_scores = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['title'])
        similarity_scores.append(round(i[1], 3))

    return recommended_movies, similarity_scores


# Button
if st.button("Recommend"):
    names, scores = recommend(selected_movie)

    st.subheader("Similar Movies:")
    for name, score in zip(names, scores):
        st.write(f"🎥 {name}  |  Similarity: {score}")