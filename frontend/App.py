import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="SecureChain",
    page_icon="🔐",
    layout="wide"
)

# ---------------- LOAD LOTTIE ---------------- #

def load_lottie(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

# Cyber security animation
lottie_security = load_lottie(
    "https://assets9.lottiefiles.com/packages/lf20_gxcnsfk2.json"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown(
    """
    <style>

    .stApp {

        background: linear-gradient(
            to right,
            #0F172A,
            #111827
        );

        color: white;
    }

    .main-title {

        font-size: 60px;

        font-weight: bold;

        color: white;

        animation: fadeIn 1s ease-in;
    }

    .subtitle {

        font-size: 25px;

        color: #CBD5E1;

        animation: fadeIn 2s ease-in;
    }

    .feature-card {

        background-color: #1E293B;

        padding: 25px;

        border-radius: 18px;

        margin-top: 15px;

        box-shadow: 0px 0px 15px rgba(0,0,0,0.3);

        min-height: 240px;

        animation: fadeIn 1s ease-in;
    }

    .feature-card:hover {

        transform: scale(1.03);

        transition: 0.3s;

        box-shadow: 0px 0px 20px #2563EB;
    }

    .feature-title {

        font-size: 30px;

        font-weight: bold;

        color: white;
    }

    .feature-text {

        font-size: 18px;

        color: #CBD5E1;
    }

    .welcome-box {

        background-color: #172554;

        padding: 35px;

        border-radius: 20px;

        margin-bottom: 30px;

        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {

        from {

            opacity: 0;

            transform: translateY(20px);
        }

        to {

            opacity: 1;

            transform: translateY(0px);
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🔐 SecureChain")

st.sidebar.success("Secure Decentralized Storage")

st.sidebar.info(
    """
Navigate using the pages menu above.

Available Modules:

• Register  
• Login  
• Upload  
• Download  
• Transfer  
• Received  
• Transactions  
"""
)

# ---------------- HEADER ---------------- #

col1, col2 = st.columns([2,1])

with col1:

    st.markdown(
        """
        <div class="welcome-box">

        <div class="main-title">
        🔐 SecureChain
        </div>

        <br>

        <div class="subtitle">
        Secure File Storage and Transfer
        using Blockchain-inspired Architecture
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st_lottie(
        lottie_security,
        height=250,
        key="security"
    )

# ---------------- INTRO ---------------- #

st.write(
    """
SecureChain provides encrypted decentralized file storage using:

- AES Encryption
- SHA-256 Hashing
- IPFS Decentralized Storage
- JWT Authentication
- Blockchain-style Transaction Chaining

The system supports secure upload, download, transfer, and transaction tracking.
"""
)

# ---------------- FEATURE CARDS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-card">

        <div class="feature-title">
        🔒 AES Encryption
        </div>

        <br>

        <div class="feature-text">

        Files are securely encrypted before storage to ensure confidentiality and protection from unauthorized access.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-card">

        <div class="feature-title">
        🌐 IPFS Storage
        </div>

        <br>

        <div class="feature-text">

        Encrypted files are stored in decentralized IPFS storage for distributed and reliable access.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-card">

        <div class="feature-title">
        ⛓ Blockchain Security
        </div>

        <br>

        <div class="feature-text">

        SHA-256 transaction chaining provides integrity verification and tamper resistance.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- FEATURES ---------------- #

st.markdown("## 🚀 Core Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✔ Secure File Upload")

    st.success("✔ Secure File Download")

    st.success("✔ AES Encryption")

    st.success("✔ SHA-256 Hashing")

with col2:

    st.success("✔ Secure File Transfer")

    st.success("✔ IPFS Decentralized Storage")

    st.success("✔ JWT Authentication")

    st.success("✔ Blockchain-style Transactions")

# ---------------- FOOTER ---------------- #

st.markdown(
    """
    <hr>

    <center>

    <p style='color:gray'>

    SecureChain © 2026

    </p>

    </center>
    """,
    unsafe_allow_html=True
)