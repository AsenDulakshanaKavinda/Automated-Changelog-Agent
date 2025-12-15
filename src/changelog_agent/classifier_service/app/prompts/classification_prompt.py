
from langchain_core.prompts import ChatPromptTemplate
from src.changelog_agent.classifier_service.app.schemas.parser import classification_parser

classifier_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior software release engineer.

Your task is to classify Git commits for changelog generation.

Classification rules:
- feature: new user-facing functionality
- fix: bug fixes
- chore: maintenance, tooling, CI
- docs: documentation-only changes
- refactor: restructuring without behavior change

Breaking change rules:
- API removal or rename
- Database schema changes
- Behavior changes requiring user action

You MUST return output that strictly follows the provided schema.
Do NOT add explanations or extra text.
"""
        ),
        (
            "human",
            """
Commit SHA: {commit_sha}
Commit message: {message}
Files changed: {files_changed}

Classify this commit.

{format_instructions}
"""
        )
    ]
).partial(
    format_instructions=classification_parser.get_format_instructions()
)

