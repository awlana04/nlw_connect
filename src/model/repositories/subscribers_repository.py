from src.model.configs.connection import DBConnectionHandler
from src.model.entities.subscribers import Subscribers
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
  def insert(self, subscriber_info: dict) -> None:
    with DBConnectionHandler() as db:
      try:
        new_subscriber = Subscribers(name=subscriber_info.get('name'), email=subscriber_info.get('email'), link=subscriber_info.get('link'), event_id=subscriber_info.get('event_id'))

        db.session.add(new_subscriber)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()

        raise exception
  
  def select_subscriber(self, email: str, event_id: int) -> Subscribers:
    with DBConnectionHandler() as db:
      data = (
        db.session.query(Subscribers).filter(Subscribers.email == email, Subscribers.event_id == event_id).one_or_none()
      )

      return data