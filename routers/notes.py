
from fastapi import APIRouter, HTTPException
from schemas import Note
import storage


router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


@router.get("/")
def get_notes(limit: int = 10):
    return list(storage.values())[:limit]

@router.get("/{note_id}")
def get_note(note_id: int):
    note = storage.get(note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

@router.post("/", status_code=201)
def create_note(note: Note):
    note.id = storage.next_id
    storage[storage.next_id] = note
    storage.next_id += 1
    return note

@router.delete("/{note_id}")
def delete_note(note_id: int):
    note = storage.pop(note_id, None)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

