
import os
import logging

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI(
    title="DevOps Quest",
    description="DevOps Learning and Simulation Platform",
    version=APP_VERSION
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def home():
    return {
        "application": "DevOps Quest",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "message": "Welcome to DevOps Quest!"
    }


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/ready")
def ready():
    return {"status": "READY"}


@app.get("/api/missions")
def missions():
    return {
        "missions": [
            {
                "id": 1,
                "name": "Fix Docker Container",
                "points": 100
            },
            {
                "id": 2,
                "name": "Resolve Kubernetes Pod Failure",
                "points": 200
            },
            {
                "id": 3,
                "name": "Fix Grafana Alert",
                "points": 300
            }
        ]
    }


@app.get("/api/player")
def player():
    return {
        "name": "DevOps Engineer",
        "level": "Junior",
        "xp": 0
    }
