from maps.siege_stats import SiegeStats
from maps.player_entry_completed_game import PlayerEntryCompletedGame

class CompletedGameTeam:
    score: int
    is_winner: bool
    siege: SiegeStats
    players: list[PlayerEntryCompletedGame]