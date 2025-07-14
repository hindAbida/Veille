import streamlit as st
import os
from pathlib import Path
import base64

def show():
    st.markdown("<h2>📑 Veille Brevet (PDF Visualisation)</h2>", unsafe_allow_html=True)

    base_choice = st.selectbox("📁 Choisir une base :", ["Espacenet", "USPTO", "WIPO"])
    
    base_folder_map = {
        "Espacenet": "data/espacenet",
        "USPTO": "data/uspto",
        "WIPO": "data/wipo"
    }

    folder_path = base_folder_map[base_choice]

    if not os.path.exists(folder_path):
        st.warning("📂 Dossier non trouvé.")
        return

    # Liste les fichiers PDF
    pdf_files = sorted(Path(folder_path).glob("*.pdf"))
    if not pdf_files:
        st.info("Aucun PDF disponible dans ce dossier.")
        return

    selected_pdf = st.selectbox("📄 Choisir un PDF :", [f.name for f in pdf_files])
    pdf_path = os.path.join(folder_path, selected_pdf)

    # Lecture du PDF en tant que binaire
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    # Bouton de téléchargement fiable
    st.download_button(
        label="📥 Télécharger le PDF",
        data=pdf_bytes,
        file_name=selected_pdf,
        mime="application/pdf"
    )

    # (Optionnel) Petit rappel texte
    st.markdown("🔒 *Si le PDF ne s'affiche pas dans votre navigateur, utilisez le bouton ci-dessus pour le télécharger.*")
