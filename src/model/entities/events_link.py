from sqlalchemy import Column, Integer, String, ForeignKey

from src.model.configs.base import Base

class EventsLink(Base):
  __tablename__ = 'Events_link'

  id = Column(Integer, primary_key=True, autoincrement=True)
  link = Column(String, nullable=False)
  event_id = Column(Integer, ForeignKey("Events.id"))
  subscriber_id = Column(Integer, ForeignKey("Subscribers.id"))