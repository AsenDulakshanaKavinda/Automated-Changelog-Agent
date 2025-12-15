# Webhook Service – Architecture & Flow

## Flow Diagram

```text

# file structure
webhook-service/
 ├── app/
 │   ├── app.py - FastAPI entry point
 │   ├── api/
 │   │   └── github_webhook.py - Github webhook endpoint
 │   ├── event/
 │   │   └── event_handlers.py - Github event handlers
 │   │   └── ... event handlers (push, pr ...)
 │   ├── core/
 │   │   └── security.py - Github signature verification
 │   ├── schemas/
 │   │   └── orchestrator.py - Orchestrator input schema
 │   └── services/
 │       └── orchestrator_client.py - Send data to orchestrator
 │── main.py - End point
 └── requirements.txt

```



