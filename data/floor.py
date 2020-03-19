import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Floor(SqlAlchemyBase):
    __tablename__ = 'floor'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # house_id

