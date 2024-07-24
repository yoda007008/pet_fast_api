from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

class Roles(BaseModel):
    roles = Table(
        "roles",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String, nullable=False),
        Column("permissions", JSON),
    )
class Users(BaseModel):
    users = Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("email", String, nullable=False),
        Column("username", String, nullable=False),
        Column("password", String, nullable=False),
        Column("registered_at", TIMESTAMP, default=datetime.utcnow),
        Column("role_id", Integer, ForeignKey("roles.id")),
        )
