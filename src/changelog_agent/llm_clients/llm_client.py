from langchain_mistralai import ChatMistralAI
import os
from dotenv import load_dotenv

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

load_dotenv()
try:
    llm = ChatMistralAI(
        model_name='mistral-small-latest',
        temperature=0.2
    )
    log.info(f'LLM is ready - mistral')
except Exception as e:
    ProjectException(
        e,
        context={
            'operation': 'mistral-language-model',
            'message': 'error while connecting to ChatMistralAI changelog_agent'
        }
    )