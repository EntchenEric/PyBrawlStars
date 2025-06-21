from models.match_team import MatchTeam
from models.completed_game import CompletedGame
from models.game_phase import GamePhase
from models.player_match_status import PlayerMatchStatus
from models.match_state import MatchState
from typing import Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Match:
    """
    Represents a match in the game.

    Attributes:
        initiative_side: The side that has the initiative.
        round: The current round number.
        teams: List of teams in the match.
        games: List of completed games.
        phase: The current phase of the game.
        players: The match status of players.
        state: The current state of the match.
        id: The unique identifier of the match.
    """

    initiative_side: int
    """The side (team) that currently has the initiative in the match (0 or 1)."""

    round: int
    """The current round number in the match."""

    teams: List[MatchTeam]
    """List of teams participating in the match, containing player information and team stats."""

    games: List[CompletedGame]
    """List of completed games in this match, with their results and statistics."""

    phase: GamePhase
    """The current phase of the game (e.g., preparation, in progress, ended)."""

    players: PlayerMatchStatus
    """The current status of all players in the match, including their readiness and connection state."""

    state: MatchState
    """The current state of the match (e.g., waiting, in progress, ended)."""

    id: str
    """The unique identifier of the match."""

    def __init__(
        self,
        initiative_side: int,
        round: int,
        teams: List[MatchTeam],
        games: List[CompletedGame],
        phase: GamePhase,
        players: PlayerMatchStatus,
        state: MatchState,
        id: str
    ):
        """
        Initialize a new Match instance.

        Args:
            initiative_side: The side that has the initiative.
            round: The current round number.
            teams: List of teams in the match.
            games: List of completed games.
            phase: The current phase of the game.
            players: The match status of players.
            state: The current state of the match.
            id: The unique identifier of the match.
        """
        self.initiative_side = initiative_side
        self.round = round
        self.teams = teams
        self.games = games
        self.phase = phase
        self.players = players
        self.state = state
        self.id = id

    def __str__(self) -> str:
        """
        Returns the string representation of the match.

        Returns:
            str: A string containing the match ID and current state.
        """
        return f"Match {self.id} - Round {self.round} ({self.state.value})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Match":
        """
        Creates a Match instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Match: A new Match instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for match data, got {type(json_data)}")

        try:
            teams_data = json_data.get("teams", [])
            if not isinstance(teams_data, list):
                raise ParseException(f"Expected 'teams' to be a list, got {type(teams_data)}")
            teams = [MatchTeam.from_json(t, client) for t in teams_data if isinstance(t, dict)]

            games_data = json_data.get("games", [])
            if not isinstance(games_data, list):
                raise ParseException(f"Expected 'games' to be a list, got {type(games_data)}")
            games = [CompletedGame.from_json(g, client) for g in games_data if isinstance(g, dict)]

            phase_str = json_data.get("phase")
            if phase_str is None:
                raise ParseException("Missing 'phase' field in match JSON data")
            try:
                phase = GamePhase(str(phase_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'phase': '{phase_str}'. Error: {e}")

            state_str = json_data.get("state")
            if state_str is None:
                raise ParseException("Missing 'state' field in match JSON data")
            try:
                state = MatchState(str(state_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'state': '{state_str}'. Error: {e}")

            players_data = json_data.get("players")
            if not isinstance(players_data, dict):
                raise ParseException(f"Expected 'players' to be a dictionary, got {type(players_data)}")
            players = PlayerMatchStatus.from_json(players_data, client)

            return Match(
                initiative_side=int(json_data.get("initiativeSide", 0)),
                round=int(json_data.get("round", 0)),
                teams=teams,
                games=games,
                phase=phase,
                players=players,
                state=state,
                id=str(json_data.get("id", ""))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse match data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing match data: {e}")
