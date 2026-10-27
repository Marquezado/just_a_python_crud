
from fastapi import APIRouter, HTTPException
from schemas import Note
import storage
from storage import notes


router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


@router.get("/")
def get_notes(limit: int = 10):
    return list(storage.notes.values())[:limit]

@router.get("/{note_id}")
def get_note(note_id: int):
    note = storage.notes.get(note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

@router.post("/", status_code=201)
def create_note(note: Note):
    global_next_id = storage.next_id

    note.id = global_next_id
    notes[global_next_id] = note
    storage.next_id += 1
    return note

@router.delete("/{note_id}")
def delete_note(note_id: int):
    note = storage.notes.pop(note_id, None)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

@router.put("/{note_id}")
def update_note(note_id: int, update_note: Note):
    note = notes.get(note_id)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="this note does not exist"
        )
    note.title = update_note.title
    note.description = update_note.description
    note.status = update_note.status

    return note