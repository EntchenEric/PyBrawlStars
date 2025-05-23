from models.match_mode import MatchMode
from models.player_entry import PlayerEntry
from models.banned_brawler_entry import BannedBrawlerEntry
from models.timer_preset import TimerPreset

class RegisterMatchRequest:
    mode: MatchMode
    players: list[PlayerEntry]
    location_id: int
    wins_required: int
    gadgets_allowed: bool
    banned_brawlers: list[BannedBrawlerEntry]
    timer_preset: TimerPreset
