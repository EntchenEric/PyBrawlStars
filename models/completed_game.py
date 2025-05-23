from maps.completed_game_team import CompletedGameTeam
from maps.match_location import MatchLocation

class CompletedGame:
    teams: list[CompletedGameTeam]
    duration: int
    location: MatchLocation
    replay_id: str