from typing import Any, TYPE_CHECKING, List, Optional

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
        duration: The duration of the battle in seconds.
        trophy_change: The change in trophies after the battle.
        rank: The rank achieved in the battle (for solo/duo modes).
        star_player_tag: The tag of the star player (if any).
        teams: List of teams that participated in the battle.
    """

    duration: int
    """The duration of the battle in seconds."""

    trophy_change: int
    """The change in trophies after the battle. Can be positive or negative."""

    rank: Optional[int]
    """The rank achieved in the battle (for solo/duo modes). None for 3v3 modes."""

    star_player_tag: Optional[str]
    """The tag of the star player. None if no star player was selected."""

    teams: List[List[str]]
    """List of teams that participated in the battle. Each team is a list of player tags."""

    def __init__(
        self,
        duration: int,
        trophy_change: int,
        rank: Optional[int] = None,
        star_player_tag: Optional[str] = None,
        teams: Optional[List[List[str]]] = None
    ):
        """
        Initialize a new BattleResult instance.

        Args:
            duration: The duration of the battle in seconds.
            trophy_change: The change in trophies after the battle.
            rank: The rank achieved in the battle (for solo/duo modes).
            star_player_tag: The tag of the star player (if any).
            teams: List of teams that participated in the battle.
        """
        self.duration = duration
        self.trophy_change = trophy_change
        self.rank = rank
        self.star_player_tag = star_player_tag
        self.teams = teams or []

    def __str__(self) -> str:
        """
        Returns the string representation of the battle result.

        Returns:
            str: A string containing the battle duration and trophy change.
        """
        result = f"Battle ({self.duration}s): {self.trophy_change:+d} trophies"
        if self.rank:
            result += f", Rank {self.rank}"
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
            teams_data = json_data.get("teams", [])
            if not isinstance(teams_data, list):
                raise ParseException(f"Expected 'teams' to be a list, got {type(teams_data)}")
            teams = []
            for team in teams_data:
                if not isinstance(team, list):
                    raise ParseException(f"Expected team to be a list, got {type(team)}")
                teams.append([str(tag) for tag in team if isinstance(tag, (str, int))])

            return BattleResult(
                duration=int(json_data.get("duration", 0)),
                trophy_change=int(json_data.get("trophyChange", 0)),
                rank=int(json_data["rank"]) if "rank" in json_data else None,
                star_player_tag=str(json_data["starPlayer"]["tag"]) if "starPlayer" in json_data else None,
                teams=teams
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse battle result data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing battle result data: {e}")