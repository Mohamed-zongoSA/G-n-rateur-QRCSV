# QRCSV-Generator
QRCSV-Generator est un script Python permettant de générer automatiquement des QR codes à partir d'un fichier CSV. Il extrait des informations spécifiques sur des étudiants et les encode sous forme de QR codes, en ajoutant un filigrane personnalisé ("BIT").

## Description
QRCSV-Generator est un outil permettant de générer des QR codes à partir d'un fichier CSV contenant des informations sur des étudiants. Chaque QR code encode les informations essentielles et inclut un filigrane personnalisé ("BIT").  

## Fonctionnalités
- Lecture des données depuis un fichier CSV (`infos.csv`).
- Génération de QR codes avec des informations détaillées (ID, Nom, Prénom, Genre, etc.).
- Ajout automatique d'un filigrane ("BIT") en couleur dégradée.
- Sauvegarde des QR codes dans un dossier `qr_students`.

## Prérequis
Assurez-vous d'avoir installé Python et les dépendances nécessaires avant d'exécuter le script.

### **Installation des dépendances**
Exécutez la commande suivante pour installer les bibliothèques requises :

```bash
pip install qrcode[pil]
```
### **Execution**
Placez votre fichier CSV ( infos.csv) dans le même dossier que le script.
Exécutez le script Python :

```bash
python qr_bit.py
```

### **Format du fichier CSV**
Le fichier infos.csv doit contenir les colonnes suivantes :

```bash
ID;Last Name;First name ;Gender;Birth date and place;Department;In emergency

ID: 12345
Last Name: Doe
First Name: John
Gender: Male
Birth: 01/01/2000, City
Department: Computer Science
Emergency: +226 XXXXXXXX

```
### **Problèmes fréquents**
- Erreur sur les colonnes : Vérifiez que votre CSV respecte exactement le format attendu.
- Police de caractère non trouvée : Assurez-vous que arial.ttfest disponible, sinon le script utilisera une police par défaut.
- QR code non généré : Assurez-vous que le dossier qr_studentsest bien créé et que les données sont bien présentes dans le CSV.

