from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class ServiceVersion:
    """
    Represents the version information of the Brawl Stars service.

    Attributes:
        major: The major version number.
        minor: The minor version number.
        build: The build number.
        environment: The environment name.
        sha: The commit SHA of the service.
    """

    major: int
    """The major version number (e.g., 1 in 1.2.3)."""

    minor: int
    """The minor version number (e.g., 2 in 1.2.3)."""

    build: int
    """The build number (e.g., 3 in 1.2.3)."""

    environment: str
    """The environment name (e.g., 'production', 'staging')."""

    sha: str
    """The commit SHA of the service."""

    def __init__(
        self,
        major: int,
        minor: int,
        build: int,
        environment: str,
        sha: str
    ):
        """
        Initialize a new ServiceVersion instance.

        Args:
            major: The major version number.
            minor: The minor version number.
            build: The build number.
            environment: The environment name.
            sha: The commit SHA of the service.
        """
        self.major = major
        self.minor = minor
        self.build = build
        self.environment = environment
        self.sha = sha

    def __str__(self) -> str:
        """
        Returns the string representation of the service version.

        Returns:
            str: A string containing the version number and environment.
        """
        return f"v{self.major}.{self.minor}.{self.build} ({self.environment})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "ServiceVersion":
        """
        Creates a ServiceVersion instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            ServiceVersion: A new ServiceVersion instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for service version data, got {type(json_data)}")

        try:
            return ServiceVersion(
                major=int(json_data.get("major", 0)),
                minor=int(json_data.get("minor", 0)),
                build=int(json_data.get("build", 0)),
                environment=str(json_data.get("environment", "unknown")),
                sha=str(json_data.get("sha", ""))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse service version data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing service version data: {e}")