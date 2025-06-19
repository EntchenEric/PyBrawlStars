from typing import Any, TYPE_CHECKING, List, Optional
from models.match_mode import MatchMode
from models.game_mode import GameMode

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class RegisterMatchRequest:
    """
    Represents a request to register a match.

    Attributes:
        match_mode: The mode of the match.
        game_mode: The game mode to be played.
        map_id: The ID of the map to play on.
        team_size: The size of each team.
        player_tags: List of player tags participating in the match.
        team_indices: List of team indices for each player.
        is_power_match: Whether this is a power match.
        use_gadgets: Whether gadgets are allowed.
        use_star_powers: Whether star powers are allowed.
        is_ranked: Whether this is a ranked match.
        is_tutorial: Whether this is a tutorial match.
        is_friendly: Whether this is a friendly match.
    """

    match_mode: MatchMode
    """The mode of the match (e.g., NORMAL, RANKED, FRIENDLY)."""

    game_mode: GameMode
    """The game mode to be played (e.g., GEM_GRAB, SHOWDOWN)."""

    map_id: int
    """The ID of the map to play on."""

    team_size: int
    """The size of each team."""

    player_tags: List[str]
    """List of player tags participating in the match."""

    team_indices: List[int]
    """List of team indices for each player (0 or 1)."""

    is_power_match: bool
    """Whether this is a power match."""

    use_gadgets: bool
    """Whether gadgets are allowed in the match."""

    use_star_powers: bool
    """Whether star powers are allowed in the match."""

    is_ranked: bool
    """Whether this is a ranked match."""

    is_tutorial: bool
    """Whether this is a tutorial match."""

    is_friendly: bool
    """Whether this is a friendly match."""

    def __init__(
        self,
        match_mode: MatchMode,
        game_mode: GameMode,
        map_id: int,
        team_size: int,
        player_tags: List[str],
        team_indices: List[int],
        is_power_match: bool = False,
        use_gadgets: bool = True,
        use_star_powers: bool = True,
        is_ranked: bool = False,
        is_tutorial: bool = False,
        is_friendly: bool = False
    ):
        """
        Initialize a new RegisterMatchRequest instance.

        Args:
            match_mode: The mode of the match.
            game_mode: The game mode to be played.
            map_id: The ID of the map to play on.
            team_size: The size of each team.
            player_tags: List of player tags participating.
            team_indices: List of team indices for each player.
            is_power_match: Whether this is a power match.
            use_gadgets: Whether gadgets are allowed.
            use_star_powers: Whether star powers are allowed.
            is_ranked: Whether this is a ranked match.
            is_tutorial: Whether this is a tutorial match.
            is_friendly: Whether this is a friendly match.
        """
        self.match_mode = match_mode
        self.game_mode = game_mode
        self.map_id = map_id
        self.team_size = team_size
        self.player_tags = player_tags
        self.team_indices = team_indices
        self.is_power_match = is_power_match
        self.use_gadgets = use_gadgets
        self.use_star_powers = use_star_powers
        self.is_ranked = is_ranked
        self.is_tutorial = is_tutorial
        self.is_friendly = is_friendly

    def __str__(self) -> str:
        """
        Returns the string representation of the register match request.

        Returns:
            str: A string containing the match mode, game mode, and player count.
        """
        mode_str = self.match_mode.value.replace("_", " ").title()
        game_str = self.game_mode.value.replace("_", " ").title()
        return f"{mode_str} {game_str} match with {len(self.player_tags)} players"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "RegisterMatchRequest":
        """
        Creates a RegisterMatchRequest instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            RegisterMatchRequest: A new RegisterMatchRequest instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for register match request data, got {type(json_data)}")

        try:
            match_mode_str = json_data.get("matchMode")
            if match_mode_str is None:
                raise ParseException("Missing 'matchMode' field in register match request JSON data")
            try:
                match_mode = MatchMode(str(match_mode_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'matchMode': '{match_mode_str}'. Error: {e}")

            game_mode_str = json_data.get("gameMode")
            if game_mode_str is None:
                raise ParseException("Missing 'gameMode' field in register match request JSON data")
            try:
                game_mode = GameMode(str(game_mode_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'gameMode': '{game_mode_str}'. Error: {e}")

            player_tags = [str(tag) for tag in json_data.get("playerTags", [])]
            team_indices = [int(idx) for idx in json_data.get("teamIndices", [])]

            if len(player_tags) != len(team_indices):
                raise ParseException("Number of player tags must match number of team indices")

            return RegisterMatchRequest(
                match_mode=match_mode,
                game_mode=game_mode,
                map_id=int(json_data.get("mapId", 0)),
                team_size=int(json_data.get("teamSize", 3)),
                player_tags=player_tags,
                team_indices=team_indices,
                is_power_match=bool(json_data.get("isPowerMatch", False)),
                use_gadgets=bool(json_data.get("useGadgets", True)),
                use_star_powers=bool(json_data.get("useStarPowers", True)),
                is_ranked=bool(json_data.get("isRanked", False)),
                is_tutorial=bool(json_data.get("isTutorial", False)),
                is_friendly=bool(json_data.get("isFriendly", False))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse register match request data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing register match request data: {e}")
