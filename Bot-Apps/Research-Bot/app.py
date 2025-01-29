import streamlit as st
from phi.assistant import Assistant
from phi.tools.hackernews import HackerNews
from phi.llm.groq import Groq
from phi.model.openai import OpenAIChat

st.title("Multi-Agent AI Researcher 🔍🤖")
st.caption("This app allows you to research top stories and users on HackerNews and generate insightful content.")



groq_api_key = st.text_input("Groq API Key", type="password")

if groq_api_key :
    researcher = Assistant(
        name = "HackerNews Story Researcher",
        role="Researches and analyzes top HackerNews stories, providing detailed insights and trends.",
        tools=[HackerNews()],
    )

    user_researcher = Assistant(
        name="HackerNews User Researcher",
        role="Analyzes HackerNews user profiles, their contributions, and impact on the community.",
        tools=[HackerNews()],
    )

    hn_assistant = Assistant(
        name="HackerNews Insights Team",
        team=[researcher, user_researcher],
        llm= Groq(
            model="mixtral-8x7b-32768",
            max_tokens=2048,
            temperature=0.7,
            api_key=groq_api_key
        ),

        system_prompt=(
            "You are an expert HackerNews analyst team. Your goal is to provide in-depth insights, "
            "trend analysis, and valuable information based on HackerNews data. When responding:"
            "\n1. Always provide context and explain the significance of your findings."
            "\n2. Use data to support your insights whenever possible."
            "\n3. Highlight emerging trends or patterns you observe."
            "\n4. Consider the broader implications of the information for the tech industry or society."
            "\n5. When appropriate, suggest follow-up questions or areas for further exploration."
        )
    )



    query = st.text_area("Enter your research query", height=100)

    if st.button("Generate Insights"):
        if query :
            with st.spinner("Analyzing HackerNews data..."):
                response = hn_assistant.run(query, stream=True)

                st.markdown("## Insights")
                st.write(response)

        else:
            st.warning("Enter a query")
    
else:
    st.warning("Please enter your Groq API key to proceed.")





