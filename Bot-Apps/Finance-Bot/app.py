import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# pip install phi streamlit groq

from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file
api_key = os.getenv("GROQ_API_KEY")


# Create Web Agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(model="llama3-8b-8192"),
    tools=[DuckDuckGo()],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Create Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(model="llama3-8b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Create Agent Team
agent_team = Agent(
    team=[web_agent, finance_agent],
    name="Agent Team (Web+Finance)",
    model=Groq(model="llama3-8b-8192"),
    show_tool_calls=True,
    markdown=True,
)

# Streamlit UI
st.title("Finance Agent Team")

user_input = st.text_input("Enter your question:")
if st.button("Submit"):
    with st.spinner("Processing..."):
        response = agent_team.run(user_input)
    st.markdown(response)

if __name__ == "__main__":
    st.set_page_config(page_title="Finance Agent Team", page_icon="💼")

# import requests
# import os

# api_key = os.environ.get("GROQ_API_KEY")
# url = "https://api.groq.com/openai/v1/models"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# print(response.json())



print("Web Agent Model:", web_agent.model)