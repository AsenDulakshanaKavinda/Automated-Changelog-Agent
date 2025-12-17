from src.changelog_agent.release_service.app.agent.release_manager_agent import release_manager
from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException


def run_release_manager(summarized_commits):


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






