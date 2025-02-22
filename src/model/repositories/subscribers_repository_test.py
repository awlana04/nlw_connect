import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
  subscriber_info = {
    "name": "John Doe",
    "email": "john@doe.com",
    "event_id": 2
  }

  subscriber_repository = SubscribersRepository()
  subscriber_repository.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
  email = "john@doe.com"
  event_id = 2

  subscriber_repository = SubscribersRepository()

  response = subscriber_repository.select_subscriber(email, event_id)

  print(response.name)

@pytest.mark.skip("Select in DB")
def test_ranking():
  event_id = 1

  subscriber_repository = SubscribersRepository()
  response = subscriber_repository.get_ranking(event_id)

  for element in response:
    print(f"Link: {element.link}, total de inscritos: {element.total}")