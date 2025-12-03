from langchain.agents import create_agent
from langchain_community.llms import GPT4All
from pydantic import BaseModel

MODEL_PATH="./models/mistral-7b.Q4_0.gguf"

class ResearchResponse(BaseModel):
    topic: str
    summary: str  # Fixed typo: was "summamy"
    sources: list[str]
    tools_used: list[str]

def main():
    llm = GPT4All(model=MODEL_PATH)
    
    # Simple string prompt - no ChatPromptTemplate needed
    agent = create_agent(
        model=llm,
        system_prompt="You are a research assistant. Answer questions thoroughly.",
        tools=[],  # Add actual tools here if needed
        response_format=ResearchResponse  # For structured output
    )
    
    # Just pass messages - no need for chat_history placeholder
    result = agent.invoke({
        "messages": [{"role": "user", "content": "What is the capital of Spain?"}]
    })
    
    print(result)

if __name__ == "__main__":
    main()