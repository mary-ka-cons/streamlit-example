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
    # Titre de l'application
    st.title("Comparaison des résultats des équipes")

    # Données des équipes
    equipe_a = {'Nom': 'Équipe A', 'Résultat (%)': 20}
    equipe_b = {'Nom': 'Équipe B', 'Résultat (%)': 40}

    # Affichage des équipes dans Streamlit
    afficher_equipe(equipe_a)
    afficher_equipe(equipe_b)

def afficher_equipe(equipe):
    # Stylisation du texte en bleu et en gras
    resultat_stylise = f"<span style='color: blue; font-weight: bold;'>{equipe['Résultat (%)']}%</span>"
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

