import streamlit as st
import requests
import time

st.title("🔑 Login")

st.markdown("Login to SecureChain")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    with st.spinner("Authenticating..."):

        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.01)

            progress.progress(i + 1)

        res = requests.post(

            "http://127.0.0.1:8000/login",

            data={
                "username": username,
                "password": password
            }
        )

    if res.status_code == 200:

        data = res.json()

        st.session_state.token = data["token"]

        st.success("Login successful")



    else:

        st.error("Invalid credentials")