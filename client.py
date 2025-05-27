import asyncio
import aiohttp
from models.client_error import ClientError, from_json as client_error_from_json
from models.player import Player, from_json as player_from_json
from models.club import Club, from_json as club_from_json
from utility import parse_tag

class BSClient:
    api_key: str
    base_url: str
    version: int
    _session: aiohttp.ClientSession | None
    _headers: dict
    _is_closed: bool

    def __init__(self, api_key: str | None, base_url: str = "https://api.brawlstars.com", version: int = 1):
        if not api_key:
            raise ValueError("API key must be provided and cannot be empty.")

        self.api_key = api_key
        self.base_url = base_url
        self.version = version
        self._headers = {"Authorization": f"Bearer {self.api_key}"}
        self._session = None
        self._is_closed = True

    async def _ensure_session(self):
        """Ensures the session is active."""
        if self._is_closed or self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(headers=self._headers)
            self._is_closed = False

    async def get_player(self, tag: str) -> Player | ClientError:
        await self._ensure_session()
        if not self._session:
             raise RuntimeError("Session not available. This is an unexpected state.")

        parsed_tag = parse_tag(tag=tag)
        if len(parsed_tag) < 1:
            raise RuntimeError("The tag has to be at least on character long.")
        url = f"{self.base_url}/v{self.version}/players/{parsed_tag}"

        try:
            timeout = aiohttp.ClientTimeout(total=10)
            async with self._session.get(url, timeout=timeout) as response:
                
                if response.status == 200:
                    data = await response.json()
                    return player_from_json(data)
                else:
                    try:
                        data = await response.json()
                        return client_error_from_json(data)
                    except aiohttp.ContentTypeError:
                        error_text = await response.text()
                        return ClientError(message=f"API error: {response.status} - {error_text}", reason=str(response.status))

        except asyncio.TimeoutError:
            return ClientError(message="Request timed out", reason="Timeout")
        except aiohttp.ClientConnectorError as e:
            return ClientError(message=f"Connection error: {e}", reason="ConnectionError")
        except aiohttp.ClientError as e: # Catch other aiohttp client errors
            return ClientError(message=f"AIOHTTP error: {e}", reason="ClientError")

    async def get_club(self, tag: str) -> Club | ClientError:
        await self._ensure_session()
        if not self._session:
             raise RuntimeError("Session not available. This is an unexpected state.")

        parsed_tag = parse_tag(tag=tag)
        if len(parsed_tag) < 1:
            raise RuntimeError("The tag has to be at least on character long.")
        url = f"{self.base_url}/v{self.version}/players/{parsed_tag}"

        try:
            timeout = aiohttp.ClientTimeout(total=10)
            async with self._session.get(url, timeout=timeout) as response:
                
                if response.status == 200:
                    data = await response.json()
                    return player_from_json(data)
                else:
                    try:
                        data = await response.json()
                        return client_error_from_json(data)
                    except aiohttp.ContentTypeError:
                        error_text = await response.text()
                        return ClientError(message=f"API error: {response.status} - {error_text}", reason=str(response.status))

        except asyncio.TimeoutError:
            return ClientError(message="Request timed out", reason="Timeout")
        except aiohttp.ClientConnectorError as e:
            return ClientError(message=f"Connection error: {e}", reason="ConnectionError")
        except aiohttp.ClientError as e: # Catch other aiohttp client errors
            return ClientError(message=f"AIOHTTP error: {e}", reason="ClientError")

    async def close(self):
        """Closes the underlying aiohttp.ClientSession."""
        if self._session and not self._session.closed:
            await self._session.close()
        self._is_closed = True

    async def __aenter__(self):
        """Async context manager entry point. Ensures session is active."""
        await self._ensure_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit point. Closes the session."""
        await self.close()
