import time
import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Convert 'Course Rating' to numeric (in case there are any non-numeric entries)
    df['Course Rating'] = pd.to_numeric(df['Course Rating'], errors='coerce')
    
    return df

# Path to the CSV file
file_path = ("https://raw.githubusercontent.com/buddhima300/Courses_recommendation_app/main/Coursera.csv")

# Load the data
df = load_data(file_path)

# Display a message while loading
st.text('Loading data...')




# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/buddhima300/Courses_recommendation_app/main/Coursera.csv")

# Convert 'Course Rating' to numeric
df['Course Rating'] = pd.to_numeric(df['Course Rating'], errors='coerce')

# Function to recommend courses
def recommend_courses(difficulty=None, min_rating=0, skill=None):
    # Filter based on difficulty level
    recommendations = df[df['Difficulty Level'].str.lower().str.contains(difficulty.lower())] if difficulty else df
    # Filter based on minimum rating
    recommendations = recommendations[recommendations['Course Rating'] >= min_rating]
    # Filter based on skills if provided
    if skill:
        recommendations = recommendations[recommendations['Skills'].str.contains(skill, case=False, na=False)]
    # Return the recommended courses
    return recommendations[['Course Name', 'University', 'Course Rating', 'Difficulty Level', 'Skills']]

# Streamlit app
st.title('Online Courses Recommendation System')

# User inputs
difficulty = st.selectbox('Select Difficulty Level', ['All', 'Beginner', 'Intermediate', 'Advanced'])
min_rating = st.slider('Minimum Course Rating', 0.0, 5.0, 3.0)
skill = st.text_input('Enter a Skill (optional)')

# Recommend courses based on inputs
if difficulty == 'All':
    difficulty = None

recommendations = recommend_courses(difficulty=difficulty, min_rating=min_rating, skill=skill)

# Display recommendations
st.header('Recommended Courses')
if not recommendations.empty:
    progress_bar=st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete+1)
    st.write(recommendations)
else:
    st.write('No courses match your criteria.')


#showing data of Data columns
if st.sidebar.toggle('show Number of Courses'):
    st.sidebar.header('Number of courses')
    no_of_courses=df['Course Rating'].value_counts()
    st.sidebar.write(no_of_courses)

#showing the difficulty level with number of courses
if st.sidebar.checkbox('Difficulty Level and Course Count'):
    st.sidebar.header('Difficulty level')
    difficulty=df['Difficulty Level'].value_counts()
    st.sidebar.write(difficulty)

#showing the top Rated Universities with proress bar loading
Uni=df['University'].unique()
st.sidebar.subheader('Top rated Universities')
if st.sidebar.toggle('Top rated Universities'):
    progress_bar=st.sidebar.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete+1)
    st.sidebar.write(Uni)

