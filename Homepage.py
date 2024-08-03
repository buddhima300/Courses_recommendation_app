import pandas as pd
import streamlit as st 
#showing the courses distribution
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Welcome to online courses recommendation")
st.image('https://foundr.com/wp-content/uploads/2023/04/How-to-create-an-online-course.jpg')

st.info('This particular interactive application is designed to find out the best online courses which have higher ratings')
st.write('Following graphs and diagrams shows the top rated online courses')

#reading the dataset
df=pd.read_csv("https://raw.githubusercontent.com/buddhima300/Courses_recommendation_app/main/Coursera.csv")
dataset=df.head()
st.write(dataset)



st.info('This will show how the university courses are distibuted through this online platform')
# Count the number of courses offered by each university
university_course_counts = df['University'].value_counts()

# Create a bar plot for the distribution of courses by university
sns.set(style='whitegrid')
plt.figure(figsize=(50, 100))
sns.barplot(x=university_course_counts.values, y=university_course_counts.index, palette='viridis')
plt.xlabel('Number of Courses')
plt.ylabel('University')
plt.title('Distribution of Courses by University')

# Display the plot using Streamlit
st.pyplot(plt)

st.subheader('This graph is showing the boxplot of courses rating by difficulty level')
# Convert 'Course Rating' to numeric (in case there are any non-numeric entries)
df['Course Rating'] = pd.to_numeric(df['Course Rating'], errors='coerce')

# Set the style for the plot
sns.set(style='whitegrid')

# Create a boxplot for the distribution of course ratings by difficulty level
plt.figure(figsize=(12, 8))
sns.boxplot(x='Difficulty Level', y='Course Rating', data=df, palette='viridis')

# Add labels and title
plt.xlabel('Difficulty Level')
plt.ylabel('Course Rating')
plt.title('Boxplot of Course Ratings by Difficulty Level')

# Display the plot in Streamlit
st.pyplot(plt)



# Convert 'Course Rating' to numeric (in case there are any non-numeric entries)
df['Course Rating'] = pd.to_numeric(df['Course Rating'], errors='coerce')

# Set the style for plots
sns.set(style='whitegrid')

# Create a boxplot for the distribution of course ratings by difficulty level
st.header('Boxplot of Course Ratings by Difficulty Level')
plt.figure(figsize=(12, 8))
sns.boxplot(x='Difficulty Level', y='Course Rating', data=df, palette='viridis')
plt.xlabel('Difficulty Level')
plt.ylabel('Course Rating')
plt.title('Boxplot of Course Ratings by Difficulty Level')
st.pyplot(plt)

# Calculate the correlation matrix
correlation_matrix = df[['Course Rating']].corr()

# Create a heatmap for the correlation matrix
st.header('Correlation Heatmap')
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True, square=True, fmt='.2f')
plt.title('Correlation Heatmap')
st.pyplot(plt)


# Sample DataFrame for demonstration purposes
# Replace this with your actual DataFrame
df = pd.DataFrame({
    'Course Rating': ['Excellent', 'Good', 'Average', 'Excellent', 'Poor', 'Good', 'Poor', 'Excellent']
})

# Streamlit application
st.title('Course Ratings Analysis')

# Create the plot
plt.figure(figsize=(18,7))
sns.countplot(data=df, x='Course Rating', palette='plasma')
plt.xlabel('Course Ratings', fontsize='16', color='blue')
plt.ylabel('Number of courses', fontsize='16', color='blue')
plt.xticks(fontsize='14', color='green')
plt.yticks(fontsize='14', color='red')
plt.title("Count of Course Ratings\n", fontsize=24, fontweight='bold', color='indigo')

# Display the plot in Streamlit
st.pyplot(plt)

# Optionally, you can use st.write to display the DataFrame or any additional information
st.write(df)


#Adding and side bar
st.sidebar.header('Number of courses')
no_of_courses=df['Course Rating'].value_counts()
st.sidebar.write(no_of_courses)