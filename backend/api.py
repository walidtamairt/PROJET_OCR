from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

# 🔹 Charger le fichier .env
load_dotenv()

# 🔹 Récupérer la clé Azure depuis l'environnement
AZURE_KEY = os.getenv("AZURE_KEY")
AZURE_ENDPOINT = "https://evision.cognitiveservices.azure.com/"

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    if not AZURE_KEY:
        return {"error": "Azure key is not set in environment variables"}

    content = await file.read()

    url = AZURE_ENDPOINT + "vision/v3.2/ocr"

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(url, headers=headers, data=content)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()

    # 🔹 Extraire le texte
    extracted_text = ""
    if "regions" in data:
        for region in data["regions"]:
            for line in region["lines"]:
                for word in line["words"]:
                    extracted_text += word["text"] + " "
                extracted_text += "\n"

    # 🔹 Récupérer la langue (si disponible)
    language = data.get("language", "unknown")

    return {
        "text": extracted_text,
        "language": language
    }