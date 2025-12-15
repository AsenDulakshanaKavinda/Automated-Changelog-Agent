from langchain_core.output_parsers import PydanticOutputParser
from src.changelog_agent.classifier_service.app.schemas.schema import ClassificationResult

classification_parser = PydanticOutputParser(
    pydantic_object=ClassificationResult
)