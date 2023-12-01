### Packages
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

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
st.dataframe(
    df,
    column_config={
        "Score": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        #"Logo": st.column_config.ImageColumn(width = "large")
        "Logo": st.image(["Images/mario.png", "Images/luigi.png"])
    },
    hide_index=True,
)
