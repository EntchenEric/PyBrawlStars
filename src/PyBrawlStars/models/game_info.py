from typing import Any, TYPE_CHECKING, List, Optional
from models.game_mode import GameMode
from models.event_modifier import EventModifier

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class GameInfo:
    """
    Represents information about a game.

    Attributes:
        mode: The game mode being played.
        map_name: The name of the map.
        map_id: The unique identifier of the map.
        modifiers: List of modifiers applied to the game.
        score_limit: The score limit for the game mode.
        time_limit: The time limit for the game in seconds.
        trophy_game: Whether the game affects trophies.
        star_game: Whether the game affects star points.
        tutorial: Whether the game is a tutorial.
        survival: Whether the game is a survival mode.
        team_size: The size of each team.
        ranked: Whether the game is ranked.
        big_game: Whether the game is a big game mode.
        has_timed_super: Whether brawlers have timed supers.
        has_second_abilities: Whether brawlers have second abilities.
    """

    mode: GameMode
    """The game mode being played (e.g., GEM_GRAB, SHOWDOWN)."""

    map_name: str
    """The name of the map where the game takes place."""

    map_id: int
    """The unique identifier of the map."""

    modifiers: List[EventModifier]
    """List of modifiers applied to the game (e.g., ENERGY_DRINK, HEALING_MUSHROOMS)."""

    score_limit: Optional[int]
    """The score limit for the game mode. None if not applicable."""

    time_limit: Optional[int]
    """The time limit for the game in seconds. None if not applicable."""

    trophy_game: bool
    """Whether the game affects trophies."""

    star_game: bool
    """Whether the game affects star points."""

    tutorial: bool
    """Whether the game is a tutorial."""

    survival: bool
    """Whether the game is a survival mode."""

    team_size: int
    """The size of each team."""

    ranked: bool
    """Whether the game is ranked."""

    big_game: bool
    """Whether the game is a big game mode."""

    has_timed_super: bool
    """Whether brawlers have timed supers."""

    has_second_abilities: bool
    """Whether brawlers have second abilities."""

    def __init__(
        self,
        mode: GameMode,
        map_name: str,
        map_id: int,
        modifiers: Optional[List[EventModifier]] = None,
        score_limit: Optional[int] = None,
        time_limit: Optional[int] = None,
        trophy_game: bool = False,
        star_game: bool = False,
        tutorial: bool = False,
        survival: bool = False,
        team_size: int = 3,
        ranked: bool = False,
        big_game: bool = False,
        has_timed_super: bool = False,
        has_second_abilities: bool = False
    ):
        """
        Initialize a new GameInfo instance.

        Args:
            mode: The game mode being played.
            map_name: The name of the map.
            map_id: The unique identifier of the map.
            modifiers: List of modifiers applied to the game.
            score_limit: The score limit for the game mode.
            time_limit: The time limit for the game in seconds.
            trophy_game: Whether the game affects trophies.
            star_game: Whether the game affects star points.
            tutorial: Whether the game is a tutorial.
            survival: Whether the game is a survival mode.
            team_size: The size of each team.
            ranked: Whether the game is ranked.
            big_game: Whether the game is a big game mode.
            has_timed_super: Whether brawlers have timed supers.
            has_second_abilities: Whether brawlers have second abilities.
        """
        self.mode = mode
        self.map_name = map_name
        self.map_id = map_id
        self.modifiers = modifiers or []
        self.score_limit = score_limit
        self.time_limit = time_limit
        self.trophy_game = trophy_game
        self.star_game = star_game
        self.tutorial = tutorial
        self.survival = survival
        self.team_size = team_size
        self.ranked = ranked
        self.big_game = big_game
        self.has_timed_super = has_timed_super
        self.has_second_abilities = has_second_abilities

    def __str__(self) -> str:
        """
        Returns the string representation of the game info.

        Returns:
            str: A string containing the game mode and map name.
        """
        mode_str = self.mode.value.replace("_", " ").title()
        modifiers_str = f" with {', '.join(m.value for m in self.modifiers)}" if self.modifiers else ""
        return f"{mode_str} on {self.map_name}{modifiers_str}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "GameInfo":
        """
        Creates a GameInfo instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            GameInfo: A new GameInfo instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for game info data, got {type(json_data)}")

        try:
            mode_str = json_data.get("mode")
            if mode_str is None:
                raise ParseException("Missing 'mode' field in game info JSON data")
            try:
                mode = GameMode(str(mode_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'mode': '{mode_str}'. Error: {e}")

            modifiers_data = json_data.get("modifiers", [])
            if not isinstance(modifiers_data, list):
                raise ParseException(f"Expected 'modifiers' to be a list, got {type(modifiers_data)}")
            modifiers = []
            for modifier_str in modifiers_data:
                try:
                    modifiers.append(EventModifier(str(modifier_str)))
                except ValueError as e:
                    print(f"Warning: Invalid modifier value '{modifier_str}'. Error: {e}")

            return GameInfo(
                mode=mode,
                map_name=str(json_data.get("mapName", "")),
                map_id=int(json_data.get("mapId", 0)),
                modifiers=modifiers,
                score_limit=int(json_data["scoreLimit"]) if "scoreLimit" in json_data else None,
                time_limit=int(json_data["timeLimit"]) if "timeLimit" in json_data else None,
                trophy_game=bool(json_data.get("trophyGame", False)),
                star_game=bool(json_data.get("starGame", False)),
                tutorial=bool(json_data.get("tutorial", False)),
                survival=bool(json_data.get("survival", False)),
                team_size=int(json_data.get("teamSize", 3)),
                ranked=bool(json_data.get("ranked", False)),
                big_game=bool(json_data.get("bigGame", False)),
                has_timed_super=bool(json_data.get("hasTimedSuper", False)),
                has_second_abilities=bool(json_data.get("hasSecondAbilities", False))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse game info data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing game info data: {e}")