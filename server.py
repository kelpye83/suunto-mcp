import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Suunto MCP Server", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/mcp")
def mcp_manifest() -> dict[str, object]:
    return {
        "name": "suunto-mcp",
        "version": "1.0.0",
        "tools": [
            {
                "name": "get_activities",
                "description": "Returns sample Suunto activities",
                "input_schema": {"type": "object"},
            },
            {
                "name": "get_summary",
                "description": "Returns a sample activity summary",
                "input_schema": {"type": "object"},
            },
        ],
    }


@app.post("/tools/get_activities")
def get_activities() -> dict[str, list[str]]:
    return {"activities": ["running", "cycling", "swimming"]}


@app.post("/tools/get_summary")
def get_summary() -> dict[str, str]:
    return {"summary": "This is a sample summary."}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")