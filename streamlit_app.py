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
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
