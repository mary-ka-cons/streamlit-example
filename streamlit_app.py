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

    # Stylisation du DataFrame pour masquer l'index et les bordures
    styled_df = df.style.hide_index().set_table_styles([
        {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('border', 'none')]},
        {'selector': 'th, td', 'props': [('border', 'none'), ('padding', '10px'), ('text-align', 'left')]}
    ])

    # Affichage du DataFrame stylisé dans une table
    st.write(styled_df, unsafe_allow_html=True)

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

