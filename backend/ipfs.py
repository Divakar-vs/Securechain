import requests


def upload_to_ipfs(data, filename):

    res = requests.post(
        "http://127.0.0.1:5001/api/v0/add",
        files={"file": (filename, data)}
    )

    cid = res.json()["Hash"]

    requests.post(
        "http://127.0.0.1:5001/api/v0/files/mkdir",
        params={
            "arg": "/securechain",
            "parents": "true"
        }
    )

    requests.post(
        "http://127.0.0.1:5001/api/v0/files/cp",
        params=[
            ("arg", f"/ipfs/{cid}"),
            ("arg", f"/securechain/{filename}")
        ]
    )

    return cid