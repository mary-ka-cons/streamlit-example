#pip install streamlit-aggrid


### Packages
#import altair as alt
#import numpy as np
#import pandas as pd
#import streamlit as st
#from PIL import Image
#from st_aggrid import AgGrid


## Test ChatGPT

import streamlit as st

def main():
    # Ajouter une classe CSS pour définir le fond en gris
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #1B1E37;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Titre de l'application
    st.title("Comparaison des résultats des équipes")

    # Données des équipes
    couleur_hex = '#33C8E9'  # Vous pouvez ajuster le code hexadécimal ici
    equipes = [
        {'Nom': 'Équipe A', 'Résultat (%)': 20},
        {'Nom': 'Équipe B', 'Résultat (%)': 10},
    ]

    # Trier les équipes en fonction du résultat
    equipes_triees = sorted(equipes, key=lambda x: x['Résultat (%)'], reverse=True)

    # Affichage des équipes dans Streamlit
    for equipe in equipes_triees:
        afficher_equipe(equipe, couleur_hex)

def afficher_equipe(equipe, couleur_hex):
    # Stylisation du texte en utilisant la couleur hexadécimale
    resultat_stylise = f"<span style='color: {couleur_hex}; font-weight: bold;'>{equipe['Résultat (%)']}%</span>"
    st.write(f"**{equipe['Nom']}** - Résultat : {resultat_stylise}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()












## test 2

### Images
#img = ["Images/mario.png", "Images/luigi.png"]
#
#for i in range(len(img)):
#    st.image(img[i])
#

## test 1

### Set-Up Streamlit
########### Set the tab name
#st.set_page_config(
#    page_title="Contest",
#    page_icon="🧿",
#
#)
#
#
############ Set the page title
#st.title("Live Results")
#
############ Build the app
#df = pd.DataFrame(
#    {
#        "Team name": ["Roadmap", "Extras"],
#        "Score": [1,2],
#        "Logo":["Images/mario.png", "Images/luigi.png"]
#    }
#)
#
#AgGrid(df)

