import hashlib
import os
import zlib

def compute_sha1_and_store(content: bytes, obj_type="blob") -> str:
    header = f"{obj_type} {len(content)}\0".encode()
    store = header + content
    sha = hashlib.sha1(store).hexdigest()

    dir_path = f".ggit/objects/{sha[:2]}"
    file_path = f"{dir_path}/{sha[2:]}"

    print(f"[DEBUG] Writing object to {file_path}")

    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(zlib.compress(store))

    return sha