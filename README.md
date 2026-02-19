# 📄 DocScan — IA & Extraction OCR via MCP Protocol

> Application d'extraction de texte intelligente propulsée par **Azure Vision** et exposée aux agents IA via le **Model Context Protocol (MCP)**.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Azure](https://img.shields.io/badge/Azure-Cognitive%20Services-0078D4?logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-purple)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🧠 Vue d'ensemble

**DocScan** est une application OCR moderne qui permet d'extraire du texte à partir d'images et de documents, en exploitant les services cognitifs de Microsoft Azure.

Ce qui rend DocScan unique : ses fonctionnalités sont exposées via le **Model Context Protocol (MCP)**, permettant à des agents IA comme **Claude** ou **GitHub Copilot** de piloter l'application de manière **totalement autonome**.

```
Image / Document
      │
      ▼
 Azure Vision API  ──►  Texte extrait
      │
      ├──► Interface Web (Humain)
      │
      └──► Serveur MCP (Agent IA autonome)
```

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| 🖼️ **OCR Avancé** | Extraction de texte depuis images ou documents via Azure Vision |
| 🌐 **Interface Web** | Frontend moderne avec design Glassmorphism |
| 🤖 **Agentic AI Ready** | Exposition des fonctionnalités OCR pour agents IA autonomes via MCP |
| 🧩 **Architecture Modulaire** | Séparation claire : moteur OCR · API Web · serveur MCP |

---

## 🏗️ Structure du projet

```
PROJET_OCR/
├── backend/
│   ├── api.py           # 🌐 Serveur FastAPI — Interface Web
│   ├── mcp_server.py    # 🤖 Serveur MCP — Interface Agents IA
│   ├── ocr_logic.py     # 🔍 Cœur métier — Appels Azure Vision
│   └── .env             # 🔐 Configuration (clés API — ignoré par Git)
├── frontend/
│   ├── index.html       # Interface utilisateur HTML5
│   ├── style.css        # Design moderne & responsive
│   └── script.js        # Logique de communication frontend
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/walidtamairt/PROJET_OCR.git
cd PROJET_OCR
```

### 2️⃣ Installer les dépendances

```bash
pip install -r backend/requirements.txt
```

### 3️⃣ Configurer les variables d'environnement

Créer un fichier `.env` dans `backend/` :

```env
AZURE_KEY=VOTRE_CLE_API
AZURE_ENDPOINT=https://votre_ressource.cognitiveservices.azure.com/
```

> 💡 Obtenez vos clés sur le [portail Azure](https://portal.azure.com) en créant une ressource **Computer Vision**.

---

## 🚀 Utilisation

### 🧑‍💻 Mode Web — Interface Humain

Lancer le backend :

```bash
uvicorn backend.api:app --reload
```

Puis ouvrir `frontend/index.html` dans votre navigateur, importer un document ou une image et lancer l'OCR.

---

### 🤖 Mode Agent — Interface IA (MCP)

Lancer le serveur MCP via l'inspecteur :

```bash
npx @modelcontextprotocol/inspector python backend/mcp_server.py
```

**Fonctionnalités exposées aux agents :**

| Type | Nom | Description |
|---|---|---|
| 🔧 Tool | `analyze_document_url` | OCR d'un document via URL |
| 📦 Resource | `config://info` | État et configuration du service |
| 🧠 Prompt | *(modèles inclus)* | Transcription et synthèse automatique |

---

## 🧠 Compétences démontrées

**IA Générative & Agentique**
- Workflows LLM & prompt engineering
- Orchestration agentique via MCP
- Interopérabilité agents IA (Claude, Copilot)

**Backend Engineering**
- API REST avec FastAPI
- Intégration Azure Cognitive Services
- Architecture découplée et modulaire

---

## 📌 Roadmap

- [ ] Upload de PDF multi-pages
- [ ] OCR multilingue
- [ ] Historique des extractions
- [ ] Export PDF / JSON / Markdown
- [ ] Authentification utilisateur
- [ ] Mode batch pour agents IA

---

## 👤 Auteur

**Walid Tamairt** — [GitHub](https://github.com/walidtamairt)

---

*Projet réalisé dans le cadre du Bachelor IA & Data — ECE Paris*
