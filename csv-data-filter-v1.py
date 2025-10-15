import streamlit as st
import pandas as pd
from io import StringIO

st.title("CSV Data Filter App")

st.write("Upload a .csv file to get started.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Use uploaded_file directly for pandas to ensure consistency
    # pandas can often read directly from the file_uploader object or its string representation
    
    try:
        # Attempt to decode as UTF-8 first, common for CSVs
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        df = pd.read_csv(stringio)
    except UnicodeDecodeError:
        # If UTF-8 fails, try latin1 or another common encoding
        stringio = StringIO(uploaded_file.getvalue().decode('latin1'))
        df = pd.read_csv(stringio)
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        st.info("Please ensure your CSV is properly formatted and encoded (UTF-8 is recommended).")
        st.stop() # Stop execution if file reading fails

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
