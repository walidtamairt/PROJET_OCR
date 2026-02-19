# 📄 DocScan

## 🌍 Transformez vos documents en texte avec facilité !

### 📝 Description du projet

DocScan est une application web qui permet d'extraire le texte d’images et de PDF grâce à l’OCR fourni par Microsoft Azure (Azure AI Services).

L’objectif du projet est de fournir une interface simple et intuitive pour :

- Scanner un document
- Visualiser le texte extrait
- Modifier le texte
- Exporter le contenu
- Afficher la langue détectée du document

Le projet est divisé en deux parties :

- 🎨 **Frontend** : interface utilisateur en HTML, CSS et JavaScript  
- ⚙️ **Backend** : API FastAPI qui communique avec le service Azure OCR

### ⚡ Fonctionnalités

- 📤 Importer une image ou un PDF  
- 🔍 Analyser le document (simulation ou réel via Azure OCR)  
- 📄 Visualiser le texte extrait  
- 🌍 Afficher la langue détectée du document  
- ✏️ Modifier le texte directement dans l’interface  
- 📋 Copier le texte  
- 💾 Télécharger le texte en `.txt`

### ⚙️ Installation et utilisation

#### 1️⃣ Cloner le projet

```bash
git clone https://github.com/walidtamairt/PROJET_OCR.git
cd Projet_OCR_vers2
```

## 2️⃣ Préparer le backend

✅ **Prérequis** : Python 3.11 ou supérieur

**Installer les dépendances :**

```bash
cd backend
pip install -r requirements.txt
```

**Créer un fichier .env :**
```bash
AZURE_KEY=VOTRE_CLE_AZURE_ICI
```
**Lancer le serveur FastAPI :**
```bash
uvicorn api:app --reload --port 8000
```

**L’API sera accessible sur :**
```bash
http://127.0.0.1:8000/docs
```

## 3️⃣ Préparer le frontend

**Rester dans le dossier racine du projet.**

**Lancer un serveur local pour tester le frontend :**

```bashcd frontend
python -m http.server 5500
```

**Ouvrir un navigateur et aller sur :**
```bash
http://localhost:5500
```
