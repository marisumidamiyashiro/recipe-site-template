from db_classes.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Collection(Base):
    __tablename__ = "collections"

    collection_id: Mapped[int] = mapped_column('collection_id', primary_key=True)
    collection_name: Mapped[str] = mapped_column('collection_name')

    def __init__(self, collection_name):
        self.collection_name = collection_name

    def __repr__(self):
        return self.collection_name

