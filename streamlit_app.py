import streamlit as st
import os
import base64

# Définir le code secret global
CODE_SECRET_ATTENDU = "1234"

def main():
    st.markdown(
        "<h1 style='color:#3773A6; font-size:500%; text-align:center ';> Are you ready ?</h1><br>"
        , unsafe_allow_html=True)

    st.markdown(
        "<p style='color:#3773A6; font-size:100%; text-align:center '>Welcome to you detective ! 🕵️ <br> Pour cet escape game vous aurez besoin de télécharger les fichiers laissés à votre disposition. <br> Ceux-ci vous aideront à trouver des codes et des indices vous permettant de trouver un code final à saisir ci-dessous <br> N'oubliez pas que chaque fichier doit être utilisé pour arriver à découvrir le code final ! <br><br><br></p>"
        , unsafe_allow_html=True)

    # Bouton de téléchargement pour les utilisateurs
    st.markdown("<h2 style='color:#A69937; font-size:200%; text-align:left ''>Download Files</h2>", unsafe_allow_html=True)
    if st.button("Download Files"):
        download_files()

    # Section pour proposer un code secret
    st.markdown("<h2 style='text-align: center;'>Proposer un Code Secret</h2>", unsafe_allow_html=True)

    code_secret = st.text_input("Entrez le code secret:")

    if st.button("Valider le Code Secret"):
        validate_secret_code(code_secret)   

def save_uploaded_file(uploaded_file):
    file_path = os.path.join("downloads", uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())
    st.success(f"Fichier téléchargé avec succès: {uploaded_file.name}")

def validate_secret_code(code_secret):
    # Valider le code secret avec le code secret attendu
    if code_secret == CODE_SECRET_ATTENDU:
        st.success("Code secret validé avec succès!")
    else:
        st.error("Code secret incorrect. Veuillez réessayer.")

def download_files():
    files = os.listdir("downloads")
    if not files:
        st.warning("Aucun fichier disponible pour le téléchargement.")
        return

    st.info("Cliquez sur les liens ci-dessous pour télécharger vos fichiers :")
    with st.spinner("Téléchargement en cours..."):
        for file_name in files:
            file_path = os.path.join("downloads", file_name)
            st.markdown(get_binary_file_downloader_html(file_name, file_path), unsafe_allow_html=True)

def get_binary_file_downloader_html(label, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    b64 = base64.b64encode(data).decode()
    custom_html = f'<a href="data:file/txt;base64,{b64}" download="{label}"> {label}</a>'
    return custom_html

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