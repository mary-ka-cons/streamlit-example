

import streamlit as st
import os

def main():
    st.title("Escape Game - Plateforme de Partage de Fichiers et Codes Secrets")

    # Section pour télécharger des fichiers
    st.header("Télécharger des Fichiers")
    uploaded_files = st.file_uploader("Choisissez un fichier", type=["txt", "pdf", "png", "jpg"], key="file_uploader")

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            save_uploaded_file(uploaded_file)

    # Section pour proposer un code secret
    st.header("Proposer un Code Secret")

    code_secret = st.text_input("Entrez le code secret:")
    st.warning("Assurez-vous de ne partager le code qu'avec les joueurs autorisés.")

    if st.button("Valider le Code Secret"):
        validate_secret_code(code_secret)

def save_uploaded_file(uploaded_file):
    file_path = os.path.join("downloads", uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())
    st.success(f"Fichier téléchargé avec succès: {uploaded_file.name}")

def validate_secret_code(code_secret):
    # Ici, vous pouvez implémenter la logique pour valider le code secret
    # par exemple, le comparer à un code prédéfini ou le stocker pour une vérification ultérieure
    st.success("Code secret validé avec succès!")

if __name__ == "__main__":
    main()






































################## OLD ##################


######pip install streamlit-aggrid
#####
#####
######## Packages
######import altair as alt
######import numpy as np
######import pandas as pd
######import streamlit as st
######from PIL import Image
######from st_aggrid import AgGrid
#####
#####
####### Test ChatGPT
#####
#####import streamlit as st
#####import matplotlib.pyplot as plt
#####import numpy as np
#####
#####def main():
#####    # Définir le fond de l'application en gris foncé
#####    st.markdown(
#####        """
#####        <style>
#####            .stApp {
#####                background-color: #1B1E37;
#####            }
#####        </style>
#####        """,
#####        unsafe_allow_html=True
#####    )
#####
#####    # Titre de l'application
#####    st.title("Comparaison des résultats des équipes")
#####    
#####
#####    # Données des équipes
#####    equipes = [
#####        {'Nom': 'Équipe A', 'Résultat (%)': 20},
#####        {'Nom': 'Équipe B', 'Résultat (%)': 10},
#####    ]
#####
#####    # Trier les équipes en fonction du résultat
#####    equipes_triees = sorted(equipes, key=lambda x: x['Résultat (%)'], reverse=True)
#####
#####    # Affichage des équipes dans Streamlit
#####    for equipe in equipes_triees:
#####        afficher_equipe(equipe)
#####
#####def afficher_equipe(equipe):
#####    # Créer un dégradé de couleur en fonction du résultat
#####    couleur_hex = generer_couleur_degrade(equipe['Résultat (%)'])
#####
#####    # Stylisation du texte avec fond de couleur en dégradé
#####    resultat_stylise = f"<span style='background: linear-gradient(to right, #1B1E37 0%, {couleur_hex} 100%); color: white; font-weight: bold;'>{equipe['Résultat (%)']}%</span>"
#####    st.write(f"**{equipe['Nom']}** - Résultat : {resultat_stylise}", unsafe_allow_html=True)
#####
#####def generer_couleur_degrade(percentage):
#####    # Générer une couleur en dégradé en fonction du pourcentage
#####    cmap = plt.cm.RdYlBu  # Choisissez la colormap que vous préférez
#####    norm = plt.Normalize(0, 100)
#####    couleur_rgb = cmap(norm(percentage))
#####
#####    # Convertir la couleur RGB en format hexadécimal
#####    couleur_hex = "#{:02x}{:02x}{:02x}".format(
#####        int(couleur_rgb[0] * 255),
#####        int(couleur_rgb[1] * 255),
#####        int(couleur_rgb[2] * 255)
#####    )
#####
#####    return couleur_hex
#####
#####if __name__ == "__main__":
#####    main()
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
####### test 2
#####
######## Images
######img = ["Images/mario.png", "Images/luigi.png"]
######
######for i in range(len(img)):
######    st.image(img[i])
######
#####
####### test 1
#####
######## Set-Up Streamlit
################ Set the tab name
######st.set_page_config(
######    page_title="Contest",
######    page_icon="🧿",
######
######)
######
######
################# Set the page title
######st.title("Live Results")
######
################# Build the app
######df = pd.DataFrame(
######    {
######        "Team name": ["Roadmap", "Extras"],
######        "Score": [1,2],
######        "Logo":["Images/mario.png", "Images/luigi.png"]
######    }
######)
######
######AgGrid(df)
#####
#####