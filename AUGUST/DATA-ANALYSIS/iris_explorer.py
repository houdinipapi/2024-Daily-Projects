import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Title and description
st.title("Iris Dataset Explorer")
st.write("This app allows you to explore the Iris dataset.")

# Sidebar for user input
st.sidebar.header("User Input")
species = st.sidebar.multiselect(
    "Select Species:",
    options=iris['species'].unique(),
    default=iris['species'].unique()
)

# Filter dataset based on user input
filtered_data = iris[iris['species'].isin(species)]

# Display the filtered dataset
st.write(f"#### Dataset ({len(filtered_data)} samples)")
st.dataframe(filtered_data)

# Plot
st.write("### Pairplot of the Selected Species")
fig = sns.pairplot(filtered_data, hue='species')
st.pyplot(fig)

# Summary statistics
st.write("### Summary Statistics")
st.write(filtered_data.describe())