from models.match_team import MatchTeam
from models.completed_game import CompletedGame
from models.game_phase import GamePhase
from models.player_match_status import PlayerMatchStatus
from models.match_state import MatchState

class Match:
    initiative_side: int
    round: int
    teams: list[MatchTeam]
    games: list[CompletedGame]
    phase: GamePhase
    players:PlayerMatchStatus
    state: MatchState
    id: str
