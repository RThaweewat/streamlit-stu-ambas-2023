import streamlit as st
import pandas as pd

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


edited_df = st.experimental_data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown("You can download edited file from download button below (CSV)")

df_csv = convert_df(edited_df)

st.download_button(
    label="Download edited data as CSV",
    data=df_csv,
    file_name='edited_data.csv',
    mime='text/csv',
)