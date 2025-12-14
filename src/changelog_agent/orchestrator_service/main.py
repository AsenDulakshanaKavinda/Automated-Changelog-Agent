import uvicorn

def run():
    uvicorn.run(
        "src.changelog_agent.orchestrator_service.app.app:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )


if __name__ == "__main__":
    run()








