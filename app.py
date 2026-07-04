import streamlit as st
import pandas as pd
import requests
from newspaper import Article
import nltk
from PIL import Image

st.set_page_config(
    page_title="NewsGuard AI",
    page_icon="📰",
    layout="wide"
)

st.title("📰 NewsGuard AI")
st.subheader("AI Powered News Analysis System")

st.markdown("---")

st.write("### Enter News URL")

url = st.text_input("Paste News URL Here")

if st.button("Analyze News"):

    if url == "":
        st.warning("Please enter a news URL.")
    else:
        try:
            article = Article(url)
            article.download()
            article.parse()

            st.success("News Loaded Successfully")

            st.write("## Title")
            st.write(article.title)

            st.write("## Authors")
            st.write(article.authors)

            st.write("## Publish Date")
            st.write(article.publish_date)

            st.write("## Article")
            st.write(article.text)

        except Exception:
            st.error("Unable to fetch article.")
