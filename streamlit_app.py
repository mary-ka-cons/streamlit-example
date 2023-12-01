### Packages
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

### Images
img = list("Images/mario.png", "Images/luigi.png")

for i in len(img):
    st.image(img[i])



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
        "Team name": ["Roadmap", "Extras", "Issues"],
        "Score": [1,2,3],
        "Logo":['https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1ebab919-1015-421b-ac5a-dc53da375adc/dfw9wdm-2613099c-d768-473c-b80a-54b778d403e6.png/v1/fill/w_492,h_507/mario_kart_tour___png_by_jt0328_dfw9wdm-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTA3IiwicGF0aCI6IlwvZlwvMWViYWI5MTktMTAxNS00MjFiLWFjNWEtZGM1M2RhMzc1YWRjXC9kZnc5d2RtLTI2MTMwOTljLWQ3NjgtNDczYy1iODBhLTU0Yjc3OGQ0MDNlNi5wbmciLCJ3aWR0aCI6Ijw9NDkyIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.ssflZUYOdPvvWMEhHXyQlioiznMYSzrqs4jCmJgr-yY',
                'https://github.com/mary-ka-cons/streamlit-example/blob/master/mario.png',
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
        "Logo": st.column_config.ImageColumn(width = "large")
    },
    hide_index=True,
)
