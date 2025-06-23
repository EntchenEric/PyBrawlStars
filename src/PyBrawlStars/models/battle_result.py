from typing import Any, TYPE_CHECKING, List, Optional
from datetime import datetime
from .game_mode import GameMode
from .battle_player import BattlePlayer

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class BattleResult:
    """
    Represents the result of a battle in the game.

    Attributes:
        battle_time: The timestamp when the battle occurred.
        duration: The duration of the battle in seconds.
        trophy_change: The change in trophies after the battle.
        mode: The game mode of the battle.
        type: The type of battle.
        result: The result of the battle.
        star_player: The star player of the battle (if any).
        teams: List of teams that participated in the battle.
    """

    battle_time: datetime
    """The timestamp when the battle occurred."""

    duration: int
    """The duration of the battle in seconds."""

    trophy_change: int
    """The change in trophies after the battle. Can be positive or negative."""

    mode: GameMode
    """The game mode of the battle."""

    type: str
    """The type of battle."""

    result: str
    """The result of the battle."""

    star_player: BattlePlayer | None
    """The star player of the battle (if any)."""

    teams: List[List[BattlePlayer]]
    """List of teams that participated in the battle."""

    def __init__(
        self,
        battle_time: datetime,
        duration: int,
        trophy_change: int,
        mode: GameMode,
        type: str,
        result: str,
        star_player: BattlePlayer | None = None,
        teams: List[List[BattlePlayer]] | None = None
    ):
        """
        Initialize a new BattleResult instance.

        Args:
            battle_time: The timestamp when the battle occurred.
            duration: The duration of the battle in seconds.
            trophy_change: The change in trophies after the battle.
            mode: The game mode of the battle.
            type: The type of battle.
            result: The result of the battle.
            star_player: The star player of the battle (if any).
            teams: List of teams that participated in the battle.
        """
        self.battle_time = battle_time
        self.duration = duration
        self.trophy_change = trophy_change
        self.mode = mode
        self.type = type
        self.result = result
        self.star_player = star_player
        self.teams = teams or []

    def __str__(self) -> str:
        """
        Returns the string representation of the battle result.

        Returns:
            str: A string containing the battle duration and trophy change.
        """
        result = f"Battle ({self.duration}s): {self.trophy_change:+d} trophies, Result: {self.result}"
        return result

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BattleResult":
        """
        Creates a BattleResult instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BattleResult: A new BattleResult instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for battle result data, got {type(json_data)}")

        try:
            # Parse battle time
            battle_time_str = json_data.get("battleTime", "")
            if battle_time_str:
                battle_time = datetime.fromisoformat(battle_time_str.rstrip('Z'))
            else:
                battle_time = datetime.now()

            # Parse mode
            mode_data = json_data.get("battle", {}).get("mode")
            if not isinstance(mode_data, dict):
                raise ParseException(f"Expected 'mode' to be a dictionary, got {type(mode_data)}")
            mode = GameMode.from_json(mode_data, client)

            # Parse star player
            star_player_data = json_data.get("battle", {}).get("starPlayer")
            star_player = BattlePlayer.from_json(star_player_data, client) if star_player_data else None

            # Parse teams
            teams_data = json_data.get("battle", {}).get("teams", [])
            if not isinstance(teams_data, list):
                raise ParseException(f"Expected 'teams' to be a list, got {type(teams_data)}")
            
            teams = []
            for team_data in teams_data:
                if not isinstance(team_data, list):
                    raise ParseException(f"Expected team to be a list, got {type(team_data)}")
                team = [BattlePlayer.from_json(player_data, client) for player_data in team_data if isinstance(player_data, dict)]
                teams.append(team)

            return BattleResult(
                battle_time=battle_time,
                duration=int(json_data.get("battle", {}).get("duration", 0)),
                trophy_change=int(json_data.get("battle", {}).get("trophyChange", 0)),
                mode=mode,
                type=str(json_data.get("battle", {}).get("type", "")),
                result=str(json_data.get("battle", {}).get("result", "")),
                star_player=star_player,
                teams=teams
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse battle result data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing battle result data: {e}")