from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class MatchLocation:
    """
    Represents a location where a match takes place.

    Attributes:
        id: The unique identifier of the location.
        region: The region where the match is hosted.
        ip: The IP address of the match server.
        port: The port number of the match server.
    """

    id: int
    """The unique identifier of the location."""

    region: str
    """The region where the match is hosted (e.g., 'EU', 'NA')."""

    ip: str
    """The IP address of the match server."""

    port: int
    """The port number of the match server."""

    def __init__(
        self,
        id: int,
        region: str,
        ip: str,
        port: int
    ):
        """
        Initialize a new MatchLocation instance.

        Args:
            id: The unique identifier of the location.
            region: The region where the match is hosted.
            ip: The IP address of the match server.
            port: The port number of the match server.
        """
        self.id = id
        self.region = region
        self.ip = ip
        self.port = port

    def __str__(self) -> str:
        """
        Returns the string representation of the match location.

        Returns:
            str: A string containing the region and server info.
        """
        return f"{self.region} ({self.ip}:{self.port})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "MatchLocation":
        """
        Creates a MatchLocation instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            MatchLocation: A new MatchLocation instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for match location data, got {type(json_data)}")

        try:
            return MatchLocation(
                id=int(json_data.get("id", 0)),
                region=str(json_data.get("region", "")),
                ip=str(json_data.get("ip", "")),
                port=int(json_data.get("port", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse match location data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing match location data: {e}")