from sqlalchemy import Column, String, Integer, ForeignKey 

from src.model.configs.base import Base

class Subscribers(Base):
  __tablename__ = "Subscribers"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  link = Column(String, nullable=True)
  event_id = Column(Integer, ForeignKey("Events.id")) 