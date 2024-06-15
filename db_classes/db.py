from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Float, inspect
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column
from sqlalchemy.sql import select

Base = declarative_base()
Session = sessionmaker()


def bind_engine(engine):
    Base.metadata.create_all(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    return session


def find_changes(original_dict, changed_dict):
    original = set(original_dict)
    changed = set(changed_dict)

    return dict(changed - original)
