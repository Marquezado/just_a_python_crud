
from fastapi import FastAPI, HTTPException
from routers.notes import router as notes_router

app = FastAPI(
    title="My Notes CRUD API",
)

app.include_router(notes_router)


@app.get("/")
def home():
    return {"message": "This api is running"}
