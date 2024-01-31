import streamlit as st
import os
import base64

# Définir le code secret global
CODE_SECRET_ATTENDU = "1234"

def main():
    st.title("Escape Game - Plateforme de Partage de Fichiers et Codes Secrets")

    # Bouton "Télécharger Fichiers" (jaune)
    if st.button("Télécharger Fichiers"):
        download_files()

    # Bouton "Tester mon code" (violet)
    if st.button("Tester mon code"):
        code_secret = st.text_input("Entrez le code secret :")
        if st.button("Valider"):
            result = validate_secret_code(code_secret)
            st.markdown(result, unsafe_allow_html=True)

def download_files():
    files = os.listdir("downloads")
    if not files:
        st.warning("Aucun fichier disponible pour le téléchargement.")
        return

    st.info("Cliquez sur le lien ci-dessous pour télécharger vos fichiers :")
    with st.spinner("Téléchargement en cours..."):
        for file_name in files:
            file_path = os.path.join("downloads", file_name)
            st.markdown(get_binary_file_downloader_html(file_name, file_path), unsafe_allow_html=True)

def validate_secret_code(code_secret):
    # Valider le code secret avec le code secret attendu
    if code_secret == CODE_SECRET_ATTENDU:
        return "<div style='color: green; text-align: center;'>Bravo ! Vous avez réussi ! 🎉👏</div>"
    else:
        return "<div style='color: red; text-align: center;'>Erreur. Le code secret est incorrect. Veuillez réessayer.</div>"

def get_binary_file_downloader_html(label, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    b64 = base64.b64encode(data).decode()
    custom_html = f'<a href="data:application/octet-stream;base64,{b64}" download="{label}">Télécharger {label}</a>'
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