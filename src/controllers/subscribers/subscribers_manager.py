from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersManager:
  def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
    self.__subscribers_repository = subscribers_repository

  def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
    link = http_request.param["link"]
    event_id = http_request.param["event_id"]

    subscribers = self.__subscribers_repository.select_subscribers_by_link(link, event_id)

    return self.__format_subscribers_by_link(subscribers)


  def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
    event_id = http_request.param["event_id"]
    
    event_ranking = self.__subscribers_repository.get_ranking(event_id)

    return self.__format_event_ranking(event_ranking)

  def __format_subscribers_by_link(self, subscribers: list) -> HttpResponse:
    formatted_subscriber = []

    for subscriber in subscribers:
      formatted_subscriber.append(
        {
          "name": subscriber.name,
          "email": subscriber.email
        }
      )

    return HttpResponse(
      body={
        "data": {
          "Type": "Subscriber",
          "count": len(formatted_subscriber),
          "subscribers": formatted_subscriber
        }
      },
      status_code=200
    )

  def __format_event_ranking(self, event_rankin: list) -> HttpResponse:
    formatted_event_ranking = []

    for position in event_rankin:
      formatted_event_ranking.append(
        {
          "link": position.link,
          "total_subscribers": position.total
        }
      )

    return HttpResponse(
      body={
        "data": {
          "Type": "Ranking",
          "count": len(formatted_event_ranking),
          "ranking": formatted_event_ranking
        }
      },
      status_code=200
    )