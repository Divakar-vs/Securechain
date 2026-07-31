import streamlit as st
import requests
import time

st.title("📤 Upload File")

if "token" not in st.session_state:

    st.warning("Please login first")

    st.stop()

file = st.file_uploader(
    "Choose a file"
)

if file:

    if st.button("Upload File"):

        with st.spinner(
            "Encrypting and Uploading..."
        ):

            progress = st.progress(0)

            for i in range(100):

                time.sleep(0.02)

                progress.progress(i + 1)

            res = requests.post(

                "http://127.0.0.1:8000/upload",

                headers={
                    "token": st.session_state.token
                },

                files={
                    "file": (
                        file.name,
                        file.getvalue()
                    )
                }
            )

        if res.status_code == 200:

            data = res.json()

            st.success("Upload successful")



            st.json(data)

        else:

            st.error("Upload failed")

            st.write(res.text)