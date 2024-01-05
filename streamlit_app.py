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
import pandas as pd
from PIL import Image

# Données d'exemple (remplacez-les par vos propres données)
data = {
    'Équipe': ['Équipe A', 'Équipe B', 'Équipe C', 'Équipe D'],
    'Résultat (%)': [75, 89, 92, 68],
}

# Créer un DataFrame Pandas
df = pd.DataFrame(data)

# Charger les images
image_paths = ['Images/mario.png', 'Images/luigi.png', 'Images/luigi.png', 'Images/luigi.png']
images = [Image.open(image_path) for image_path in image_paths]

# Ajouter les images au DataFrame
df['Image'] = images

# Tri du DataFrame par classement
df = df.sort_values(by='Résultat (%)', ascending=False).reset_index(drop=True)

# Titre de l'application
st.title("Classement des équipes")

# Afficher le tableau avec les images, noms d'équipe, résultats en pourcentage et classement
st.table(df[['Image', 'Équipe', 'Résultat (%)']])

# Vous pouvez également afficher le classement sous forme de texte
#st.subheader("Classement:")
#for i, row in df.iterrows():
#        st.write(f"{i + 1}. {row['Équipe']} - {row['Résultat (%)]}%")}


# Ajouter d'autres fonctionnalités selon les besoins (graphiques, widgets, etc.)




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

