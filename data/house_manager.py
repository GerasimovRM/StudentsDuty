import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class HouseManager(SqlAlchemyBase):
    __tablename__ = 'house_manager'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # house_id
    # user_id


