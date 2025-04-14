import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Page configuration
st.set_page_config(page_title="Data Sweeper", layout="wide")

# Custom CSS styling
st.markdown(
    """
    <style>
        .main { background-color: #121212; }
        .block-container {
            padding: 3rem 2rem;
            border-radius: 12px;
            background-color: #1e1e1e;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }
        h1, h2, h3, h4, h5, h6 { color: #66c2ff; }
        .stButton>button {
            border: none;
            border-radius: 8px;
            background-color: #0078D7;
            color: white;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
        }
        .stButton>button:hover { background-color: #005a9e; cursor: pointer; }
        .stDataFrame, .stTable {
            border-radius: 10px;
            overflow: hidden;
        }
        .css-1aumxhk, .css-18e3th9 {
            text-align: left;
            color: white;
        }
        .stRadio>label, .stCheckbox>label { font-weight: bold; color: white; }
        .stDownloadButton>button {
            background-color: #28a745;
            color: white;
        }
        .stDownloadButton>button:hover { background-color: #218838; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Advanced Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

# Upload files
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# Process each file
if uploaded_files:
    for idx, file in enumerate(uploaded_files):
        file_extension = os.path.splitext(file.name)[-1].lower()

        # Load into DataFrame
        if file_extension == ".csv":
            df = pd.read_csv(file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_extension}")
            continue

        st.markdown(f"### 📄 File: `{file.name}`")
        st.write(f"**📏 File Size:** {file.size / 1024:.2f} KB")
        st.write("🔍 Preview of the Uploaded File:")
        st.dataframe(df.head())

        # Cleaning options
        st.subheader("🛠️ Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates from {file.name}", key=f"dup_{idx}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates Removed!")
            with col2:
                if st.button(f"Fill Missing Values for {file.name}", key=f"fillna_{idx}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing numeric values filled!")

        # Column selection
        st.subheader("🎯 Select Columns to Convert")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns, key=f"cols_{idx}")
        if columns:
            df = df[columns]

        # Visualization section
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}", key=f"viz_{idx}"):
            numeric_cols = df.select_dtypes(include='number').columns.tolist()
            if numeric_cols:
                selected_chart_cols = st.multiselect(f"Select numeric columns to visualize ({file.name})", numeric_cols, default=numeric_cols[:2], key=f"chart_{idx}")
                if selected_chart_cols:
                    st.bar_chart(df[selected_chart_cols])
                else:
                    st.warning("Please select at least one numeric column.")
            else:
                st.warning("No numeric columns available to visualize.")

        # File conversion
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=f"conv_{idx}")
        if st.button(f"Convert {file.name}", key=f"convert_btn_{idx}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_extension, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False, engine='openpyxl')
                file_name = file.name.replace(file_extension, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

    # Success message
    st.toast("🎉 All files processed successfully!")
