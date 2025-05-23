from models.scheduled_event_location import ScheduledEventLocation

class ScheduledEvent:
    event: ScheduledEventLocation
    slot_id: int
    start_time: str
    end_time: str