from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_community.llms import GPT4All
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
# create_tool_calling_agent, AgentExecutor

MODEL_PATH="./models/mistral-7b.Q4_0.gguf"
load_dotenv()

class ResearchResponse(BaseModel):
    topic : str
    summamy : str
    sources : list[str]
    tools_used : list[str]


def main():
    llm = GPT4All(model=MODEL_PATH)
    parser = PydanticOutputParser(pydantic_object=ResearchResponse)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a research assistant that will help generate a research paper.
                Answer the user query and use neccessary tools.
                Wrap the output in this format and provide no other text\n{format_instructions}
                """,
            ),
            ("placeholder","{chat_history}"),
            ("human","{query}"),
            ("placeholder","{agent_scratchpad}"),

        ]
    ).partial(format_instructions=parser.get_format_instructions())

    agent=create_agent(
        model=llm,
        system_prompt=prompt,
        tools=[]
    )

    result =agent.invoke(
        {"messages":[{"role":"user", "content":"¿What is the capital of Spain?"}]}
    )
    print(result)

if __name__ == "__main__":
    main()
