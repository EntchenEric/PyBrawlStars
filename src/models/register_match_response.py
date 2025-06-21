from typing import Any, TYPE_CHECKING, Optional
from models.match_location import MatchLocation

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class RegisterMatchResponse:
    """
    Represents a response to a match registration request.

    Attributes:
        match_id: The unique identifier of the registered match.
        location: The location where the match will be hosted.
        error_code: The error code if registration failed.
        error_message: The error message if registration failed.
    """

    match_id: str
    """The unique identifier of the registered match."""

    location: Optional[MatchLocation]
    """The location where the match will be hosted, or None if registration failed."""

    error_code: Optional[int]
    """The error code if registration failed, or None if successful."""

    error_message: Optional[str]
    """The error message if registration failed, or None if successful."""

    def __init__(
        self,
        match_id: str,
        location: Optional[MatchLocation] = None,
        error_code: Optional[int] = None,
        error_message: Optional[str] = None
    ):
        """
        Initialize a new RegisterMatchResponse instance.

        Args:
            match_id: The unique identifier of the registered match.
            location: The location where the match will be hosted.
            error_code: The error code if registration failed.
            error_message: The error message if registration failed.
        """
        self.match_id = match_id
        self.location = location
        self.error_code = error_code
        self.error_message = error_message

    def __str__(self) -> str:
        """
        Returns the string representation of the register match response.

        Returns:
            str: A string containing the match ID and status.
        """
        if self.error_code is not None:
            return f"Match registration failed: {self.error_message} (Error {self.error_code})"
        return f"Match {self.match_id} registered at {self.location}" if self.location else f"Match {self.match_id} registered"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "RegisterMatchResponse":
        """
        Creates a RegisterMatchResponse instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            RegisterMatchResponse: A new RegisterMatchResponse instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for register match response data, got {type(json_data)}")

        try:
            location_data = json_data.get("location")
            location = MatchLocation.from_json(location_data, client) if isinstance(location_data, dict) else None

            return RegisterMatchResponse(
                match_id=str(json_data.get("matchId", "")),
                location=location,
                error_code=int(json_data["errorCode"]) if "errorCode" in json_data else None,
                error_message=str(json_data["errorMessage"]) if "errorMessage" in json_data else None
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse register match response data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing register match response data: {e}")