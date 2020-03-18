import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    middle_name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    news = orm.relation("News", back_populates="customer")

    def __repr__(self):
        return f'id: {self.id}  name: {self.name}  email:{self.email}'
