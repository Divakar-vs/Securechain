import streamlit as st
import requests
import time

# ---------------- PAGE TITLE ---------------- #

st.title("📩 Received Files")

st.markdown(
    """
Secure files transferred from other users
can be downloaded securely from here.
"""
)

# ---------------- LOGIN CHECK ---------------- #

if "token" not in st.session_state:

    st.warning("Please login first")

    st.stop()

# ---------------- FETCH RECEIVED FILES ---------------- #

with st.spinner("Loading received files..."):

    res = requests.get(

        "http://127.0.0.1:8000/received",

        headers={
            "token": st.session_state.token
        }
    )

# ---------------- RESPONSE CHECK ---------------- #

if res.status_code != 200:

    st.error("Failed to fetch received files")

    st.write(res.text)

    st.stop()

# ---------------- GET DATA ---------------- #

data = res.json()

files = data.get("files", [])

# ---------------- EMPTY CHECK ---------------- #

if not files:

    st.info("No received files available")

    st.stop()

# ---------------- FILE SELECTION ---------------- #

file_names = [

    f"{file['filename']}  ←  {file['sender']}"

    for file in files
]

selected = st.selectbox(
    "Select Received File",
    file_names
)

selected_index = file_names.index(selected)

selected_file = files[selected_index]

# ---------------- FILE DETAILS ---------------- #

st.markdown("## 📄 File Details")

col1, col2 = st.columns(2)

with col1:

    st.success(
        f"📁 Filename: {selected_file['filename']}"
    )

    st.info(
        f"👤 Sender: {selected_file['sender']}"
    )

with col2:

    st.warning(
        f"🔗 CID: {selected_file['cid']}"
    )

    st.success(
        f"🕒 Received: {selected_file['timestamp']}"
    )

# ---------------- DOWNLOAD SECTION ---------------- #

st.markdown("---")

st.markdown("## 📥 Secure Download")

st.write(
    """
Click below to securely download
and decrypt the transferred file.
"""
)

# ---------------- DOWNLOAD BUTTON ---------------- #

if st.button("Download Received File"):

    with st.spinner(
        "Decrypting and downloading..."
    ):

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

    # ---------------- SUCCESS ---------------- #

    if res.status_code == 200:

        st.success(
            "File decrypted successfully"
        )



        st.download_button(

            label="💾 Save File",

            data=res.content,

            file_name=selected_file["filename"],

            mime="application/octet-stream"
        )

    # ---------------- FAILURE ---------------- #

    else:

        st.error("Download failed")

        st.write(res.text)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption(
    "SecureChain • Decentralized Secure File Transfer"
)