from src.changelog_agent.classifier_service.app.prompts.classification_prompt import classifier_prompt
from src.changelog_agent.classifier_service.app.llm_clients.llm_client import llm
from src.changelog_agent.classifier_service.app.schemas.parser import classification_parser

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

from typing import Any, List


def classify_commits(commits) -> List[Any] | None:
    """
    Read all the commits and classify them.

    Args:
        commits: list of commits
    """
    results = []

    try:
       classification_chain = (
           classifier_prompt
           | llm
           | classification_parser
       )
       log.info(f'classification_chain created')

       log.info(f'commits ----{commits}')

       for commit in commits:
           log.info("Classifying commit: %s", commit.sha)

           result = classification_chain.invoke({
               "commit_sha": commit.sha,
               "message": commit.message,
               "files_changed": commit.file_changed,
           })

           results.append({
               "commit_sha": commit.sha,
               "classification": result,
           })

       log.info(f'classification_chain invoked')
       return results
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'classify_commit',
                'message': 'error while classifying commit',
            }
        )










