import streamlit as st

from scraper import (
    scrape_website,
    clean_body_content,
    extract_body_content
)
from parse import call_gpt_api

# Title
st.title("AI Scraper")

# Input URL
url = st.text_input("Enter the URL to scrape")

# Initialize session state for query and response
if "query" not in st.session_state:
    st.session_state.query = ""
if "gpt_response" not in st.session_state:
    st.session_state.gpt_response = ""
if "cleaned_content" not in st.session_state:
    st.session_state.cleaned_content = ""

# Scrape the website
if st.button("Scrape The Site"):
    st.write("I'm on it Boss, Scraping The Site...")
    result = scrape_website(url)
    body = extract_body_content(result)
    cleaned_content = clean_body_content(body)
    st.session_state.cleaned_content = cleaned_content  # Store in session state

    st.write("Scraped content successfully!")
    with st.expander("View Cleaned Content"):
        st.text_area("Cleaned Content", cleaned_content, height=300)

# Query Input
if st.session_state.cleaned_content:
    st.write("What do you want to ask?")
    st.session_state.query = st.text_input("Enter your query", key="query_input")

    if st.button("Submit"):
        st.write("Fetching response from GPT...")
        response = call_gpt_api("execute " + st.session_state.query + " in " + st.session_state.cleaned_content)
        st.session_state.gpt_response = response

# Display GPT Response
if st.session_state.gpt_response:
    st.write("Response from GPT API:")
    st.write(st.session_state.gpt_response)
