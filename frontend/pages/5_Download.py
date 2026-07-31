import streamlit as st
import requests
import time

st.title("📥 Download File")

if "token" not in st.session_state:

    st.warning("Please login first")

    st.stop()

res = requests.get(

    "http://127.0.0.1:8000/files",

    headers={
        "token": st.session_state.token
    }
)

data = res.json()

files = data.get("files", [])

if not files:

    st.info("No uploaded files")

    st.stop()

file_names = [

    file["filename"]

    for file in files
]

selected = st.selectbox(
    "Select File",
    file_names
)

selected_file = next(

    file for file in files

    if file["filename"] == selected
)

st.write("### File Details")

st.write("📄 Filename:", selected_file["filename"])

st.write("🔗 CID:", selected_file["cid"])

st.write("🔐 Hash:", selected_file["hash"])

if st.button("Download File"):

    with st.spinner("Decrypting file..."):

        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.01)

            progress.progress(i + 1)

        res = requests.post(

            "http://127.0.0.1:8000/download",

            headers={
                "token": st.session_state.token
            },

            data={

                "cid": selected_file["cid"],

                "key": selected_file["key"],

                "nonce": selected_file["nonce"],

                "tag": selected_file["tag"],

                "filename": selected_file["filename"]
            }
        )

    if res.status_code == 200:

        st.success("File Ready")



        st.download_button(

            label="Save File",

            data=res.content,

            file_name=selected_file["filename"],

            mime="application/octet-stream"
        )

    else:

        st.error("Download failed")