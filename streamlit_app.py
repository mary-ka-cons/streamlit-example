#pip install streamlit-aggrid


### Packages
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from st_aggrid import AgGrid


### Images
#img = ["Images/mario.png", "Images/luigi.png"]
#
#for i in range(len(img)):
#    st.image(img[i])


### Set-Up Streamlit
########### Set the tab name
st.set_page_config(
    page_title="Contest",
    page_icon="🧿",
)

########### Set the page title
st.title("Live Results")

########### Build the app
df = pd.DataFrame(
    {
        "Team name": ["Roadmap", "Extras"],
        "Score": [1,2],
        "Logo":["Images/mario.png", "Images/luigi.png"]
    }
)

AgGrid(df)

