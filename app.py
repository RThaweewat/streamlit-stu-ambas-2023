import streamlit as st
import pandas as pd
from io import StringIO

@st.cache
def convert_df(dataframe: pd.DataFrame):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return dataframe.to_csv().encode('utf-8')

# Todo list add features: drop dup, drop na, fill na
uploaded_file = st.file_uploader("Choose your CSV file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)


edited_df = st.experimental_data_editor(df)
final_df = convert_df(edited_df)
if final_df is not None:
    st.markdown("You can download edited file from download button below (CSV)")
    st.download_button(
        label="Download edited data as CSV",
        data=final_df,
        file_name='edited_data.csv',
        mime='text/csv',
        )


