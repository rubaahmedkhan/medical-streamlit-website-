import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Check and print the actual column names for debugging
    st.write("Columns in the uploaded file:")
    st.write(df.columns)

    # Check if required columns are present
    if 'Patient Name' in df.columns or 'Diagnosis' in df.columns:
        st.write("Initial 5 Rows:")
        st.dataframe(df.head(5))

        st.write("Data Summary:")
        st.write(df.describe())

        if st.button("Show Graph"):
            st.write("Generating Bar Graph...")

            # Count the occurrences of each diagnosis
            diagnosis_count = df['Diagnosis'].value_counts()

            # Create the plot (Bar Graph)
            fig, ax = plt.subplots()
            diagnosis_count.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_title("Diagnosis Frequency")
            ax.set_xlabel("Diagnosis")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
    else:
        # Handle case where required columns are missing
        st.error("Missing required columns: 'Patient Name' or 'Diagnosis'. Please upload a valid medical CSV file.")
else:
    # Display error when no file is uploaded
    st.error("Please upload a CSV file.")
