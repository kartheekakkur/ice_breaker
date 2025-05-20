
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


from langchain_core.tools import Tool
from langchain.agents import (
  create_react_agent,
  AgentExecutor,

)
from tools.tools import get_profile_url

from langchain import hub


def lookup(name: str) -> str:
    """
    This function takes a string as input and returns a LinkedIn profile URL.
    """

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    template = """
    Given the name of a person {name_of_person}, I want you to get me the LinkedIn profile page.
    Your answers should return exactly one LinkedIn url as output as string without quotes.
    """
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"],
        template=template
    )
    tools_for_agent = [
        Tool(
            name="Crawl google for the LinkedIn profile Page",
            func=get_profile_url,
            description="Useful for when you need to get exactly one LinkedIn profile URL for a given name."
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )
    # Invoke the agent executor with the input name
    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})

    
    # Construct the LinkedIn URL
    url = result["output"]
    
    return url

if __name__ == "__main__":
    load_dotenv()
    name = "Akkur"
    linkedin_url = lookup(name)
    print(f"LinkedIn URL for {name}: {linkedin_url}")