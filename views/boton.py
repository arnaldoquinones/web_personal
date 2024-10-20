import requests  # this is to GET the javascript 
import re  # regular expression for extracting the list of words
import streamlit as st  # web app development

# CSS customization for buttons
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0000FF;
    color: #ffffff;
}
div.stButton > button:hover {
    background-color: #FF0000;
    color: #ff99ff;
}
</style>
""", unsafe_allow_html=True)

# Function to extract the wordle solution list from the JavaScript source page
@st.cache_data
def extract_solution():
    wordle_js = requests.get("https://www.powerlanguage.co.uk/wordle/main.c1506a22.js")

    # Check if the request was successful
    if wordle_js.status_code != 200:
        st.error("Failed to retrieve data from Wordle website")
        return []

    # Print the first few lines of the response to debug the content
    st.write("First 500 characters of the JavaScript response:", wordle_js.text[:500])

    # Try to extract the list of words from the JavaScript file
    m = re.findall(r'var La=\[(.*?)\]', wordle_js.text, flags=re.S)

    # If we found the list, process it
    if m:
        word_list = m[0].replace('"', '').split(",")
        return word_list
    else:
        st.error("Could not find the word list in the JavaScript file.")
        return []

# Call the function to get the word list
word_list = extract_solution()

st.title("👻 Wordle Spoiler 👿")

# Input to get the Wordle number
index = st.text_input(label="Enter the Wordle Number for which you need the solution")

# Warning message
st.error("⚠️ Do you really want to do this? You can always play for fun!!!")

# Check if the button is pressed and a valid index is entered
if st.button("Yes I just want to spoil the mood") and index.isdigit():
    word_index = int(index)

    # Check if the index is within the range of the word list
    if 0 <= word_index < len(word_list):
        st.balloons()
        st.write(f"The solution for Wordle #{word_index} is: {word_list[word_index]}")
    else:
        st.error("The index you entered is out of range. Please enter a valid Wordle number.")
