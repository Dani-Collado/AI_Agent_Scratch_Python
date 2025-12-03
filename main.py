from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

def main():
    # Use Ollama locally - NO API KEY NEEDED
    llm = ChatOllama(model="mistral")  # or neural-chat, llama2
    
    agent = create_agent(
        model=llm,
        system_prompt="You are a research assistant. Answer questions thoroughly.",
        tools=[],
        response_format=ResearchResponse
    )
    
    result = agent.invoke({
        "messages": [{"role": "user", "content": "What is the capital of Spain?"}]
    })
    
    print(result)

if __name__ == "__main__":
    main()