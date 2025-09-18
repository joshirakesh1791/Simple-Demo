import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Complex Streamlit App")

# Sidebar inputs
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name:")
number = st.sidebar.slider("Select a number:", 1, 100, 50)

# Main content
if user_name:
    st.write(f"Hello, {user_name}!")
else:
    st.write("Please enter your name in the sidebar.")

# Generate random data and display a table
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)
st.write("Here is a random dataset:")
st.dataframe(data)

# Plotting functionality
st.write("Here is a random plot:")
fig, ax = plt.subplots()
data['A'].plot(kind='line', ax=ax)
st.pyplot(fig)

# Adding interactivity: Calculate square of the selected number
