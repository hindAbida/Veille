
import streamlit as st
import streamlit.components.v1 as components
import os

def display_html(filename, title=None):
    if title:
        st.markdown(f"#### 📊 {title}")
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            components.html(f.read(), height=450, scrolling=True)
    else:
        st.error(f"Fichier introuvable : {filename}")

# 🔶 Fonction réutilisable pour afficher un graphe HTML avec bordure orange
def render_with_border(path, height=500):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            html_content = f.read()
        bordered_html = f"""
        <div style="border: 3px solid orange; border-radius: 8px; padding: 10px;">
            {html_content}
        </div>
        """
        components.html(bordered_html, height=height, scrolling=True)
    else:
        st.warning(f"❌ Fichier manquant : {os.path.basename(path)}")


def show():
    st.markdown("""
    <div class="section" id="vsc">
        <h2>📚 Veille Scientifique</h2>
        <p>Cette section présente les résultats de notre analyse bibliométrique appliquée aux publications issues de 4 bases : <strong>Scopus, PubMed, Web of Science, IEEE</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

    db_choice = st.selectbox("Choisir une base de données", ["Scopus", "PubMed", "Web of Science", "IEEE"])
    db_dir = db_choice.lower().replace(" ", "")  # ex: "webofscience"

    view_mode = st.radio("Mode d'affichage", ["1D", "2D"], horizontal=True)

    if view_mode == "2D":
        st.markdown(f"### 🔎 Réseaux bibliométriques – {db_choice}")

        file_map = {
            "Réseau sémantique": "Keyword_Keyword.html",
            "Réseau des experts": "Auteur_Auteur.html",
            "Réseau géographique": "Pays_Keyword.html",
            "Réseau géostratégique": "Pays_Pays.html",
            "Co-occurrence auteur/mot-clé": "Auteur_Keyword.html"
        }

        for title, filename in file_map.items():
            st.subheader(f"📌 {title}")
            path = os.path.join("data", db_dir, filename)
            render_with_border(path)

    elif view_mode == "1D":
        st.markdown(f"### 📊 Dashboard Power BI – {db_choice}")

        powerbi_links = {
            "Scopus": "https://app.powerbi.com/reportEmbed?reportId=ae7f28f4-1730-4ed3-a5db-b776361ae0f3&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7&actionBarEnabled=true&reportCopilotInEmbed=true",
            "PubMed": "https://app.powerbi.com/reportEmbed?reportId=37d97e9c-0d45-4e8c-8cad-4348d08a3388&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7&actionBarEnabled=true&reportCopilotInEmbed=true",
            "Web of Science": "https://app.powerbi.com/reportEmbed?reportId=1ffbd18b-8447-4ef1-9f23-b702ad660a94&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7&actionBarEnabled=true&reportCopilotInEmbed=true ",
            "IEEE": "https://app.powerbi.com/reportEmbed?reportId=37d97e9c-0d45-4e8c-8cad-4348d08a3388&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7&actionBarEnabled=true&reportCopilotInEmbed=true"
        }

        if db_choice in powerbi_links:
            iframe_url = powerbi_links[db_choice]
            components.html(f"""
            <iframe title="Dashboard Power BI - {db_choice}" 
                    width="1000" height="700" 
                    src="{iframe_url}" 
                    frameborder="0" allowFullScreen="true"
                    style="border: 3px solid orange; border-radius: 8px; padding: 5px;">
            </iframe>
            """, height=700)
        else:
            st.error("Lien Power BI non défini pour cette base.")



