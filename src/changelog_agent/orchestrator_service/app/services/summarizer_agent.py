from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException

from src.changelog_agent.summarizer_service import summarize_classified_commits

def run_summarizer(classified_commits):

    """
    Run summarizer on all classified_commits

    Args:
        classified_commits (list): list of classified_commits
    """

    if not classified_commits:
        log.error("No classified_commits found, run_classifier")
        return []

    try:
        log.info(f"Running summarizer on classified_commits, length of classified_commits: {len(classified_commits)}")
        results = summarize_classified_commits(classified_commits)
        return results
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'run_summarizer',
                "message": "An error occurred",
            }
        )










