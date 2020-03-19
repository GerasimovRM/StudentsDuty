import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class SuperAdmin(SqlAlchemyBase):
    __tablename__ = 'super_admin'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # admin_id
