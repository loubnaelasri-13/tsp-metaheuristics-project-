# Projet Métaheuristiques pour le Problème du Voyageur de Commerce (TSP)

Ce projet implémente plusieurs **métaheuristiques à solution unique** pour résoudre le problème du voyageur de commerce (TSP), ainsi qu'une approche hybride.

## Algorithmes implémentés

- **Heuristique gloutonne du plus proche voisin (Greedy)**
- **Threshold Accepting**
- **Recuit simulé (Simulated Annealing)**
- **Approche hybride : Recuit simulé + recherche locale 2-opt**

## Instances utilisées

- `instance_29.txt`  
- `instance_51.txt`  

Ces fichiers contiennent les matrices de distances entre les villes pour chaque instance.

## Organisation du dépôt
tsp-metaheuristics-project/
├── data/ # Instances TSP
├── src/ # Code Python pour les algorithmes
├── results/ # Tableaux et figures générés
├── report/ # Rapport LaTeX et PDF
└── README.md # Présentation du projet
## Comment exécuter les expériences

1. Installer les dépendances (Python 3.x) :

```bash
pip install numpy pandas matplotlib

Exécuter le script principal :

python src/experiments.py

Les résultats seront affichés dans la console et sauvegardés dans results/results_table.csv.
Rapport

Le rapport détaillé du projet se trouve dans le dossier report/ (report.tex et report.pdf) et présente :

La description du TSP

Les algorithmes implémentés

L'approche hybride proposée

Les résultats expérimentaux et leur analyse
