from db_classes.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(Base, UserMixin):
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

    def get_id(self):
        return self.user_id


def create_user(name, email, password, session):
    user = session.query(User).filter_by(user_name=name).first()

    if user:
        print("exists")
        return -1
    else:
        new_user = User(name, email, generate_password_hash(password))
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user.user_id


def login(name, password, session):
    user = session.query(User).filter_by(user_name=name).first()
    if check_password_hash(user.user_password, password):
        return user.user_id
    else:
        return -1


def get_user_by_id(user_id, session):
    return session.query(User.filter_by(User.user_id == user_id))
