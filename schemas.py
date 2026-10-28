from pydantic import BaseModel, Field

class NoteBase(BaseModel):
    title: str = Field(max_length=50)
    description: str | None = None
    completed: bool = False

class Note(NoteBase):
    id: int

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: str | None = None
    description : str | None = None
    completed: bool | None = None

class NoteStatusUpdate(BaseModel):
    completed: bool
