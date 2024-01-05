#pip install streamlit-aggrid


### Packages
#import altair as alt
#import numpy as np
#import pandas as pd
#import streamlit as st
#from PIL import Image
#from st_aggrid import AgGrid


## Test ChatGPT
# Importer les bibliothèques nécessaires
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Données d'exemple (remplacez-les par vos propres données)
data = {
    'Équipe': ['Équipe A', 'Équipe B', 'Équipe C', 'Équipe D'],
    'Résultat (%)': [75, 89, 92, 68],
    'Image': ['Images/mario.png', 'Images/mario.png', 'Images/mario.png', 'Images/mario.png'],
}

# Créer un DataFrame Pandas
df = pd.DataFrame(data)

# Tri du DataFrame par classement
df = df.sort_values(by='Résultat (%)', ascending=False).reset_index(drop=True)

# Titre de l'application
st.title("Classement des équipes")

# Configuration de st_aggrid
grid_options = {
    'rowSelection': 'single',
    'rowMultiSelectWithClick': True,
    'onSelectionChanged': 'console.log("selection changed")',
}

# Afficher le tableau avec les images, noms d'équipe, résultats en pourcentage et classement
components.html(
    f'<div id="myGrid" style="height: 400px;">{df.to_html()}</div>',
    height=400,
)

# Vous pouvez également afficher le classement sous forme de texte
st.subheader("Classement:")
for i, row in df.iterrows():
    st.write(f"{i + 1}. {row['Équipe']} - {row['Résultat (%)']}%")





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

