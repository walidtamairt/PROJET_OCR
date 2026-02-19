import os
import httpx
from dotenv import load_dotenv

load_dotenv()

AZURE_KEY = os.getenv("AZURE_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://evision.cognitiveservices.azure.com/")

async def perform_ocr(content: bytes = None, image_url: str = None):
    """Logique partagée pour l'OCR Azure."""
    url = f"{AZURE_ENDPOINT.rstrip('/')}/vision/v3.2/ocr"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/octet-stream" if content else "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        if content:
            response = await client.post(url, headers=headers, content=content)
        else:
            response = await client.post(url, headers=headers, json={"url": image_url})
            
        if response.status_code != 200:
            return {"error": response.text}

        data = response.json()
        extracted_text = ""
        for region in data.get("regions", []):
            for line in region["lines"]:
                extracted_text += " ".join([w["text"] for w in line["words"]]) + "\n"
        
        return {
            "text": extracted_text.strip() or "Aucun texte détecté.",
            "language": data.get("language", "unknown")
        }