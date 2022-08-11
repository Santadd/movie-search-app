import json
from turtle import pos
import streamlit as st
import requests
apikey = "56c370de"
# Get user input
title = st.text_input("Enter movie title and press enter")
if title:
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={apikey}"
        # Get response
        resp = requests.get(url)
        json_resp = resp.json()
        # Create columns
        col1, col2 = st.columns([1, 2])
        # Put Image in column one
        with col1:
            poster = json_resp['Poster']
            if not poster:
                st.write('Image not found')
            else:
                st.image(poster)
        # Title and other details
        with col2:
            st.subheader(json_resp['Title'])
            st.caption(f"Genre: {json_resp['Genre']}")
            st.caption(f"Year: {json_resp['Year']}")
            st.write(json_resp['Plot'])
            st.text(f"Rating: {json_resp['imdbRating']}")
            # Progress bar
            st.progress(float(json_resp['imdbRating'])/10)
            
    except:
        st.error("We could not find any movie")