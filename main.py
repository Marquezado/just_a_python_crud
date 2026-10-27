
from fastapi import FastAPI, HTTPException
from schemas import Note

app = FastAPI(
    title="My Notes CRUD API",
)

notes:  [int, Note] = {}
next_id = 99999

@app.get("/")
def home():
    return {"message": "This api is running"}

@app.get("/notes")
def get_notes(limit: int = 10):
    return list(notes.values())[:limit]

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    note = notes.get(note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

@app.post("/notes", status_code=201)
def create_note(note: Note):
    global next_id
    note.id = next_id
    notes[next_id] = note
    next_id += 1
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    note = notes.pop(note_id, None)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

