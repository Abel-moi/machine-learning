import streamlit as st

# Mise en page
st.set_page_config(
    page_title="Page d'accueil",
    page_icon="🌐",
    layout="wide",
)

# Navigation
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Aller à", ['Page d\'accueil', 'Analyse de données'])

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
    
    # Graphiques et statistiques
    st.subheader('Quelques statistiques intéressantes')
    #chart_data = pd.DataFrame(
       #np.random.randn(20, 3),
       #columns=['a', 'b', 'c'])

    #st.line_chart(chart_data)

    # Bas de page
    st.markdown("""
    ---

    """, unsafe_allow_html=True)

# Page d'analyse de données
elif selection == 'Analyse de données':
    st.title('Page d\'analyse de données')
    # Ici, vous pouvez ajouter le code pour l'analyse de données
