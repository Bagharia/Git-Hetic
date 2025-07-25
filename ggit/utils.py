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

def get_object(sha: str) -> bytes:
    """Récupère le contenu d'un objet Git par son SHA"""
    dir_path = f".ggit/objects/{sha[:2]}"
    file_path = f"{dir_path}/{sha[2:]}"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Object {sha} not found")
    
    with open(file_path, "rb") as f:
        compressed_data = f.read()
    
    return zlib.decompress(compressed_data)