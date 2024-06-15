from db_classes.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column('user_id', primary_key=True)
    user_name: Mapped[str] = mapped_column('user_name', unique=True)
    user_email: Mapped[str] = mapped_column('user_email')
    user_password: Mapped[str] = mapped_column('user_password')

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def __repr__(self):
        return self.user_name + " " + self.user_email

