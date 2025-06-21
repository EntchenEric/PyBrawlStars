from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

class PlayerRankingClub:
    """
    Represents a club for a player in the ranking leaderboard.

    Attributes:
        name: The name of the club.
    """
    name: str
    """The name of the club."""

    def __init__(self, name: str):
        """
        Initialize a new PlayerRankingClub instance.

        Args:
            name: The name of the club.
        """
        self.name = name

    def __str__(self) -> str:
        """
        Returns the string representation of the club.

        Returns:
            str: The club's name.
        """
        return self.name

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerRankingClub":
        """
        Creates a PlayerRankingClub instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerRankingClub: A new PlayerRankingClub instance.
        """
        name = str(json_data.get("name", "N/A")) if isinstance(json_data, dict) else "N/A"
        return PlayerRankingClub(name=name)