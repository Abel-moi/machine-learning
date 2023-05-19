import requests
import streamlit as st
from streamlit_lottie import st_lottie

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
    
    # Logo, titre et description
    st.image("Logo.png", width=200)
    st.title('PlateSmart')
    st.subheader('IA de reconnaissance de plaques d\'immatriculation')

    st.write("Pour le projet de DeepLearning, nous avons décidé de faire un projet qui peut nous aider dans nos mémoires de fin d'études. Le sujet choisit est un projet ayant pour but de faire une IA qui reconnait et lit le contenu des photographie / images des plaques d\'immatriculation de véhicules. Ce projet nous permet donc d'introduire une IA pouvant reconnaitre un certain type d'objets (les plaques) puis d'extraires un contenu (le contenu des plaques)")
    
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
    
    col1, col2 = st.columns([1,3])
    
    with col1:
        lottie= load_lottie("https://assets9.lottiefiles.com/packages/lf20_G6Lxp3nm1p.json")
        st_lottie(lottie, height = 250, key = "coding")
    # ajouter le code pour l'analyse de données
    
    with col2:
        st.subheader('Fonctionnement')
        st.write("Le but de l'application étant de reconnaitre et lire des plaques d'immatriculation de véhicules, il parait évident que le bot se doit de savoir ce qu'est une plaque. Pour ce faire, il a du s'entrainer de nombreux cycle (INSERER LE PROCEDE DE L'ENTRAINEMENT DU BOT). Apres avoir repérer la plaque, il doit maintenant extraire le contenu de cette derniere, à savoir les caracteres et les chiffres figurant dessus. Enfin il les notes et les affiches pour que l'on puisse bien vérifier s'il n'y a pas eu d'erreur lors du traitement de la plaque.")
    
    st.subheader('Demonstration')
    

    
    
    
    
    
    
    
    
    
    
    
    
