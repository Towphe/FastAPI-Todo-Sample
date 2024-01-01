from sqlalchemy import Column, DateTime, Integer, String, Float, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base  = declarative_base()

class Entry(Base):
    __tablename__ = "entry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String, default=None)
    is_done = Column(Boolean, default=False)
    created_date = Column(Date, default=date.today)
    updated_date = Column(Date, default=None)

    def toDict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "is_done" : self.is_done,
            "created_date" : self.created_date,
            "updated_date" : self.updated_date
        }