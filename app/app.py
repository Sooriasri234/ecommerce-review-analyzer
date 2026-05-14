import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="E-Commerce Review Analyzer",
    page_icon="🛍️",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
    <style>
    .main {
        background: linear-gradient(
            135deg,
            #667eea 0%,
            #764ba2 100%
        );
    }

    .title {
        font-size: 50px;
        font-weight: bold;
        color: #4A90E2;
        text-align: center;
    }

    .subtitle {
        font-size: 22px;
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

   .feature-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);

        border: 1px solid rgba(255, 255, 255, 0.2);

        padding: 25px;
        border-radius: 20px;

        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);

        text-align: center;

        transition: 0.3s ease-in-out;
    }

    .feature-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.35);
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LANDING PAGE ---------------- #

st.markdown('<p class="title">🛍️ E-Commerce Product Review Analyzer</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Analyze customer reviews using AI-powered sentiment analysis</p>',
    unsafe_allow_html=True
)

# ---------------- HERO SECTION ---------------- #

col1, col2 = st.columns([1, 1])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1556740749-887f6717d7e4",
        use_container_width=True
    )

with col2:
    st.subheader("📌 About Project")

    st.write("""
    This AI-powered application helps businesses analyze customer reviews
    from e-commerce platforms.

    ✔ Detect Positive Reviews  
    ✔ Detect Negative Reviews  
    ✔ Analyze Customer Satisfaction  
    ✔ Visualize Review Insights  
    ✔ Improve Product Quality  
    """)

    st.button("🚀 Get Started")

# ---------------- FEATURES ---------------- #

st.markdown("## ✨ Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <h3>😊 Sentiment Analysis</h3>
        <p>Identify positive and negative customer reviews instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Data Visualization</h3>
        <p>View review insights using charts and analytics.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ AI Powered</h3>
        <p>Machine learning based intelligent review classification.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DEMO REVIEW SECTION ---------------- #

st.markdown("## 📝 Try Demo Review")

col1, col2, col3 = st.columns(3)

# ---------------- POSITIVE BUTTON ---------------- #

with col1:
    if st.button("😊 Positive Review"):
        st.success("Prediction: Positive Review")
        st.balloons()

        st.info("""
        Review:
        "This product is amazing! The quality is excellent and delivery was very fast."
        """)

# ---------------- NEGATIVE BUTTON ---------------- #

with col2:
    if st.button("😡 Negative Review"):
        st.error("Prediction: Negative Review")

        st.info("""
        Review:
        "Very disappointed with the product. It stopped working after two days."
        """)

# ---------------- NEUTRAL BUTTON ---------------- #

with col3:
    if st.button("😐 Neutral Review"):
        st.warning("Prediction: Neutral Review")

        st.info("""
        Review:
        "The product is okay for the price."
        """)

# ---------------- CUSTOM USER INPUT ---------------- #

st.markdown("---")

review = st.text_area("Enter Your Own Product Review")

if st.button("🚀 Analyze Review"):

    if review == "":
        st.warning("Please enter a review.")

    else:
        review_lower = review.lower()

        # SIMPLE DEMO PREDICTION LOGIC

        positive_words = [
            "good", "excellent", "amazing",
            "best", "love", "great",
            "fantastic", "awesome"
        ]

        negative_words = [
            "bad", "worst", "poor",
            "hate", "damaged", "disappointed"
        ]

        if any(word in review_lower for word in positive_words):
            st.success("✅ Prediction: Positive Review")

        elif any(word in review_lower for word in negative_words):
            st.error("❌ Prediction: Negative Review")

        else:
            st.warning("😐 Prediction: Neutral Review")

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">
    Developed using ❤️ with Streamlit
</div>
""", unsafe_allow_html=True)