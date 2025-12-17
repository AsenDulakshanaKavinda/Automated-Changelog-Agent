
from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException

from src.changelog_agent.release_service import release_manager


def run_release_manager(summarized_commits):

    """
    Create a release note using summerize commits

    """


    if not summarized_commits:
        log.error("No summarized commits found, run_summarize")
        return []

    try:
        log.info(f"Running release manager on preprocess_summarized_commits")
        results = release_manager(summarized_commits)
        return results
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'run_release_manager',
                "message": "An error occurred",
            }
        )






