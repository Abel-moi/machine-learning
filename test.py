import requests
import streamlit as st
from streamlit_lottie import st_lottie

########################################################### AVOIR INSTALLE STREAMLIT_LOTTIE ET REQUEST AVE LES COMMANDES PIP ##########################################################################

# Mise en page
st.set_page_config(
    page_title="Page d'accueil",
    page_icon="🌐",
    layout="wide",
)

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Navigation
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Aller à", ['Page d\'accueil', 'Application Web'])

# Page d'accueil
if selection == 'Page d\'accueil':
    # Intégration du CSS
    st.markdown("""
    <style>
    body {
        color: #fff;
        background-image: url("https://www.example.com/your-background-image.jpg");
        background-repeat: no-repeat;
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Logo, titre et description
    st.image("Logo.png", width=200)
    st.title('PlateSmart')
    st.subheader('IA de reconnaissance de plaques d\'immatriculation')

    st.write("Pour le projet de DeepLearning, nous avons décidé de faire un projet qui peut nous aider dans nos mémoires de fin d'études. La reconnaissance de plaques d\'immatriculation nous permet de faire de l'analyse d'image afin de reperer les plaques puis de lire leur contenu.")
    
    lottie = load_lottie("https://assets5.lottiefiles.com/packages/lf20_it6c3dgk.json")
    st_lottie(lottie, height = 250, key = "coding")
    
    st.markdown("<h2 style ='text-align : center;'> By Abel, Canelle, Cedric, Markclay </h2>", unsafe_allow_html = True)

    
    # TRAIT DE SECTION
    #st.markdown("""
    #---

    #""", unsafe_allow_html=True)

# Page d'analyse de données
elif selection == 'Application Web':
    st.title('Page de l\'application Web')
    # ajouter le code pour l'analyse de données
