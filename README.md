🎬 Content-Based Movie Recommendation System with Streamlit:
Movie Recommendation System helps users discover movies based on their interests.
In this project, we developed a Content-Based Movie Recommendation System using Python, Machine Learning, and Streamlit.
The system recommends movies that are similar in content (such as overview, genre, and keywords) to the movie selected by the user.
📌 What is Content-Based Recommendation?
Content-based recommendation suggests items similar to the item selected by the user, based on item features.
It does not depend on other users’ data.

🔍 How It Works – Feature Engineering:
Combines text features is the process of converting raw data into meaningful features (overview,tags).
the overview text represents the movies\ content and is used to find similarity between movies.

*What is Vectorization?
Vectorization converts text (words) into numbers (vectors).
 Vectorization converts movie content text into numerical vectors using CountVectorizer, enabling similarity calculation between movies.

* What is Similarity Computation?
After vectorization, each movie is represented as a numeric vector.
Similarity computation compares these vectors to find movies with similar content
Similarity computation uses cosine similarity to compare movie content vectors and identify the most similar movies.
The recommendation logic selects the most similar movies by sorting cosine similarity scores of movie content vectors and displaying the top results.

🧠 Recommendation Logic
User selects a movie from the dropdown list
Movie features (genres, overview, cast, keywords) are combined
Text data is converted into numerical vectors using CountVectorizer
Cosine similarity is calculated between all movie vectors
Movies with the highest similarity scores are recommended
📌 Technologies Used
Python
Pandas – for data handling
Scikit-learn – for vectorization and similarity calculation
Streamlit – for building the web interface
Pickle – for saving and loading trained data


📌 Cosine Similarity
Cosine Similarity measures the similarity between two vectors by calculating the cosine of the angle between them.
It returns a value between 0 and 1, where higher value means more similarity.
