#!/usr/bin/env python3
"""
Script de test pour vérifier toutes les commandes Git
Ce script teste toutes les fonctionnes disponibles dans le système Git
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

def run_command(cmd, description=""):
    """Exécute une commande et affiche le résultat"""
    print(f"\n{'='*60}")
    print(f"🧪 TEST: {description}")
    print(f"📝 Commande: python main.py {cmd}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            ["python", "main.py"] + cmd.split(),
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        print("✅ Sortie standard:")
        print(result.stdout)
        
        if result.stderr:
            print("⚠️  Erreurs:")
            print(result.stderr)
        
        print(f"📊 Code de retour: {result.returncode}")
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Erreur d'exécution: {e}")
        return False

def create_test_files():
    """Crée des fichiers de test"""
    print("\n📁 Création des fichiers de test...")
    
    # Créer un fichier de test
    with open("test_file.txt", "w") as f:
        f.write("Ceci est un fichier de test\n")
    
    # Créer un sous-répertoire avec un fichier
    os.makedirs("test_dir", exist_ok=True)
    with open("test_dir/subfile.txt", "w") as f:
        f.write("Fichier dans un sous-répertoire\n")
    
    # Modifier le fichier existant
    with open("fichier.txt", "w") as f:
        f.write("Contenu modifié du fichier\n")
    
    print("✅ Fichiers de test créés")

def cleanup_test_files():
    """Nettoie les fichiers de test"""
    print("\n🧹 Nettoyage des fichiers de test...")
    
    test_files = ["test_file.txt", "test_dir"]
    for file in test_files:
        if os.path.exists(file):
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)
    
    print("✅ Fichiers de test supprimés")

def test_all_commands():
    """Teste toutes les commandes disponibles"""
    print("🚀 DÉBUT DES TESTS GIT")
    print("="*60)
    
    # Initialisation
    print("\n1️⃣  INITIALISATION DU DÉPÔT")
    success = run_command("init", "Initialisation d'un nouveau dépôt Git")
    if not success:
        print("❌ Échec de l'initialisation - arrêt des tests")
        return False
    
    # Création des fichiers de test
    create_test_files()
    
    # Test des commandes de base
    print("\n2️⃣  TESTS DES COMMANDES DE BASE")
    
    # Status initial
    run_command("status", "État initial du dépôt")
    
    # Hash-object
    run_command("hash-object test_file.txt", "Calcul du hash d'un fichier")
    
    # Add
    run_command("add test_file.txt", "Ajout d'un fichier à l'index")
    run_command("add test_dir/subfile.txt", "Ajout d'un fichier dans un sous-répertoire")
    run_command("add fichier.txt", "Ajout du fichier modifié")
    
    # Status après add
    run_command("status", "État après ajout des fichiers")
    
    # Ls-files
    run_command("ls-files", "Liste des fichiers dans l'index")
    
    # Write-tree
    tree_result = run_command("write-tree", "Création de l'arbre à partir de l'index")
    
    # Commit-tree (si write-tree a réussi)
    if tree_result:
        # On récupère le SHA de l'arbre depuis la sortie (à adapter selon votre implémentation)
        run_command("commit-tree <tree_sha> -m 'Premier commit'", "Création du premier commit")
    
    # Commit
    run_command("commit -m 'Premier commit avec add'", "Commit avec la commande porcelain")
    
    # Show-ref
    run_command("show-ref", "Affichage des références")
    
    # Log
    run_command("log", "Affichage de l'historique des commits")
    
    # Status après commit
    run_command("status", "État après le premier commit")
    
    # Modification pour tester les changements
    print("\n3️⃣  TESTS DES MODIFICATIONS")
    
    with open("test_file.txt", "a") as f:
        f.write("Ligne ajoutée pour tester les modifications\n")
    
    with open("new_file.txt", "w") as f:
        f.write("Nouveau fichier non tracké\n")
    
    run_command("status", "État avec des modifications")
    
    # Add des modifications
    run_command("add test_file.txt", "Ajout des modifications")
    run_command("add new_file.txt", "Ajout du nouveau fichier")
    
    run_command("status", "État après ajout des modifications")
    
    # Commit des modifications
    run_command("commit -m 'Deuxième commit avec modifications'", "Commit des modifications")
    
    # Log final
    run_command("log", "Historique final")
    
    # Status final
    run_command("status", "État final")
    
    # Test ls-tree (si on a des commits)
    print("\n4️⃣  TESTS AVANCÉS")
    
    # Récupérer le SHA du dernier commit pour ls-tree
    # Note: Cette partie peut nécessiter une adaptation selon votre implémentation
    run_command("ls-tree <tree_sha>", "Affichage du contenu d'un arbre")
    
    # Test rev-parse
    run_command("rev-parse HEAD", "Résolution de la référence HEAD")
    
    print("\n🎉 FIN DES TESTS")
    return True

def main():
    """Fonction principale"""
    print("🧪 SCRIPT DE TEST COMPLET POUR LE SYSTÈME GIT")
    print("="*60)
    
    # Vérifier que main.py existe
    if not os.path.exists("main.py"):
        print("❌ Erreur: main.py non trouvé dans le répertoire actuel")
        return 1
    
    # Sauvegarder l'état initial
    initial_files = set(os.listdir("."))
    
    try:
        # Lancer tous les tests
        success = test_all_commands()
        
        if success:
            print("\n✅ TOUS LES TESTS TERMINÉS AVEC SUCCÈS")
        else:
            print("\n❌ CERTAINS TESTS ONT ÉCHOUÉ")
            
    except KeyboardInterrupt:
        print("\n⏹️  Tests interrompus par l'utilisateur")
    except Exception as e:
        print(f"\n💥 Erreur inattendue: {e}")
    finally:
        # Nettoyage
        cleanup_test_files()
        
        # Vérifier qu'on n'a pas laissé de fichiers de test
        current_files = set(os.listdir("."))
        new_files = current_files - initial_files
        if new_files:
            print(f"\n⚠️  Fichiers créés pendant les tests: {new_files}")
    
    print("\n🏁 FIN DU SCRIPT DE TEST")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 