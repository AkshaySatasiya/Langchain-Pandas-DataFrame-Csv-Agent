import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent,create_csv_agent
import pandas as pd


# Ad your Credentials here 
# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR API KEY"

# Read CSV files into pandas DataFrames
df1 = pd.read_csv(r"YOUR DATASET PATH")
df2 = pd.read_csv(r"YOUR DATASET PATH")
df3 = pd.read_csv(r"YOUR DATASET PATH")


# Create an agent to work with the CSV data sources
agent1 = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo-1106"),
    [df1,df2,df3],
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# Streamlit app
def main():
    st.title("Universal Chatbot: Pandas DataFrame")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    user_query = st.chat_input("Enter your query:")

    if user_query:
        # Displaying the User Message
        with st.chat_message("user"):
            st.markdown(user_query)

        # Process the user's query
        response = agent1.run(user_query)

        # Displaying and Storing the Assistant Message
        with st.chat_message("assistant"):
            st.markdown(response)

        # Storing Messages
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()