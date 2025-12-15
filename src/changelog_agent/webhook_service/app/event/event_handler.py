from src.changelog_agent.webhook_service.app.event.handle_push_event import handle_push_event
from src.changelog_agent.webhook_service.app.event.handle_pull_req_event import handle_pull_req_event


event_dict = {
    'push': handle_push_event,
    'pull_req': handle_pull_req_event,
}

def event_handler(event: str, payload: dict):
    return event_dict[event](payload)





