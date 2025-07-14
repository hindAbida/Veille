import streamlit as st
from sections import intro, problematique, requete, veille_scientifique, veille_brevet, discussion

st.set_page_config(
    page_title="Étude Bibliométrique ODD 11",
    page_icon="images/odd.jpeg",  # Path to your icon
    layout="wide"
)

# --- CSS Custom Tabs ---
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# Navigation logic
section = st.radio("Navigation", [
    "🏠 Accueil",
    "❓ Problématique",
    "🔎 Requête",
    "📚 Veille Scientifique",
    "📄 Veille Brevet",
    "📈 Discussion"
], horizontal=True, label_visibility="collapsed")

# Routing
if section == "🏠 Accueil":
    intro.show()
elif section == "❓ Problématique":
    problematique.show()
elif section == "🔎 Requête":
    requete.show()
elif section == "📚 Veille Scientifique":
    veille_scientifique.show()
elif section == "📄 Veille Brevet":
    veille_brevet.show()
elif section == "📈 Discussion":
    discussion.show()
