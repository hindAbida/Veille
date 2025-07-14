import streamlit as st
import streamlit.components.v1 as components

def show():
    # Charger ton style.css
    with open("assets/prob.css") as f:
        custom_css = f"<style>{f.read()}</style>"

    # HTML + CSS complet
    html_content = f"""
    {custom_css}
    <section data-bs-version="5.1" class="features3 programm5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12">
                    <div class="title-wrapper">
                        <h2 class="mbr-section-title mbr-fonts-style">Les Domaines</h2>
                        <p class="mbr-text mbr-fonts-style">
                            Exploration des liens entre IA, les mathématiques numériques et les villes résilientes.
                        </p>
                    </div>
                </div>

                <!-- Cartes -->
                {generate_card1("🟦 1. Domaine : Intelligence Artificielle et Données")}
                {generate_card2("🟩 2. Domaine : Développement durable – ODD 11")}
                {generate_card3("🟨 3. Domaine : Mathématiques numériques")}
            </div>
        </div>
    </section>
    """

    # Afficher dans la page
    components.html(html_content, height=600, scrolling=True)

# Fonction d’aide pour générer une carte
def generate_card1(title):
    return f"""
    <div class="col-12 col-lg-3 col-md-6 features-without-image item">
        <div class="item-wrapper">
            <div class="title-wrap">
                <div class="title">
                    <span class="mbr-iconfont mobi-mbri-success mobi-mbri"></span>
                    <h3 class="mbr-card-title mbr-fonts-style">{title}</h3>
                </div>
            </div>
            <a class="link-wrap" href="#">
                <p class="mbr-link mbr-fonts-style">Mots Clés : "SDG 11"</br>"ODD 11"</br>"Sustainable Development Goal 11"</br>"resilient cities"</br>"sustainable transport"</br>"urban mobility"</br>"affordable housing"</br>"air quality"</br></p>
            </a>
        </div>
    </div>
    """
def generate_card1(title):
    return f"""
    <div class="col-12 col-lg-3 col-md-6 features-without-image item">
        <div class="item-wrapper">
            <div class="title-wrap">
                <div class="title">
                    <span class="mbr-iconfont mobi-mbri-globe mobi-mbri"></span>
                    <h3 class="mbr-card-title mbr-fonts-style">{title}</h3>
                </div>
            </div>
            <a class="link-wrap" href="#">
                <p class="mbr-link mbr-fonts-style">
                    <strong>Mots Clés :</strong><br>
                    <span>"SDG 11"</span>
                    <span>"ODD 11"</span>
                    <span>"Sustainable Development Goal 11"</span>
                    <span>"resilient cities"</span>
                    <span>"sustainable transport"</span>
                    <span>"urban mobility"</span>
                    <span>"affordable housing"</span>
                    <span>"air quality"</span>
                </p>
            </a>
        </div>
    </div>
    """
def generate_card2(title):
    return f"""
    <div class="col-12 col-lg-3 col-md-6 features-without-image item">
        <div class="item-wrapper">
            <div class="title-wrap">
                <div class="title">
                    <span class="mbr-iconfont mobi-mbri-setting3 mobi-mbri"></span>
                    <h3 class="mbr-card-title mbr-fonts-style">{title}</h3>
                </div>
            </div>
            <a class="link-wrap" href="#">
                <p class="mbr-link mbr-fonts-style">
                    <strong>Mots Clés :</strong><br>
                    <span>"artificial intelligence"</span>
                    <span>"AI"</span>
                    <span>"deep learning"</span>
                    <span>"reinforcement learning"</span>
                    <span>"machine learning"</span>
                    <span>"data science"</span>
                    <span>"data analytics"</span>
                    <span>"open data"</span>
                    <span>"data-driven"</span>
                    <span>"big data"</span>
                    <span>"smart cities"</span>
                    <span>"IoT"</span>
                    <span>"sensors"</span>
                    <span>"edge computing"</span>
                    <span>"digital twin"</span>
                    <span>"cloud computing"</span>
                    <span>"GIS"</span>
                </p>
            </a>
        </div>
    </div>
    """
def generate_card3(title):
    return f"""
    <div class="col-12 col-lg-6 col-md-12 features-without-image item">
        <div class="item-wrapper">
            <div class="title-wrap">
                <div class="title">
                    <span class="mbr-iconfont mobi-mbri-calc mobi-mbri"></span>
                    <h3 class="mbr-card-title mbr-fonts-style">{title}</h3>
                </div>
            </div>
            <div class="link-wrap">
                <p class="mbr-link mbr-fonts-style"><strong>📌 Modélisation et Simulation :</strong><br>
                    <span>"mathematical modeling"</span>
                    <span>"numerical simulation"</span>
                    <span>"urban dynamics models"</span>
                    <span>"finite elements"</span>
                    <span>"partial differential equations"</span>
                    <span>"Monte Carlo simulation"</span>
                </p>

                <p class="mbr-link mbr-fonts-style"><strong>📌 Optimisation et Aide à la Décision :</strong><br>
                    <span>"multi-objective optimization"</span>
                    <span>"linear programming"</span>
                    <span>"stochastic optimization"</span>
                    <span>"decision support systems"</span>
                    <span>"operations research"</span>
                    <span>"fuzzy logic"</span>
                </p>

                <p class="mbr-link mbr-fonts-style"><strong>📌 Statistiques et Indicateurs Urbains :</strong><br>
                    <span>"spatio-temporal analysis"</span>
                    <span>"statistical inference"</span>
                    <span>"regression models"</span>
                    <span>"local governance"</span>
                    <span>"public policy"</span>
                    <span>"citizen engagement"</span>
                    <span>"urban access index"</span>
                    <span>"population density"</span>
                    <span>"pollution metrics"</span>
                </p>
            </div>
        </div>
    </div>
    """


def a_show():
    st.markdown("""
    <div class="section" id="requete">
        <h2>🔎 La requête bibliographique</h2>
        <p>Notre requête combine 3 axes : ODD 11 + IA + méthodes numériques</p>
        <div style="background:#fffbe6; padding:15px; border-left:5px solid orange;">
            "<i>SDG 11" OR "resilient cities" OR "urban mobility"</i> AND <br>
            "<i>artificial intelligence" OR "big data" OR "smart cities"</i> AND <br>
            "<i>mathematical modeling" OR "numerical simulation"</i>"
        </div>
    </div>
    """, unsafe_allow_html=True)