#!/usr/bin/env python3
"""
Script de test simple pour le système Git
"""

import os
import sys
import subprocess
import re

def run_cmd(cmd):
    """Exécute une commande et retourne la sortie"""
    try:
        result = subprocess.run(
            ["python", "main.py"] + cmd.split(),
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1

def extract_sha(output):
    """Extrait un SHA de la sortie (40 caractères hexadécimaux)"""
    match = re.search(r'[a-f0-9]{40}', output)
    return match.group(0) if match else None

def test_workflow():
    """Teste un workflow Git complet"""
    print("🧪 Test du workflow Git complet")
    print("="*50)
    
    # 1. Initialisation
    print("\n1. Initialisation...")
    stdout, stderr, code = run_cmd("init")
    print(f"   Sortie: {stdout}")
    if code != 0:
        print(f"   ❌ Erreur: {stderr}")
        return False
    
    # 2. Créer un fichier de test
    print("\n2. Création d'un fichier de test...")
    with open("hello.txt", "w") as f:
        f.write("Hello, Git!\n")
    
    # 3. Status initial
    print("\n3. Status initial...")
    stdout, stderr, code = run_cmd("status")
    print(f"   Sortie:\n{stdout}")
    
    # 4. Hash-object
    print("\n4. Hash-object...")
    stdout, stderr, code = run_cmd("hash-object hello.txt")
    print(f"   Sortie: {stdout}")
    
    # 5. Add
    print("\n5. Add...")
    stdout, stderr, code = run_cmd("add hello.txt")
    print(f"   Sortie: {stdout}")
    
    # 6. Status après add
    print("\n6. Status après add...")
    stdout, stderr, code = run_cmd("status")
    print(f"   Sortie:\n{stdout}")
    
    # 7. Ls-files
    print("\n7. Ls-files...")
    stdout, stderr, code = run_cmd("ls-files")
    print(f"   Sortie:\n{stdout}")
    
    # 8. Write-tree
    print("\n8. Write-tree...")
    stdout, stderr, code = run_cmd("write-tree")
    tree_sha = extract_sha(stdout)
    print(f"   Sortie: {stdout}")
    print(f"   Tree SHA: {tree_sha}")
    
    # 9. Commit-tree
    if tree_sha:
        print(f"\n9. Commit-tree avec SHA: {tree_sha}...")
        stdout, stderr, code = run_cmd(f"commit-tree {tree_sha} -m 'Premier commit'")
        commit_sha = extract_sha(stdout)
        print(f"   Sortie: {stdout}")
        print(f"   Commit SHA: {commit_sha}")
    
    # 10. Commit (porcelain)
    print("\n10. Commit (porcelain)...")
    stdout, stderr, code = run_cmd("commit -m 'Premier commit'")
    print(f"   Sortie: {stdout}")
    
    # 11. Show-ref
    print("\n11. Show-ref...")
    stdout, stderr, code = run_cmd("show-ref")
    print(f"   Sortie:\n{stdout}")
    
    # 12. Log
    print("\n12. Log...")
    stdout, stderr, code = run_cmd("log")
    print(f"   Sortie:\n{stdout}")
    
    # 13. Status final
    print("\n13. Status final...")
    stdout, stderr, code = run_cmd("status")
    print(f"   Sortie:\n{stdout}")
    
    # 14. Ls-tree (si on a un tree SHA)
    if tree_sha:
        print(f"\n14. Ls-tree avec SHA: {tree_sha}...")
        stdout, stderr, code = run_cmd(f"ls-tree {tree_sha}")
        print(f"   Sortie:\n{stdout}")
    
    # 15. Rev-parse
    print("\n15. Rev-parse HEAD...")
    stdout, stderr, code = run_cmd("rev-parse HEAD")
    print(f"   Sortie: {stdout}")
    
    print("\n✅ Test terminé!")
    return True

def cleanup():
    """Nettoie les fichiers de test"""
    test_files = ["hello.txt"]
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"   Supprimé: {file}")

def main():
    print("🚀 Démarrage des tests Git")
    print("="*50)
    
    try:
        success = test_workflow()
        if success:
            print("\n🎉 Tous les tests ont réussi!")
        else:
            print("\n❌ Certains tests ont échoué")
    except KeyboardInterrupt:
        print("\n⏹️  Tests interrompus")
    except Exception as e:
        print(f"\n💥 Erreur: {e}")
    finally:
        print("\n🧹 Nettoyage...")
        cleanup()
    
    print("\n🏁 Fin des tests")

if __name__ == "__main__":
    main() 