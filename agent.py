from langchain_openai.chat_models import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

model = ChatOpenAI(model="gpt-4-turbo", streaming=True)

tools = [TavilySearchResults(max_results=2)]

agent = create_react_agent(model, tools)