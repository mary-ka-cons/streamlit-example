import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Contest",
    page_icon="🧿",
)

# dashboard title
st.title("Live Results")

df = pd.DataFrame(
    {
        "Team name": ["Roadmap", "Extras", "Issues"],
        "Score": [1,2,3],
        "Logo":['file:///Users/marie-camillevergez/Documents/PERSO/PROJETS/Tests%20Streamlit/luigi.png',
                'file:///Users/marie-camillevergez/Documents/PERSO/PROJETS/Tests%20Streamlit/luigi.png',
               'file:///Users/marie-camillevergez/Documents/PERSO/PROJETS/Tests%20Streamlit/luigi.png']
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
        "Logo": st.column_config.ImageColumn("Avatar")
    },
    hide_index=True,
)
