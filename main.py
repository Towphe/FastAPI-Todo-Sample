import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Entry as ModelEntry
from schema import Entry as SchemaEntry
from entryDto import Entry as EntryDto

from sqlalchemy.sql.expression import update
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Date

import os
from dotenv import load_dotenv

load_dotenv('.env')

engine = create_engine(os.environ['DATABASE_URI'], echo=True)
meta = MetaData()

route = "todo"

conn = engine.connect()

entries = Table(
        'entry', meta,
        Column('id', Integer, primary_key = True, autoincrement=True),
        Column('title', String),
        Column('description', String),
        Column('is_done', Boolean),
        Column('created_date', Date),
        Column('updated_date', Date)
    )

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])

@app.get("/{route}/{id}")
async def GetEntry(id: int):
    entry = db.session.query(ModelEntry).first(ModelEntry.id == id)
    return entry

@app.get("/{route}")
async def GetEntries(skip: int = 0, limit: int = 10):
    entries = db.session.query(ModelEntry).slice(skip, limit).all()
    return entries

@app.post("/{route}")
async def CreateEntry(entryDto: EntryDto):
    new_entry = ModelEntry(title = entryDto.title, description = entryDto.description)
    db.session.add(new_entry)
    db.session.commit()
    return "New entry added."

@app.delete("/{route}/{id}")
async def DeleteEntry(id: int):
    delEntr = entries.delete().where(entries.c.id == id)
    conn.execute(delEntr)

    return "Entry deleted."

@app.patch("/{route}/{id}/done")
async def MarkDone(id: int):
    updEntr = entries.update().where(entries.c.id == id).values(is_done = True)
    conn.execute(updEntr)
    return "Marked entry #{id} as finished."

@app.patch("/{route}/{id}")
async def UpdateEntry(id: int, entryDto: EntryDto):
    updEntr = entries.update().where(entries.c.id == id).values(title = entryDto.title, description = entryDto.description)
    conn.execute(updEntr)
    return "Updated entry #{id}"