from models.game_mode import GameMode
from models.modifiers import Modifiers

class ScheduledEventLocation:
    mode: GameMode
    modifiers: Modifiers
    id: int
    map: str