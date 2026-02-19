📄 DocScan : Intelligence Artificielle & Extraction OCR (Protocol MCP)
DocScan est une application avancée d'extraction de texte (OCR) exploitant les services cognitifs d'Azure. Ce projet démontre l'intégration d'un workflow d'IA générative moderne en exposant ses fonctionnalités via le Model Context Protocol (MCP), permettant ainsi à des agents IA (Claude, Copilot) de piloter l'application de manière autonome.

🌟 Points Forts
Interface Web Moderne : Frontend épuré avec design "Glassmorphism" pour une expérience utilisateur fluide.

Agentic AI Ready : Premier pas vers les agents autonomes grâce à l'implémentation du standard MCP.

Logique Découplée : Architecture modulaire séparant le moteur OCR de l'interface de transport (Web vs Agent).


🛠️ Installation et Configuration
Cloner le dépôt :

Bash
git clone https://github.com/walidtamairt/PROJET_OCR.git
cd PROJET_OCR
Installer les dépendances :

Bash
pip install -r backend/requirements.txt
Configurer les variables d'environnement :
Créez un fichier .env dans le dossier backend/ :

Plaintext
AZURE_KEY=votre_cle_subscription
AZURE_ENDPOINT=https://votre_ressource.cognitiveservices.azure.com/
🚀 Utilisation
Mode Web (Utilisateur Humain)
Lancez l'API pour alimenter le frontend :

Bash
uvicorn backend.api:app --reload
Accédez ensuite au fichier index.html pour importer vos documents manuellement.

Mode Agent (Assistant IA)
Pour tester l'exposition des outils via l'inspecteur MCP :

Bash
npx @modelcontextprotocol/inspector python backend/mcp_server.py
Tools : analyze_document_url (Extraction de texte via URL).

Resources : config://info (Statut du service).

Prompts : Modèles pour la transcription et la synthèse automatique.

🧠 Expertise IA Acquise
IA Générative : Optimisation de modèles (LLM), ingénierie de prompt et workflows IA.

Interopérabilité : Mise en œuvre du protocole MCP pour l'orchestration d'agents.

Backend Engineering : Création d'APIs robustes avec FastAPI et intégration de services cloud.
