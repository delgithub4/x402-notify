from fastapi import FastAPI

from routes.notify import router as notify_router

app = FastAPI(
    title="x402-notify",
    version="1.0.0"
)

app.include_router(notify_router)


@app.get("/")
def home():

    return {
        "service": "x402-notify",
        "status": "running"
    }
