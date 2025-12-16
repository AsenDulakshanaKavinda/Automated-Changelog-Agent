from src.changelog_agent.summarizer_service.app.agent.summarizer_agent import summarize_classified_commits
from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException

def run_summarizer(classified_commits):

    """
    Run summarizer on all classified_commits

    Args:
        classified_commits (list): list of classified_commits
    """
    log.info(f'type >>>>>: {type(classified_commits[0])} and length: {len(classified_commits)}')

    if not classified_commits:
        log.error("No classified_commits found, run_classifier")
        return []

    try:
        log.info(f"Running summarizer on classified_commits, len(classified_commits) = {len(classified_commits)}")
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










