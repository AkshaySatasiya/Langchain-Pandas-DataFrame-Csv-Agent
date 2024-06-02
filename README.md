
# Chatting with Datasets for Insights Using Langchain Agents

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/downloads/release)



## About

This project enables chatting with multiple CSV documents to extract insights. It utilizes LangChain's CSV Agent and Pandas DataFrame Agent, alongside OpenAI and Gemini APIs, to facilitate natural language interactions with structured data, aiming to uncover hidden insights through conversational AI.

## Features

- **Natural Language Dataset Interaction**: Chat in human language with Titanic, CarDekho, and Swiggy datasets for intuitive insights.
- **LangChain and Pandas Integration**: Leverage the CSV and DataFrame agents for seamless data handling.
- **OpenAI and Gemini API Utilization**: Use cutting-edge AI models for intelligent data interpretation and response generation.
- **Requirements File**: Includes a `requirements.txt` file for easy environment setup.

## Getting Started

These instructions will guide you through setting up the project on your local machine.

## Configuration 🔧

Before running the application, configure the following environment variables:

- `OPENAI_API_KEY`: Your **OpenAI API Key** for accessing OpenAI models.
- `GEMINI_API_KEY`: Your **Gemini API Key** for accessing Gemini models.

- Provide path of your CSV files into the script.

### Prerequisites

- Python 3.8+ installed on your system.
- Access to OpenAI and Gemini APIs.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourprojectname.git
   ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```


## Project Structure

- `csv_agent.ipynb`: Notebook for interacting with CSV datasets using LangChain.
- `dataframe_agent.ipynb`: Notebook for DataFrame-based dataset interactions using Pandas.
- `gemini.ipynb`: Notebook demonstrating the use of OpenAI and Gemini APIs for conversational insights.
- `requirements.txt`: Lists all project dependencies.

## Acknowledgments

- Thanks to [OpenAI](https://openai.com) and [Gemini](https://gemini.com) for their AI models.
- Appreciation for [LangChain](https://langchain.com) for their conversational AI toolkits.
- Acknowledgment to the creators of the Titanic, CarDekho, and Swiggy datasets for enabling rich conversational data analysis.
