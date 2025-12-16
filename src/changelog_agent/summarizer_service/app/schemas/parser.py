from langchain_core.output_parsers import PydanticOutputParser
from src.changelog_agent.summarizer_service.app.schemas.schema import SummarizerResults

summarizer_parser = PydanticOutputParser(
    pydantic_object=SummarizerResults
)