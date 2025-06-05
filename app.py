import streamlit as st
import requests

API_KEY = "e9f35a70dabfa17fc0f07fcff3bb2384"
BASE_URL = "https://gnews.io/api/v4/search"

#css
st.markdown("""
    <style>
/* Base Reset and Body */
body {
    margin: 0;
    padding: 0;
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
    overflow-x: hidden;
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    margin-top: 40px;
    background: linear-gradient(90deg, #00eaff, #a9f1df);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 10px rgba(0, 255, 255, 0.2);
}

/* Search Container */
.search-container {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin: 30px 0;
}

/* Search Box */
.search-box {
    width: 320px;
    padding: 14px 20px;
    border-radius: 50px;
    border: 1px solid rgba(255,255,255,0.3);
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    color: #fff;
    font-size: 16px;
    transition: 0.3s ease;
    outline: none;
}

.search-box::placeholder {
    color: #ccc;
}

/* Search Button */
.search-button {
    padding: 14px 24px;
    border-radius: 50px;
    background: linear-gradient(135deg, #00e6e6, #66ffe6);
    border: none;
    color: #1a1a1a;
    font-weight: bold;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s ease-in-out;
    box-shadow: 0 0 12px rgba(0,255,255,0.3);
}

.search-button:hover {
    background: linear-gradient(135deg, #66ffe6, #00e6e6);
    transform: scale(1.05);
}

/* News Card */
.news-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 24px;
    margin: 20px auto;
    max-width: 750px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease, box-shadow 0.3s;
}

.news-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 16px 32px rgba(0, 255, 255, 0.2);
}

/* News Title */
.news-title {
    font-size: 26px;
    font-weight: bold;
    font-family: 'Raleway', sans-serif;
    color: #76f9ff;
    margin-bottom: 10px;
    text-shadow: 0 2px 8px rgba(0,255,255,0.3);
}

/* News Description */
.news-description {
    font-size: 18px;
    color: #e2e2e2;
    line-height: 1.6;
    font-family: 'Lora', serif;
}

/* Links */
a {
    font-weight: bold;
    color: #00e6e6;
    text-decoration: none;
    transition: color 0.3s ease-in-out;
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

