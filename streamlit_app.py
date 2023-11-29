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
df
