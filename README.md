#  Data Cleaning Automation Tool with Generative AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Gemini_API-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

A generative AI-powered tool that automates data cleaning tasks by dynamically generating and executing Python code based on natural language input.

## 📊 Project Overview

This project leverages Google's Gemini API to create a data cleaning automation tool that simplifies the process of preparing and cleaning datasets. Users can describe their data cleaning requirements in natural language, and the tool automatically generates and executes the corresponding Python code. The tool is designed to streamline data processing tasks, reduce manual effort, and improve the efficiency and accuracy of data pipelines.

### 🎯 Key Features
- **Natural Language Processing**: Users can describe data cleaning tasks in plain English.
- **Automated Code Generation**: The tool dynamically generates Python code based on user input.
- **Streamlit Web Interface**: A user-friendly interface for uploading CSV files, describing tasks, and viewing results.
- **Integration with Gemini API**: Utilizes Google's LLM to interpret user input and generate accurate code.
- **Data Cleaning Automation**: Reduces manual effort and improves efficiency in data pipelines.

## 🧠 Technical Implementation

### Files
- `sentient.py` - Main script for the data cleaning automation tool.
- `requirements.txt` - List of dependencies for the project.
- `example_data.csv` - Sample dataset for testing the tool.

### Data Flow
1. **User Input**: The user uploads a CSV file and describes the data cleaning task in natural language.
2. **Code Generation**: The Gemini API interprets the user's input and generates the corresponding Python code.
3. **Code Execution**: The generated code is executed on the uploaded dataset.
4. **Result Display**: The cleaned dataset is displayed to the user via the Streamlit interface.

## 🚀 Getting Started

## Setup Instructions

### Prerequisites
- Python 3.7+
- Pandas
- Streamlit
- Large Language Models
- Required Python packages (install via pip):

### Install required packages
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
```bash
streamlit run sentient.py
```

### Future Enhancements

#Advanced Features

Customizable Data Cleaning Pipelines: Allow users to save and reuse data cleaning workflows.

Integration with Cloud Storage: Enable users to directly import datasets from cloud storage services like Google Drive or AWS S3.

Error Handling and Suggestions: Improve the tool's ability to handle ambiguous or incomplete user input by providing suggestions and error messages.

Support for Multiple Data Formats: Extend the tool to support other data formats such as Excel, JSON, and SQL databases.

#calability and Performance

Distributed Processing: Implement distributed data processing using Apache Spark for handling large datasets.

Real-time Collaboration: Allow multiple users to collaborate on data cleaning tasks in real-time.

Performance Optimization: Optimize the tool for faster code generation and execution, especially for large datasets.

User Experience Enhancements
Interactive Data Visualization: Integrate interactive data visualization tools like Plotly or Altair for better data exploration.

User Feedback Loop: Implement a feedback mechanism to improve the tool's accuracy and usability based on user input.

Tutorials and Documentation: Provide comprehensive tutorials and documentation to help users get started with the tool.

## License
MIT License

## Contact
For questions or collaboration opportunities, please reach out to:

Email: sriram.vivek@stonybrook.edu
LinkedIn: https://www.linkedin.com/in/sriram-vivek-58a673269/

