import streamlit as st
import os
from pathlib import Path
import base64  # ✅ Ajout de cet import important

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

    # Lecture du PDF en tant que binaire pour affichage
    with open(pdf_path, "rb") as f:
        base64_pdf = f.read()
        b64 = base64.b64encode(base64_pdf).decode("utf-8")

        # Affichage comme une image scrollable
        pdf_display = f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="800px" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
