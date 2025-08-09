from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.logger import PromptLoggingCallbackHandler

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", callbacks=[PromptLoggingCallbackHandler()])


def get_llm():
    return llm
