from fastapi import FastAPI
from routing_test import router as todo_router

app = FastAPI(
    title="Fast API PRACTICE"
)

app.include_router(todo_router)


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

