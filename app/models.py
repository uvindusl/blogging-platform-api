from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)
    tags = Column(ARRAY(String))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))