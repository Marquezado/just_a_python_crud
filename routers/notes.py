
from fastapi import APIRouter, HTTPException
from schemas import NoteCreate, NoteUpdate, Note, NoteStatusUpdate
import storage
from storage import notes


router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


@router.get("/")
def get_notes(limit: int = 10):
    return list(notes.values())[:limit]

@router.get("/{note_id}")
def get_note(note_id: int):
    note = notes.get(note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

@router.post("/", status_code=201)
def create_note(note_data: NoteCreate):
    new_id = storage.next_id

    note = Note(
        id=new_id,
        **note_data.model_dump()
    )

    notes[new_id] = note
    storage.next_id += 1
    return note

@router.patch("/{note_id}")
def update_note(note_id: int, update_note: NoteUpdate):
    note = notes.get(note_id)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="this note does not exist"
        )

    data = update_note.model_dump(exclude_unset=True)

    for field, value in data.items():
        setattr(note, field, value)

    return note

@router.delete("/{note_id}")
def delete_note(note_id: int):
    note = notes.pop(note_id, None)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist"
        )
    return note

@router.patch("/{note_id}/status")
def update_note_status(note_id: int, status_data: NoteStatusUpdate):
    note = notes.get(note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail="this note does not exist"
        )
    note.completed = status_data.completed
    return {"completed": note.completed}
