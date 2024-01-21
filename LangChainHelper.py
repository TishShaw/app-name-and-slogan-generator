from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI()
def generate_app_name_and_slogan(app_type):
    # Chain1: App Name
    prompt_template_name = PromptTemplate(
        input_variables=['app_type'],
        template="I am creating a new {app_type} app. Suggest a catchy name for this app."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="app_name")

    # Chain 2: Slogan
    prompt_template_slogan = PromptTemplate(
        input_variables=['app_name'],
        template="Create a memorable slogan for the {app_name} app. "
    )

    slogan_chain = LLMChain(llm=llm, prompt=prompt_template_slogan, output_key="slogan")

    chain = SequentialChain(
        chains=[name_chain, slogan_chain],
        input_variables=['app_type'],
        output_variables=['app_name', 'slogan']
    )

    response = chain({'app_type': app_type})

    return response

if __name__ == '__main__':
    app_type = "Productivity"
    result = generate_app_name_and_slogan(app_type)
    print(f"App Name: {result['app_name'].strip()}")
    print(f"Slogan: {result['slogan'].strip()}")