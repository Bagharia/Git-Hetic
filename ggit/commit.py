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
    
