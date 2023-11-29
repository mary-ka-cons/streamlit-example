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


d = {'Team name': ['Name 1', 'Name 2'], 'Team logo': ['logourl1', 'logourl2']}
df = pd.DataFrame(data=d)
st.dataframe(df) 

df = pd.DataFrame(
    {
        "Team name": ["Roadmap", "Extras", "Issues"],
        "Score": [1,2,3]
    }
)
st.dataframe(
    df,
    column_config={
        "Score": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        )
    },
    hide_index=True,
)
