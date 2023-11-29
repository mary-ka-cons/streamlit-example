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
        "Logo":['https://i.pinimg.com/originals/7b/47/00/7b47006350fc85297b8a63417eacd0a3.png',
                'https://i.pinimg.com/originals/7b/47/00/7b47006350fc85297b8a63417eacd0a3.png',
               'https://i.pinimg.com/originals/7b/47/00/7b47006350fc85297b8a63417eacd0a3.png']
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
        "Logo": st.column_config.ImageColumn("Logo")
    },
    hide_index=True,
)
