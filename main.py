from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from pydantic import BaseModel
import requests
from tools import search_web, search_wikipedia


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

def check_ollama():
    """Check if Ollama is running."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def main():
    if not check_ollama():
        print("❌ Error: Ollama is not running!")
        print("Start it with: ollama serve")
        return
    
    print("✅ Ollama is running")
    
    # Use Ollama locally
    llm = ChatOllama(
        model="mistral",
        timeout=120  
    )
    
    tools_search= [search_web, search_wikipedia]
    agent = create_agent(
        model=llm,
        system_prompt="You are a research assistant. Answer questions thoroughly.",
        tools=tools_search
    )
    
    query= input("¿En que se le puede ayudar? ")
    print("Running agent...")
    result = agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })

    print(result)
    # Obtener el último mensaje (que es el AIMessage)
    content = result['messages'][-1].content
    
    print(f"Respuesta Limpia {content}")
    


if __name__ == "__main__":
    main()