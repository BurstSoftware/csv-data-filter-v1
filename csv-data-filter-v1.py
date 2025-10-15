import streamlit as st
import pandas as pd
from io import StringIO

st.title("CSV Data Filter App")

st.write("Upload a .csv file to get started.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # To convert to a string based IO:
    stringio = StringIO(uploaded_data.decode('utf-8'))
    # To read file as string:
    string_data = stringio.read()

    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(StringIO(string_data))

    st.subheader("Original Data - First 10 Rows")
    st.dataframe(df.head(10))

    st.subheader("Filter Columns")
    all_columns = df.columns.tolist()
    columns_to_keep = st.multiselect(
        "Select columns you want to keep:",
        all_columns,
        default=all_columns # All columns are selected by default
    )

    if columns_to_keep:
        filtered_df = df[columns_to_keep]
        st.subheader("Filtered Data - First 10 Rows")
        st.dataframe(filtered_df.head(10))

        # Allow user to download the filtered data
        csv_buffer = StringIO()
        filtered_df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Download Filtered CSV",
            data=csv_buffer.getvalue(),
            file_name="filtered_data.csv",
            mime="text/csv"
        )
    else:
        st.warning("Please select at least one column to filter.")
