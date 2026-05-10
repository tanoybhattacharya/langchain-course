from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and public official known for his leadership of Tesla, SpaceX, X, and xAI. Musk has been the wealthiest person in the world since 2025; as of May 2026, Forbes estimates his net worth to be US$788 billion.

    Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A one sentence summary of the person
    2. A list of 5 interesting facts about the person
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(model="gpt-4-0613", temperature=0.7)
    # llm = ChatOllama(model="gemma3:270m", temperature=0.7)

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
