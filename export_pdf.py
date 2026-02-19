"""
Génère un export PDF du deck de slides interactif.
Usage: python export_pdf.py
"""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent.resolve()
HTML_FILE = HERE / "index.html"
PDF_OUT   = HERE / "test-reco-PDP-DE.pdf"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        # Charger le fichier HTML local
        page.goto(HTML_FILE.as_uri(), wait_until="networkidle")

        # Attendre le chargement des fonts Google
        page.wait_for_timeout(2000)

        # Générer le PDF en mode impression (print CSS actif)
        page.pdf(
            path=str(PDF_OUT),
            width="1280px",
            height="720px",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )

        browser.close()

    print(f"✅ PDF généré : {PDF_OUT}")
    print(f"   Taille : {PDF_OUT.stat().st_size // 1024} Ko")

if __name__ == "__main__":
    main()
