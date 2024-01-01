from pydantic import BaseModel
from models import Entry

class Entry(BaseModel):
    title: str
    description: str = None
