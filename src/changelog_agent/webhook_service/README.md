# Flow Diagram

GitHub
  ↓
Webhook Receiver
  - verify signature
  - detect event
  - extract fields
  - normalize
  ↓
Orchestrator Agent
  ↓
Multi-Agent Pipeline


# file stucture
webhook-service/
 ├── app/
 │   ├── main.py - FastAPI entry point
 │   ├── api/
 │   │   └── github_webhook.py - Github webhook endpoint
 │   ├── event/
 │   │   └── event_handlers.py - Github event handlers
 │   ├── core/
 │   │   └── security.py - Github signature verification
 │   ├── schemas/
 │   │   └── orchestrator.py - Orchestrator input schema
 │   └── services/
 │       └── orchestrator_client.py - Send data to orchestrator
 └── requirements.txt





