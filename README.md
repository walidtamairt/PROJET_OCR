📄 DocScan – IA & Extraction OCR (MCP Protocol)

DocScan est une application d’extraction de texte (OCR) basée sur l’IA, exploitant les services cognitifs de Microsoft Azure.
Le projet démontre l’intégration d’un workflow moderne d’IA générative en exposant ses fonctionnalités via le Model Context Protocol (MCP), permettant à des agents IA (Claude, Copilot) de piloter l’application de manière autonome.

✨ Fonctionnalités

🖼️ OCR Avancé
Extraction de texte à partir d’images ou de documents via Azure Vision.

🌐 Interface Web Moderne
Frontend épuré avec design Glassmorphism pour une expérience fluide.

🤖 Agentic AI Ready (MCP)
Exposition des fonctionnalités OCR pour des agents IA autonomes.

🧩 Architecture Modulaire
Séparation claire entre :

moteur OCR

API Web

serveur MCP (agents IA)

🏗️ Structure du Projet
PROJET_OCR_VERS2/
├── backend/
│   ├── api.py           # Serveur FastAPI (Interface Web)
│   ├── mcp_server.py    # Serveur MCP (Interface Agents IA)
│   ├── ocr_logic.py     # Cœur métier (Appels Azure Vision)
│   └── .env             # Configuration (Clés API - Ignoré par Git)
├── frontend/
│   ├── index.html       # Interface utilisateur HTML5
│   ├── style.css        # Design moderne & Responsive
│   └── script.js        # Logique de communication Frontend
└── README.md

⚙️ Installation
1️⃣ Cloner le dépôt
git clone https://github.com/walidtamairt/PROJET_OCR.git
cd PROJET_OCR

2️⃣ Installer les dépendances
pip install -r backend/requirements.txt

3️⃣ Configurer les variables d’environnement

Créer un fichier .env dans backend/ :

AZURE_KEY=VOTRE_CLE_API
AZURE_ENDPOINT=https://votre_ressource.cognitiveservices.azure.com/

🚀 Utilisation
🧑‍💻 Mode Web (Utilisateur Humain)

Lancer l’API backend :

uvicorn backend.api:app --reload


Puis ouvrir le fichier :

frontend/index.html


Importer un document ou une image pour lancer l’OCR.

🤖 Mode Agent (Assistant IA – MCP)

Lancer le serveur MCP via l’inspecteur :

npx @modelcontextprotocol/inspector python backend/mcp_server.py


Fonctionnalités exposées :

🔧 Tools

analyze_document_url → OCR via URL

📦 Resources

config://info → état du service

🧠 Prompts

Modèles pour transcription et synthèse automatique

🧠 Compétences & Expertise IA

IA Générative

Workflows LLM

Prompt engineering

Orchestration agentique

Interopérabilité IA

Implémentation du protocole MCP

Exposition d’outils IA aux agents autonomes

Backend Engineering

API REST avec FastAPI

Intégration de services cloud Azure

Architecture Logicielle

Découplage logique métier / transport

Approche modulaire scalable

📌 Roadmap (Idées d’évolution)

 Upload de PDF multi-pages

 OCR multilingue

 Historique des extractions

 Export PDF / JSON / Markdown

 Authentification utilisateur

 Mode batch pour agents IA
