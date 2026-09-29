import streamlit as st
import numpy as np
from PIL import Image

from OCR import extract_text
from embedding import create_embeddings
from attention import calculate_attention

st.set_page_config(
    page_title=" Aura AI Attention Visualizer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(20,184,166,0.18), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(16,185,129,0.15), transparent 25%),
        radial-gradient(circle at 50% 90%, rgba(249,115,22,0.10), transparent 30%),
        #071817;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    padding: 35px;
    border-radius: 25px;
    background:
        linear-gradient(
            135deg,
            rgba(13,148,136,0.95),
            rgba(5,150,105,0.92),
            rgba(234,88,12,0.90)
        );
    box-shadow: 0 20px 60px rgba(20,184,166,0.22);
    margin-bottom: 30px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 17px;
    color: rgba(255,255,255,0.88);
}

.section-title {
    color: #f0fdfa;
    font-size: 25px;
    font-weight: 750;
    margin-top: 25px;
    margin-bottom: 15px;
}

.card {
    background: rgba(15,118,110,0.10);
    border: 1px solid rgba(94,234,212,0.16);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0 10px 35px rgba(0,0,0,0.20);
}

.stat-card {
    background:
        linear-gradient(
            135deg,
            rgba(20,184,166,0.12),
            rgba(255,255,255,0.035)
        );
    border: 1px solid rgba(94,234,212,0.15);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.stat-number {
    color: #ccfbf1;
    font-size: 30px;
    font-weight: 800;
}

.stat-label {
    color: rgba(204,251,241,0.62);
    font-size: 13px;
    margin-top: 5px;
}

.extracted-text {
    background: rgba(2,44,34,0.75);
    border-left: 4px solid #14b8a6;
    padding: 20px;
    border-radius: 12px;
    color: #d1fae5;
    line-height: 1.8;
}

.word-card {
    background: rgba(20,184,166,0.055);
    border: 1px solid rgba(94,234,212,0.10);
    border-radius: 15px;
    padding: 15px 18px;
    margin-bottom: 12px;
}

.word-name {
    color: #f0fdfa;
    font-size: 16px;
    font-weight: 700;
}

.attention-value {
    color: #5eead4;
    font-size: 13px;
    float: right;
}

.top-attention {
    background:
        linear-gradient(
            135deg,
            rgba(249,115,22,0.20),
            rgba(20,184,166,0.12)
        );
    border: 1px solid rgba(251,146,60,0.35);
    border-radius: 20px;
    padding: 25px;
    margin-top: 25px;
}

.top-title {
    color: #fb923c;
    font-size: 14px;
    font-weight: 600;
}

.top-word {
    color: #fff7ed;
    font-size: 30px;
    font-weight: 800;
    margin-top: 5px;
}

[data-testid="stFileUploader"] {
    background: rgba(20,184,166,0.055);
    border: 2px dashed rgba(45,212,191,0.55);
    border-radius: 20px;
    padding: 20px;
}

.stButton > button {
    border-radius: 12px;
    border: none;
    background: linear-gradient(
        90deg,
        #0d9488,
        #14b8a6,
        #f97316
    );
    color: white;
    font-weight: 700;
}

.stProgress > div > div > div > div {
    background: linear-gradient(
        90deg,
        #14b8a6,
        #2dd4bf,
        #fb923c
    );
}

[data-testid="stImage"] img {
    border-radius: 18px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.30);
}

.custom-footer {
    text-align: center;
    color: rgba(204,251,241,0.45);
    margin-top: 50px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🧠 AI Attention Visualizer
    </div>
    <div class="hero-subtitle">
        Extract text from images, analyze semantic embeddings,
        and visualize which words receive the highest attention.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📤 Upload Your Image</div>',
    unsafe_allow_html=True
)

file = st.file_uploader(
    "Drop an image here",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if file:

    image = Image.open(file)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:

        st.markdown(
            '<div class="section-title">🖼️ Input Image</div>',
            unsafe_allow_html=True
        )

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.markdown(
            '<div class="section-title">🔍 OCR Analysis</div>',
            unsafe_allow_html=True
        )

        with st.spinner("Extracting text from image..."):
            text = extract_text(image)

        if not text.strip():
            st.error("No text found in the image.")
            st.stop()

        st.markdown(
            f"""
            <div class="card">
                <div class="extracted-text">
                    {text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    words = text.split()

    words = [
        word.strip(".,!?;:()[]{}")
        for word in words
    ]

    words = [
        word
        for word in words
        if len(word) > 2
    ]

    words = words[:20]

    with st.spinner("Generating semantic embeddings..."):
        embeddings = create_embeddings(words)

    with st.spinner("Calculating attention scores..."):
        scores = calculate_attention(embeddings)

    st.markdown(
        '<div class="section-title">📊 Analysis Overview</div>',
        unsafe_allow_html=True
    )

    stat1, stat2, stat3, stat4 = st.columns(4)

    top_index = np.argmax(scores)
    top_word = words[top_index]

    with stat1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{len(words)}</div>
                <div class="stat-label">Words Analyzed</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with stat2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{len(text.split())}</div>
                <div class="stat-label">Words Extracted</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with stat3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{len(words)}</div>
                <div class="stat-label">Embeddings</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with stat4:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">⭐</div>
                <div class="stat-label">{top_word}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">🧠 Word Attention Analysis</div>',
        unsafe_allow_html=True
    )

    max_score = scores.max()

    if max_score == 0:
        display_scores = np.zeros_like(scores)
    else:
        display_scores = scores / max_score

    for word, score in zip(words, display_scores):

        st.markdown(
            f"""
            <div class="word-card">
                <span class="word-name">
                    {word}
                </span>
                <span class="attention-value">
                    {score:.2f}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(float(score))

    st.markdown(
        f"""
        <div class="top-attention">
            <div class="top-title">
                ⭐ HIGHEST ATTENTION
            </div>
            <div class="top-word">
                {top_word}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown("""
    <div class="card" style="text-align:center; padding:50px;">

        <div style="font-size:55px;">
            🖼️
        </div>

        <h2 style="color:#f0fdfa;">
            Upload an image to begin
        </h2>

        <p style="color:#99f6e4;">
            Your image will be processed using OCR,
            semantic embeddings and attention analysis.
        </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    AI Attention Visualizer • OCR + Embeddings + Attention Analysis
</div>
""", unsafe_allow_html=True)
