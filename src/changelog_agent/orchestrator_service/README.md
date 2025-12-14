# Webhook Service – Architecture & Flow

### Flow Diagram
```text
HTTP Request
   ↓
main.py (server starts)
   ↓
app/app.py (creates FastAPI app)
   ↓
app/api/orchestrator.py (endpoint)
   ↓
app/schemas/orchestrator_input.py (validate input)
   ↓
Orchestrator Logic (call other agents/services)
```

### File Structure
```text
orchestrator-service/
 ├── app/
 │   ├── app.py - Create and configures the FastAPI application
 │   ├── api/
 │   │   └── orchestrator.py - Orchestrator API router
 │   ├── schemas/
 │       └── orchestrator_input.py - Orchestrator input schema (pydantic)
 │── main.py - End point
 └── requirements.txt

