from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    try:
        payload = await request.json()
        event_type = request.headers.get("X-GitHub-Event")

        print("\nEvent Type:", event_type)

        if event_type == "push":
            repo = payload.get("repository", {}).get("name")
            author = payload.get("pusher", {}).get("name")

            commits = payload.get("commits", [])
            message = commits[0].get("message") if commits else "No commit message"

            print("\nPush Event Received:")
            print("Repository:", repo)
            print("Author:", author)
            print("Message:", message)

        return JSONResponse(
            status_code=200,
            content={"status": "success", "event": event_type}
        )

    except Exception as e:
        print("ERROR:", str(e))
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


















