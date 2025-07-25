import os
from ggit.utils import get_object, get_object_type
from ggit.commit import read_tree_recursive

def lire_index():
    """Lit l'index et retourne un dictionnaire {path: sha}"""
    index_path = ".ggit/index"
    if not os.path.exists(index_path):
        return {}
    
    index_entries = {}
    with open(index_path, "r") as f:
        for line in f:
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                sha, path = parts
                index_entries[path] = sha
    return index_entries

def lire_dernier_commit():
    """Lit le dernier commit depuis HEAD et retourne son tree SHA"""
    try:
        with open(".ggit/HEAD", "r") as f:
            ref = f.read().strip()
        
        if ref.startswith("ref: "):
            ref_path = ".ggit/" + ref[5:]
            if os.path.exists(ref_path):
                with open(ref_path, "r") as f:
                    commit_sha = f.read().strip()
            else:
                return None
        else:
            commit_sha = ref
        
        if commit_sha:
            commit_data = get_object(commit_sha)
            lines = commit_data.split(b'\x00')[1].decode().splitlines()
            for line in lines:
                if line.startswith("tree "):
                    return line.split()[1]
    except:
        pass
    return None

def lire_tree_commit(tree_sha):
    """Lit un tree et retourne un dictionnaire {path: sha}"""
    if not tree_sha:
        return {}
    
    try:
        return read_tree_recursive(tree_sha)
    except:
        return {}

def calculer_sha_fichier(path):
    """Calcule le SHA d'un fichier"""
    if not os.path.exists(path):
        return None
    
    with open(path, "rb") as f:
        content = f.read()
    
    from ggit.utils import compute_sha1_and_store
    return compute_sha1_and_store(content, "blob")

def git_status():
    """Affiche l'état du dépôt Git"""
    print("On branch master")
    print()
    
    # Lire l'index (staging area)
    index_entries = lire_index()
    
    # Lire le dernier commit
    dernier_tree_sha = lire_dernier_commit()
    dernier_tree_entries = lire_tree_commit(dernier_tree_sha)
    
    # Fichiers modifiés dans l'index (staged changes)
    staged_modified = []
    staged_added = []
    staged_deleted = []
    
    # Fichiers modifiés dans le working directory (unstaged changes)
    unstaged_modified = []
    unstaged_deleted = []
    unstaged_added = []
    
    # Vérifier les fichiers dans l'index
    for path, index_sha in index_entries.items():
        dernier_sha = dernier_tree_entries.get(path)
        
        if dernier_sha is None:
            # Nouveau fichier dans l'index
            staged_added.append(path)
        elif dernier_sha != index_sha:
            # Fichier modifié dans l'index
            staged_modified.append(path)
        
        # Vérifier si le fichier existe dans le working directory
        if not os.path.exists(path):
            unstaged_deleted.append(path)
        else:
            working_sha = calculer_sha_fichier(path)
            if working_sha != index_sha:
                unstaged_modified.append(path)
    
    # Vérifier les fichiers supprimés de l'index
    for path in dernier_tree_entries:
        if path not in index_entries:
            staged_deleted.append(path)
    
    # Vérifier les nouveaux fichiers non ajoutés
    for root, dirs, files in os.walk("."):
        # Ignorer .ggit et .git
        if ".ggit" in dirs:
            dirs.remove(".ggit")
        if ".git" in dirs:
            dirs.remove(".git")
        
        for file in files:
            path = os.path.join(root, file)[2:]  # Enlever "./"
            if path not in index_entries and path not in dernier_tree_entries:
                unstaged_added.append(path)
    
    # Afficher les résultats
    if staged_added:
        print("Changes to be committed:")
        print("  (use \"git restore --staged <file>\" to unstage)")
        print()
        for path in staged_added:
            print(f"\tnew file:   {path}")
        print()
    
    if staged_modified:
        print("Changes to be committed:")
        print("  (use \"git restore --staged <file>\" to unstage)")
        print()
        for path in staged_modified:
            print(f"\tmodified:   {path}")
        print()
    
    if staged_deleted:
        print("Changes to be committed:")
        print("  (use \"git restore --staged <file>\" to unstage)")
        print()
        for path in staged_deleted:
            print(f"\tdeleted:    {path}")
        print()
    
    if unstaged_modified:
        print("Changes not staged for commit:")
        print("  (use \"git add <file>\" to update what will be committed)")
        print("  (use \"git restore <file>\" to discard changes in working directory)")
        print()
        for path in unstaged_modified:
            print(f"\tmodified:   {path}")
        print()
    
    if unstaged_deleted:
        print("Changes not staged for commit:")
        print("  (use \"git add <file>\" to update what will be committed)")
        print("  (use \"git restore <file>\" to discard changes in working directory)")
        print()
        for path in unstaged_deleted:
            print(f"\tdeleted:    {path}")
        print()
    
    if unstaged_added:
        print("Untracked files:")
        print("  (use \"git add <file>\" to include in what will be committed)")
        print()
        for path in unstaged_added:
            print(f"\t{path}")
        print()
    
    if not any([staged_added, staged_modified, staged_deleted, 
                unstaged_modified, unstaged_deleted, unstaged_added]):
        print("nothing to commit, working tree clean")
