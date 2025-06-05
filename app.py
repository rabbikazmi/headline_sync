import streamlit as st
import requests

API_KEY = "e9f35a70dabfa17fc0f07fcff3bb2384"
BASE_URL = "https://gnews.io/api/v4/search"

#css
st.markdown("""
    <style>
    @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Lora&family=Playfair+Display&family=Raleway:wght@600&display=swap" rel="stylesheet");
/* Background */
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #f8f9fa;
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
}

/* Title Styling */
.title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg, #ffe259, #ffa751);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Playfair Display', serif;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.1);
    margin: 40px 0 20px;
}

/* Search Container */
.search-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin-bottom: 40px;
}

/* Search Box */
.search-box {
    width: 320px;
    padding: 14px 20px;
    border-radius: 30px;
    border: 1px solid rgba(255,255,255,0.3);
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    color: #fff;
    font-size: 16px;
    outline: none;
    transition: all 0.3s ease-in-out;
}

.search-box::placeholder {
    color: #ccc;
}

/* Search Button */
.search-button {
    padding: 14px 24px;
    border-radius: 30px;
    border: none;
    background: linear-gradient(135deg, #ffd700, #ff9900);
    color: #1a1a1a;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: transform 0.2s ease, background 0.3s ease-in-out;
}

.search-button:hover {
    background: linear-gradient(135deg, #ffcc00, #ffae00);
    transform: scale(1.05);
}

/* News Card */
.news-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 24px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 700px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s;
}

.news-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.3);
}

/* News Title */
.news-title {
    font-size: 26px;
    font-weight: 700;
    color: #50d8d7;
    font-family: 'Raleway', sans-serif;
    margin-bottom: 10px;
}

/* News Description */
.news-description {
    font-size: 18px;
    line-height: 1.6;
    color: #e4e4e4;
    font-family: 'Lora', serif;
}

/* Links */
a {
    color: #00fff7;
    font-weight: 600;
    text-decoration: underline dotted;
    transition: color 0.3s ease;
}

a:hover {
    color: #ffdd57;
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

