
import streamlit as st
from scrape import scrape_website


st.title("AI Web Scrapper")
url=st.text_input("Enter the website url:")


if st.button("scrape site"):
    st.write("Scrapping the website")
    result=scrape_website(url)
    print(result)
    
