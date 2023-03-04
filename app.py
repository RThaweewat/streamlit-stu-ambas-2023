import streamlit as st
import pandas as pd
from io import StringIO

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


uploaded_file = st.file_uploader("Choose your CSV file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    st.write(df)
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


