from src.changelog_agent.summarizer_service.app.prompts.summarizer_prompt import summarizer_prompt
from src.changelog_agent.summarizer_service.app.llm_clients.llm_client import llm
from src.changelog_agent.summarizer_service.app.schemas.parser import summarizer_parser
from src.changelog_agent.summarizer_service.app.schemas.schema import SummarizerResults

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

def summarize_classified_commits(classified_commits):
    """
    Read the classified commits and summarize them.

    Args:
        classified commits: list of classified commits
    """

    results = []

    try:
        summarize_chain = (
            summarizer_prompt
            | llm
            | summarizer_parser
        )
        log.info("Summarize chain created.")

        for classified_commit in classified_commits:
            result = summarize_chain.invoke({
                'commit_sha': classified_commit['commit_sha'],
                'message': classified_commit['classification'].message,
                'files_changed': classified_commit['classification'].files_changed,
            })

            results.append({
                'commit_sha': classified_commit['commit_sha'],
                'summarization': result,
            })
            log.info(f'files_changed invoked')
        return results

    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'summarize_classified_commits',
                'message': 'error while summarizing classified commit',
            }
        )














