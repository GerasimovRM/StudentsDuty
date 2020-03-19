import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class FloorManager(SqlAlchemyBase):
    __tablename__ = 'floor_manager'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # floor_id
    # user_id


