from src.changelog_agent.release_service.app.prompt.release_prompt import release_manager_prompt
from src.changelog_agent.llm_clients.llm_client import llm
from src.changelog_agent.release_service.app.schemas.parser import release_manager_parser
from datetime import datetime

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log


def release_manager(summarized_commits: str):
    """
    Read all the summarized commits and make a release note
    :Args
        summarized_commits:
    """

    try:
        release_note_chain = (
            release_manager_prompt
            | llm
            | release_manager_parser
        )
        log.info("Release manager chain created.")

        result = release_note_chain.invoke({
            "release_version": '0.0.1',
            "release_date": datetime.now().isoformat(),
            "summarized_commits": summarized_commits
        })

        log.info("Release manager chain invoked.")

        return result
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'classify_commit',
                'message': 'error while classifying commit',
            }
        )









    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'release_commits',
                'message': 'error while getting release note',
            }
        )













