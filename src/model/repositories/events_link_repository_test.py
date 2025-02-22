import pytest
from .events_link_repository import EventsLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_events_link():
  event_id = 12
  subscriber_id = 8
  
  event_link_repository = EventsLinkRepository()

  event_link_repository.insert(event_id, subscriber_id)