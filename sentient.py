import google.generativeai as genai
import subprocess
import pandas as pd
import streamlit as st

# Configure API key for Generative AI
genai.configure(api_key='AIzaSyCV0BeXHo6Z13s6cP-yrmawF3pX5rhlVlk')


def generate_and_save_code(user_input, csv_file_path):
    try:
        # Load CSV and get basic details
        df = pd.read_csv(csv_file_path)
        num_rows, num_columns = df.shape
        column_names = df.columns.tolist()
        sample_data = df.head(3).to_string()

        # Prepare CSV details for the prompt
        csv_details = (f"The CSV file '{csv_file_path}' has {num_rows} rows and {num_columns} columns. "
                       f"The column names are: {', '.join(column_names)}. "
                       f"Here is a sample of the first 3 rows:\n{sample_data}\n")

        # Model initialization
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Combine CSV details and user input into the prompt
        prompt = (f"Given the following CSV file details:\n{csv_details}\n"
                  f"Please generate Python code that {user_input} "
                  )

        # Request code generation from the model
        response = model.generate_content(prompt)

        # Extract code from the response
        generated_code = response.text
        start_marker = "```python"
        end_marker = "```"
        start_idx = generated_code.find(start_marker) + len(start_marker)
        end_idx = generated_code.find(end_marker, start_idx)
        extracted_code = generated_code[start_idx:end_idx].strip()

        # Display generated code in Streamlit
        #st.write("Generated Code:\n", extracted_code)

        # Save the generated code to a temporary file
        temp_code_file = 'temp_generated_code.py'
        with open(temp_code_file, 'w') as f:
            f.write(extracted_code)

        st.write(f"Generated code saved to {temp_code_file}")
        st.write("Executing the generated code...")

        # Execute the generated code
        result = subprocess.run(['python3', temp_code_file], capture_output=True, text=True)
        st.write(result.stdout)
        st.write(result.stderr)

    except Exception as e:
        st.error(f"An error occurred: {e}")


# Streamlit application
st.title("CSV File Code Generator with Generative AI")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Preview of the uploaded CSV file:")
    st.write(df.head())

    # Get user input for what to do with the CSV file
    user_input = st.text_input("Tell me what to do with the CSV file:")

    # Button to trigger code generation
    if st.button("Generate and Execute Code"):
        # Save uploaded CSV to a temporary file
        csv_file_path = 'uploaded_temp.csv'
        df.to_csv(csv_file_path, index=False)

        # Generate and execute the code
        generate_and_save_code(user_input, csv_file_path)
