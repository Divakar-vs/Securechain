import streamlit as st
import requests
import time

st.title("👤 Register")

st.markdown("Create a SecureChain account")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Register"):

    with st.spinner("Creating account..."):

        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.01)

            progress.progress(i + 1)

        res = requests.post(

            "http://127.0.0.1:8000/register",

            data={
                "username": username,
                "password": password
            }
        )

    if res.status_code == 200:

        st.success("Registration successful")

        st.json(res.json())

    else:

        st.error("Registration failed")