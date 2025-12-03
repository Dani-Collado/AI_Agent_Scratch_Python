from langchain.tools import tool
from datetime import datetime
import os

@tool
def search_web(query: str) -> str:
    """Search the web for information using DuckDuckGo.
    
    Args:
        query: The search query string
    """
    try:
        from langchain_community.tools import DuckDuckGoSearchRun
        search = DuckDuckGoSearchRun()
        return search.run(query)
    except Exception as e:
        return f"Error searching web: {str(e)}"

@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for detailed information.
    
    Args:
        query: The search query string
    """
    try:
        from langchain_community.tools import WikipediaQueryRun
        from langchain_community.utilities import WikipediaAPIWrapper
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        return wikipedia.run(query)
    except Exception as e:
        return f"Error searching Wikipedia: {str(e)}"

# @tool
# def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
#     """Saves structured research data to a text file in the 'busquedas' folder.
    
#     Args:
#         data: The research data to save
#         filename: The output filename (default: research_output.txt)
#     """
#     folder = "busquedas"
#     os.makedirs(folder, exist_ok=True)
    
#     filepath = os.path.join(folder, filename)
    
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    
#     try:
#         with open(filepath, "a", encoding="utf-8") as f:
#             f.write(formatted_text)
#         return f"Datos guardados correctamente en {filepath}"
#     except Exception as e:
#         return f"Error al guardar: {str(e)}"