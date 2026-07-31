import streamlit as st
import requests

st.title("📜 Transactions")

if "token" not in st.session_state:

    st.warning("Please login first")

    st.stop()

res = requests.get(

    "http://127.0.0.1:8000/transactions",

    headers={
        "token": st.session_state.token
    }
)

data = res.json()

transactions = data.get(
    "transactions",
    []
)

if not transactions:

    st.info("No transactions found")

    st.stop()

for tx in transactions:

    tx_type = tx.get("type", "")

    if tx_type == "UPLOAD":

        st.success(
            f"📤 UPLOAD → {tx.get('filename')}"
        )

    elif tx_type == "DOWNLOAD":

        st.info(
            f"📥 DOWNLOAD → {tx.get('filename')}"
        )

    elif tx_type == "TRANSFER":

        st.warning(
            f"🔄 TRANSFER → {tx.get('filename')}"
        )