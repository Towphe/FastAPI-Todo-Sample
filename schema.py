from pydantic import BaseModel

class Entry(BaseModel):
    title: str
    description: str
    is_done: str

    class Config:
        orm_mode = True