import asyncio
import httpx
from typing import Any, Callable, Type, TypeVar, List
from .models.errors.client_error import ClientError
from .models.errors.network_error import NetworkError
from .models.errors.api_error import APIError
from .models.battle import Battle
from .models.player import Player
from .models.club_member import ClubMember
from .models.club import Club
from .models.brawler import Brawler
from .models.scheduled_event import ScheduledEvent
from .utility import parse_tag

T = TypeVar("T")


class BSClient:
    """
    An asynchronous client for the Brawl Stars API.

    Manages a persistent HTTP session for efficient and reliable requests.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.brawlstars.com",
        version: int = 1,
        timeout: int = 10,
    ):
        if not api_key:
            raise ValueError("API key must be provided and cannot be empty.")

        self._base_url = f"{base_url}/v{version}"
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._timeout = httpx.Timeout(timeout)

        self._session: httpx.AsyncClient | None = None

    @property
    def _lazy_session(self) -> httpx.AsyncClient:
        """Lazily initializes and returns the httpx.AsyncClient session."""
        if self._session is None or self._session.is_closed:
            self._session = httpx.AsyncClient(
                base_url=self._base_url, headers=self._headers, timeout=self._timeout
            )
        return self._session

    async def _make_request(
        self, method: str, endpoint: str, response_parser: Callable[[Any], T]
    ) -> T:
        """
        A generic method to make API requests and handle responses.

        Args:
            method: HTTP method (e.g., "GET").
            endpoint: API endpoint path (e.g., "/players/...").
            response_parser: The function to parse the JSON response into a data model.

        Raises:
            TimeoutError: If the request times out.
            NetworkError: For connection or other network issues.
            APIError: For any non-2xx API response.

        Returns:
            The parsed data model instance.
        """
        try:
            response = await self._lazy_session.request(method, endpoint)

            response.raise_for_status()

            return response_parser(response.json())

        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {e.request.url}") from e
        except httpx.NetworkError as e:
            raise NetworkError(f"Network error occurred: {e.request.url}") from e
        except httpx.HTTPStatusError as e:
            error_json = e.response.json() if e.response.content else None
            raise APIError(
                status_code=e.response.status_code, error_json=error_json,
            ) from e

    async def get_player_battlelog(self, tag: str) -> List[Battle]:
        """
        Fetches the battle log of a Player. It may take up to 30 minutes for a new battle to appear in the battlelog.

        Raises:
            APIError: If the player is not found or another API error occurs.
            ValueError: If the tag is invalid.
        """
        parsed_tag = parse_tag(tag=tag)
        if not parsed_tag:
            raise ValueError("The provided tag is invalid or empty after parsing.")

        return await self._make_request(
            method="GET",
            endpoint=f"/players/{parsed_tag}/battlelog",
            response_parser=lambda json_data: [
                Battle.from_json(battle_json, self)
                for battle_json in json_data["items"]
            ],
        )

    async def get_player(self, tag: str) -> Player:
        """
        Fetches a player by their tag.

        Raises:
            APIError: If the player is not found or another API error occurs.
            ValueError: If the tag is invalid.
        """
        parsed_tag = parse_tag(tag=tag)
        if not parsed_tag:
            raise ValueError("The provided tag is invalid or empty after parsing.")

        return await self._make_request(
            method="GET",
            endpoint=f"/players/{parsed_tag}",
            response_parser=lambda json_data: Player.from_json(json_data, self),
        )

    async def get_club_members(self, tag: str) -> List[ClubMember]:
        """
        Fetches the Members of a Club by its tag.

        Raises:
            APIError: If the player is not found or another API error occurs.
            ValueError: If the tag is invalid.
        """
        parsed_tag = parse_tag(tag=tag)
        if not parsed_tag:
            raise ValueError("The provided tag is invalid or empty after parsing.")

        return await self._make_request(
            method="GET",
            endpoint=f"/clubs/{parsed_tag}/members",
            response_parser=lambda json_data: [
                ClubMember.from_json(club_member_json, self)
                for club_member_json in json_data["items"]
            ],
        )


    async def get_club(self, tag: str) -> Club:
        """
        Fetches a club by its tag.

        Raises:
            APIError: If the club is not found or another API error occurs.
            ValueError: If the tag is invalid.
        """
        parsed_tag = parse_tag(tag=tag)
        if not parsed_tag:
            raise ValueError("The provided tag is invalid or empty after parsing.")

        return await self._make_request(
            method="GET",
            endpoint=f"/clubs/{parsed_tag}",
            response_parser=lambda json_data: Club.from_json(json_data, self),
        )
    
    async def get_brawlers(self) -> List[Brawler]:
        """
        Fetches a List of all Brawlers in the game.

        Raises:
            APIError: If the club is not found or another API error occurs.
        """
        return await self._make_request(
            method="GET",
            endpoint=f"/brawlers",
            response_parser=lambda json_data: [
                Brawler.from_json(brawler_json, self)
                for brawler_json in json_data["items"]
            ],
        )
    
    async def get_brawler(self, id: int) -> Brawler:
        """
        Fetches a List of all Brawlers in the game.

        Raises:
            APIError: If the club is not found or another API error occurs.
        """
        return await self._make_request(
            method="GET",
            endpoint=f"/brawlers/{id}",
            response_parser=lambda json_data: Brawler.from_json(json_data, self)
        )

    async def get_event_rotation(self) -> List[ScheduledEvent]:
        """
        Fetches a List of all scheduled events of the game.

        Raises:
            APIError: If the club is not found or another API error occurs.
        """
        return await self._make_request(
            method="GET",
            endpoint=f"/events/rotation",
            response_parser=lambda json_data: [
                ScheduledEvent.from_json(event_json, self)
                for event_json in json_data
            ],
        )

    async def close(self):
        """Closes the underlying HTTP session. Recommended to be called on application shutdown."""
        if self._session and not self._session.is_closed:
            await self._session.aclose()

    async def __aenter__(self):
        """Async context manager entry point."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit point. Closes the session."""
        await self.close()
