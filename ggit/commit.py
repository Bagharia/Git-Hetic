import os
import time
from ggit.write_tree import write_tree
from ggit.commit_tree import commit_tree

def lire_HEAD():
    """Lit le commit actuel depuis HEAD"""
    try:
        with open(".ggit/HEAD", "r") as f:
            ref = f.read().strip()
        
        # Si HEAD pointe vers une branche
        if ref.startswith("ref: "):
            ref_path = ".ggit/" + ref[5:]  # Enlève "ref: "
            if os.path.exists(ref_path):
                with open(ref_path, "r") as f:
                    return f.read().strip()
        return None
    except:
        return None
    
def mettre_a_jour_HEAD(nouveau_commit):
    """Met à jour HEAD avec le nouveau commit"""
    try:
        # Lit la référence actuelle
        with open(".ggit/HEAD", "r") as f:
            ref = f.read().strip()
        
        # Met à jour la branche
        if ref.startswith("ref: "):
            ref_path = ".ggit/" + ref[5:]
            with open(ref_path, "w") as f:
                f.write(nouveau_commit)
    except Exception as e:
        print(f"Erreur lors de la mise à jour de HEAD: {e}")

def it_commit(message):
    """Fait un commit simple avec le message donné"""
    
    # 1. Créer l'arbre à partir des fichiers dans l'index
    tree_sha = write_tree()
    
    # Vérifier qu'il y a quelque chose à commiter
    if not tree_sha:
        print("Rien à commiter. L'index est vide.")
        return
    
        # 2. Récupérer le commit parent (HEAD actuel)
    parent_commit = lire_HEAD()
    
    # 3. Créer le nouveau commit
    commit_sha = commit_tree(tree_sha, message, parent_commit)
    
    # 4. Mettre à jour HEAD
    mettre_a_jour_HEAD(commit_sha)
    
    # 5. Afficher le résultat
    print(f"Commit créé: {commit_sha}")
    print(f"Message: {message}")
    
    if parent_commit:
        print(f"Parent: {parent_commit}")
    else:
        print("Premier commit!")
        
def read_tree_recursive(tree_sha):
    """Lit récursivement un arbre et retourne tous les fichiers avec leurs chemins"""
    from ggit.utils import get_object
    
    entries = {}
    
    def read_tree_internal(sha, prefix=""):
        data = get_object(sha)
        if not data.startswith(b'tree '):
            raise ValueError(f"Object {sha} is not a tree")
        
        # Skip header
        null_pos = data.find(b'\x00')
        if null_pos == -1:
            raise ValueError(f"Invalid tree object {sha}")
        
        tree_data = data[null_pos + 1:]
        
        # Parse tree entries
        pos = 0
        while pos < len(tree_data):
            # Find space after mode
            space_pos = tree_data.find(b' ', pos)
            if space_pos == -1:
                break
            
            # Find null byte after name
            null_pos = tree_data.find(b'\x00', space_pos)
            if null_pos == -1:
                break
            
            mode = tree_data[pos:space_pos].decode()
            name = tree_data[space_pos + 1:null_pos].decode()
            sha = tree_data[null_pos + 1:null_pos + 21].hex()
            
            full_path = os.path.join(prefix, name) if prefix else name
            
            if mode.startswith('100'):  # blob
                entries[full_path] = sha
            elif mode.startswith('400'):  # tree
                read_tree_internal(sha, full_path)
            
            pos = null_pos + 21
    
    read_tree_internal(tree_sha)
    return entries
