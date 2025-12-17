from langchain_core.output_parsers import PydanticOutputParser
from src.changelog_agent.release_service.app.schemas.schema import ReleaseManagerOutput

release_manager_parser = PydanticOutputParser(
    pydantic_object=ReleaseManagerOutput
)