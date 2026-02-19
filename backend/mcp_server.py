from mcp.server.fastmcp import FastMCP
from ocr_logic import perform_ocr

# Initialisation du serveur
mcp = FastMCP("DocScan-Assistant")

# 🛠️ TOOL : Action d'analyse
@mcp.tool()
async def analyze_document_from_url(url: str) -> str:
    """
    Analyse un document via son URL et retourne le texte extrait.
    Idéal pour traiter des factures ou documents trouvés sur le web.
    """
    result = await perform_ocr(image_url=url)
    if "error" in result:
        return f"Échec de l'analyse : {result['error']}"
    return f"Texte extrait :\n{result['text']}\n\nLangue : {result['language']}"

# 🌍 RESOURCE : Exploration des capacités
@mcp.resource("config://info")
def get_service_info() -> str:
    """Fournit des informations sur le statut du service OCR."""
    return "Service DocScan opérationnel utilisant Azure Computer Vision v3.2."

# 🧠 PROMPT : Exemple d'utilisation
@mcp.prompt()
def extract_and_format():
    """Modèle de prompt pour aider l'IA à structurer les résultats."""
    return "Analyse ce document, extrait le texte, puis formate-le proprement en JSON ou Markdown."

if __name__ == "__main__":
    mcp.run()