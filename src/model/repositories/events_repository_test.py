import pytest

from .events_repository import EventsRepository

@pytest.mark.skip("Insert in DB")
def test_insert_events():
  event_name = "eventTest"
  event_repository = EventsRepository()

  event_repository.insert(event_name)

def test_select_event():
  event_name = "eventTest"
  event_repository = EventsRepository()

  event = event_repository.select_event(event_name)

  print(event)
  print(event.name)