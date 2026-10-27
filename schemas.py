from pydantic import BaseModel, Field


class Note(BaseModel):
    id: int | None = None
    title: str = Field(max_length=50)
    description: str | None = None
    status: str = Field(max_length=10)
