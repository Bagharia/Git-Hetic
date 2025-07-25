# 📋 Organisation du Projet Git - Style Trello

##  Vue d'ensemble
**Projet :** Git from Scratch en Python  
**Durée :** 9 jours  
**Équipe :** 4-5 développeurs  
**Objectif :** Réimplémenter les fonctionnalités de base de Git

---

##  BACKLOG (À faire)

###  **Phase 1 : Architecture (J1-J2)**
- [ ] Analyser les spécifications Git
- [ ] Créer la structure des dossiers
- [ ] Définir les interfaces communes
- [ ] Mettre en place le workflow Git d'équipe

###  **Phase 2 : Commandes Plumbing (J3-J4)**
- [ ] `git init` - Initialisation du dépôt
- [ ] `git hash-object` - Création d'objets blob
- [ ] `git cat-file` - Lecture d'objets
- [ ] `git write-tree` - Création d'arbres
- [ ] `git commit-tree` - Création de commits
- [ ] `git ls-tree` - Affichage des arbres
- [ ] `git show-ref` - Affichage des références
- [ ] `git rev-parse` - Résolution de références

###  **Phase 3 : Commandes Porcelain (J5-J6)**
- [ ] `git add` - Ajout à l'index
- [ ] `git rm` - Suppression de fichiers
- [ ] `git commit` - Création de commits
- [ ] `git status` - État du dépôt
- [ ] `git checkout` - Changement de branche
- [ ] `git log` - Historique des commits
- [ ] `git ls-files` - Liste des fichiers indexés

###  **Phase 4 : Tests (J7-J8)**
- [ ] Tests unitaires pour chaque commande
- [ ] Tests d'intégration complets
- [ ] Tests de sécurité
- [ ] Tests de performance

###  **Phase 5 : Documentation (J9)**
- [ ] README complet
- [ ] Documentation technique
- [ ] Guide d'utilisation
- [ ] Documentation d'organisation

---

##  EN COURS

### **Commandes Plumbing (8/8)** 
- [X] `git init` - Initialisation
- [x] `git hash-object` - Objets blob
- [x] `git cat-file` - Lecture objets
- [x] `git write-tree` - Création arbres
- [x] `git commit-tree` - Création commits
- [x] `git ls-tree` - Affichage arbres
- [x] `git show-ref` - Références
- [x] `git rev-parse` - Résolution refs

### **Commandes Porcelain (7/7)** 
- [x] `git add` - Ajout à l'index
- [x] `git rm` - Suppression fichiers
- [x] `git commit` - Création commits
- [x] `git status` - État dépôt
- [x] `git checkout` - Changement branche
- [x] `git log` - Historique
- [x] `git ls-files` - Liste fichiers

### **Tests (3/3)** 
- [x] `test_all_commands.py` - Tests complets
- [x] `test_simple.py` - Tests basiques
- [x] `test_checkout_security.py` - Tests sécurité

### **Documentation (3/3)** 
- [x] `README.md` - Documentation projet
- [x] `github_workflow.md` - Workflow équipe
- [x] `DOCUMENTATION_ORGANISATION.md` - Cette doc

---

##  Workflow Git d'Équipe

### **Branches**
```
main (branche principale)
├── feat/init
├── feat/hash-object
├── feat/add
├── feat/commit
├── feat/checkout
└── feat/status
```

### **Processus**
1. **Créer branche** : `git checkout -b feat/nom-commande`
2. **Développer** : Implémenter la fonctionnalité
3. **Commiter** : `git commit -m "feat: implémentation git nom-commande"`
4. **Pousser** : `git push -u origin feat/nom-commande`
5. **Pull Request** : Créer PR vers main
6. **Code Review** : Validation par un autre membre
7. **Merge** : Fusion après validation

---

##  Répartition des Tâches

| Développeur | Commandes Assignées | Statut |
|-------------|-------------------|---------|
| **Dev 1** | `init`, `hash-object`, `cat-file`, `write-tree` |  Terminé |
| **Dev 2** | `commit-tree`, `ls-tree`, `show-ref`, `rev-parse` |  Terminé |
| **Dev 3** | `add`, `rm`, `ls-files`, `status` |  Terminé |
| **Dev 4** | `commit`, `log`, `checkout` |  Terminé |

---

##  Objectifs Atteints

### **Fonctionnalités** 
- [x] 15 commandes Git implémentées
- [x] Gestion complète de l'index
- [x] Système de commits avec historique
- [x] Gestion des branches et checkout
- [x] Tests automatisés complets

### **Qualité** 
- [x] Architecture modulaire
- [x] Code documenté
- [x] Gestion d'erreurs
- [x] Conformité Git

---

##  Leçons Apprises

### **Organisation**
-  Répartition claire des tâches
-  Communication régulière
-  Code review systématique
-  Tests en continu

### **Technique**
-  Architecture modulaire efficace
-  Interfaces bien définies
-  Workflow Git professionnel
-  Documentation à jour

---

*Projet Git from Scratch - Équipe HETIC - Organisation avec Trello* 