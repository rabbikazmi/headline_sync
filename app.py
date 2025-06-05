import streamlit as st
import requests

API_KEY = "e9f35a70dabfa17fc0f07fcff3bb2384"
BASE_URL = "https://gnews.io/api/v4/search"

#css
st.markdown("""
    <style>
        /* Gradient background */
        body {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            font-family: 'Poppins', sans-serif;
        }

        /* Title Styling */
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #fff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            padding: 20px;
            border-radius: 10px;
        }

        /* News Card */
        .news-card {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
            color: #fff;
        }

        /* News Title */
        .news-title {
            font-size: 22px;
            font-weight: bold;
            color: #ffd700;
        }

        /* News Description */
        .news-description {
            font-size: 18px;
            color: #e3e3e3;
        }

        /* Buttons */
        a {
            font-weight: bold;
            color: #00e6e6;
            text-decoration: none;
        }
        a:hover {
            color: #ffcc00;
        }

    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Headline Sync - News Aggregator</div>', unsafe_allow_html=True)
query = st.text_input("Search for news:")
category = st.selectbox("Select category", ["general", "business", "technology", "sports", "science", "health", "entertainment"])
if st.button("Get News"):
    params = {"q": query, "category": category, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        articles = response.json()["articles"]
        for article in articles:
            st.markdown(f"""
                <div class="news-card">
                    <div class="news-title">{article["title"]}</div>
                    <div class="news-description">{article["description"]}</div>
                    <a href="{article["url"]}" target="_blank">Read More</a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Failed to fetch news. Check your API key or network connection.")

