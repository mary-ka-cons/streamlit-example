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
import pandas as pd

def main():
    # Titre de l'application
    st.title("Comparaison des résultats de deux équipes")

    # Création d'un DataFrame avec les données
    data = {
        'Équipe': ['Équipe 1', 'Équipe 2'],
        'Résultat (%)': [60, 75],
    }
    df = pd.DataFrame(data)

    # Stylisation de la table pour ne pas afficher d'index et de bordures
    st.markdown("""
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: none;
                padding: 10px;
                text-align: left;
            }
        </style>
    """, unsafe_allow_html=True)

    # Affichage des résultats dans une table sans index et sans bordures
    st.table(df.style.hide_index())

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

