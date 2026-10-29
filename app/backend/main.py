from fastapi import FastAPI

app = FastAPI(title="AI-Augmented SDLC", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
