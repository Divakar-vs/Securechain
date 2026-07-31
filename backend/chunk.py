def split_file(data, size=1024*1024):
    return [data[i:i+size] for i in range(0, len(data), size)]

def merge_chunks(chunks):
    return b"".join(chunks)