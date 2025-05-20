from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.scrape_linkedin_data import scrape_linkedin_profile
from langchain_core.output_parsers import StrOutputParser

from agent.linkedin_lookup_agent import lookup
from dotenv import load_dotenv
from output_parser import Summary,summary_parser
from typing import Any, Tuple



def ice_break_with(name: str) -> Summary:
    """
    This function takes a string as input and returns a LinkedIn profile URL.
    """

    # Get the LinkedIn profile URL using the lookup function
    linkedin_profile_url = lookup(name)

    # Scrape the LinkedIn profile data
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)
    summary_template ='''
    You are a helpful assistant that summarizes the text provided to you.
    Tell me some interesting facts about the about the person in {information}

    use information from LinkedIn.
    \n {format_instructions}
    '''

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()},
    )
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    chain = summary_prompt_template | llm | summary_parser
    result = chain.invoke(input={"information": linkedin_data})
    return result




if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker")
    ice_break_with("Vasudev Kartheek Akkur")
    




