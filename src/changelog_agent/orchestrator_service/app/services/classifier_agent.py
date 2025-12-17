from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException

from src.changelog_agent.classifier_service import  classify_commits

def run_classifier(commits):

    """
    Run classifier on all commits

    Args:
        commits (list): list of commits
    """

    if not commits:
        log.error("No commits found, run_classifier")
        return []

    try:
        log.info(f"Running classifier on commits, number of commit: {len(commits)}")
        results = classify_commits(commits)
        return results
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'classifier_agent',
                "message": "An error occurred",
            }
        )










