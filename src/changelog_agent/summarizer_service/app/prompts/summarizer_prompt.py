from langchain_core.prompts import ChatPromptTemplate
from src.changelog_agent.summarizer_service.app.schemas.parser import summarizer_parser

summarizer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system" , """ You are a Summarizer Agent in an automated changelog generation system.

Your responsibility is to convert a single, already-classified git commit into a clear,
concise, and human-readable summary suitable for a software release changelog.

Rules you MUST follow:
- Do NOT invent functionality or changes that are not explicitly stated.
- Do NOT repeat the commit SHA inside the summary text.
- Do NOT mention internal implementation details unless necessary.
- Write summaries in clear, professional English.
- The summary should explain WHAT changed and WHY it matters, not HOW it was implemented.
- Always follow the output format instructions exactly.

Your output will be consumed by automated systems.
Schema compliance is mandatory.
 """
        ),
        (
            "human" , """ Summarize the following commit for inclusion in a release changelog.

Commit SHA:
{commit_sha}

Commit Message:
{message}

Files Changed:
{files_changed}

Generate a concise, meaningful summary that would make sense to:
- developers
- product managers
- release notes readers

{format_instructions}
 """
        )
    ]
).partial(
    format_instructions=summarizer_parser.get_format_instructions()
)

