from models.parse_error import ParseException
from models.player_club import PlayerClub, from_json as player_club_from_json
from models.player_icon import PlayerIcon, from_json as player_icon_from_json
from models.brawler_stat import BrawlerStat, from_json as brawler_stat_from_json
from models.club import Club
from client import BSClient
from typing import Any 

class Player:
    """
    Represents a player in the game.

    This class stores all relevant information about a player, including their
    club, stats, brawlers, and cosmetic details.
    """
    club: PlayerClub | None
    """The club the player is currently in, or None if not in a club."""

    is_qualified_from_championship_challenge: bool
    """Indicates if the player has qualified from the championship challenge."""

    three_vs_three_victories: int
    """Total number of 3vs3 victories. Defaults to 0."""

    icon: PlayerIcon
    """The player's selected icon object, containing icon ID and other details."""

    tag: str
    """The unique player tag (e.g., '#2qquclvll')."""

    name: str
    """The player's current in-game name."""

    trophies: int
    """The current number of trophies the player has."""

    exp_level: int
    """The player's current experience level."""

    exp_points: int
    """The total experience points the player has accumulated."""

    highest_trophies: int
    """The highest number of trophies the player has ever achieved."""

    solo_victories: int
    """The total number of solo Showdown victories. Defaults to 0."""

    duo_victories: int
    """The total number of duo Showdown victories. Defaults to 0."""

    best_robo_rumble_time: int
    """The player's best time in the Robo Rumble event, in seconds."""

    best_time_as_big_brawler: int
    """The player's best survival time as the Big Brawler in Big Game event, in seconds."""

    brawlers: list[BrawlerStat]
    """A list of `BrawlerStat` objects, representing the player's brawlers and their stats."""

    name_color: str
    """The hexadecimal color code for the player's name (e.g., '0xffc03aff')."""

    client: BSClient
    """The brawlstars Client."""

    def __init__(
        self,
        client: BSClient,
        club: PlayerClub | None,
        is_qualified_from_championship_challenge: bool,
        three_vs_three_victories: int, # Corrected type
        icon: PlayerIcon,
        tag: str,
        name: str,
        trophies: int,
        exp_level: int,
        exp_points: int,
        highest_trophies: int,
        solo_victories: int,
        duo_victories: int,
        best_robo_rumble_time: int,
        best_time_as_big_brawler: int,
        brawlers: list[BrawlerStat],
        name_color: str,
    ):
        """
        Initializes a new Player instance.

        Args:
            club: The player's club, or None.
            is_qualified_from_championship_challenge: Qualification status.
            three_vs_three_victories: Total 3vs3 wins.
            icon: The player's icon.
            tag: The player's unique tag.
            name: The player's name.
            trophies: Current trophy count.
            exp_level: Current experience level.
            exp_points: Total experience points.
            highest_trophies: Highest ever trophy count.
            solo_victories: Total solo Showdown wins.
            duo_victories: Total duo Showdown wins.
            best_robo_rumble_time: Best Robo Rumble score/time.
            best_time_as_big_brawler: Best time as Big Brawler.
            brawlers: List of player's brawlers with their stats.
            name_color: Hex color code for the player's name.
        """
        self.client = client
        self.club = club
        self.is_qualified_from_championship_challenge = is_qualified_from_championship_challenge
        self.three_vs_three_victories = three_vs_three_victories
        self.icon = icon
        self.tag = tag
        self.name = name
        self.trophies = trophies
        self.exp_level = exp_level
        self.exp_points = exp_points
        self.highest_trophies = highest_trophies
        self.solo_victories = solo_victories
        self.duo_victories = duo_victories
        self.best_robo_rumble_time = best_robo_rumble_time
        self.best_time_as_big_brawler = best_time_as_big_brawler
        self.brawlers = brawlers
        self.name_color = name_color

    def __str__(self) -> str:
        """
        Returns the string representation of the player.

        Returns:
            The player's name.
        """
        return self.name

    async def fetch_club(self) -> Club | None:
        await self.client.get_club(self.club.tag)


def from_json(json_data: dict[str, Any], client: BSClient) -> Player:
    """
    Parses a JSON dictionary and creates a Player object.

    Args:
        json_data: A dictionary containing player data, typically from an API response.
                   The dictionary can have varied value types, not just strings.

    Returns:
        A Player object initialized with data from the JSON.

    Raises:
        ParseException: If an error occurs during parsing of the player data
                        or any of its nested objects (club, icon, brawlers).
    """
    if not isinstance(json_data, dict):
        raise ParseException(f"Expected a dictionary for player data, got {type(json_data)}")

    try:
        client = client
        club_data = json_data.get("club")
        player_club = player_club_from_json(club_data) if club_data else None

        icon_data = json_data.get("icon")
        if icon_data is None:
            raise ParseException("Missing 'icon' data in player JSON.")
        player_icon_obj = player_icon_from_json(icon_data)

        brawlers_data = json_data.get("brawlers", [])
        parsed_brawlers = [
            brawler_stat_from_json(brawler) for brawler in brawlers_data if isinstance(brawler, dict)
        ]

        return Player(
            club=player_club,
            is_qualified_from_championship_challenge=bool(json_data.get(
                "isQualifiedFromChampionshipChallenge", False
            )),
            three_vs_three_victories=int(json_data.get("3vs3Victories", 0)),
            icon=player_icon_obj,
            tag=str(json_data.get("tag", "")),
            name=str(json_data.get("name", "N/A")),
            trophies=int(json_data.get("trophies", 0)),
            exp_level=int(json_data.get("expLevel", 0)),
            exp_points=int(json_data.get("expPoints", 0)),
            highest_trophies=int(json_data.get("highestTrophies", 0)),
            solo_victories=int(json_data.get("soloVictories", 0)),
            duo_victories=int(json_data.get("duoVictories", 0)),
            best_robo_rumble_time=int(json_data.get("bestRoboRumbleTime", 0)),
            best_time_as_big_brawler=int(json_data.get("bestTimeAsBigBrawler", 0)),
            brawlers=parsed_brawlers,
            name_color=str(json_data.get("nameColor", "0x00000000")),
        )
    except (TypeError, ValueError, KeyError) as e:
        raise ParseException(f"Failed to parse player data: {e}. Input: {json_data}")
    except ParseException:
        raise
    except Exception as e:
        raise ParseException(f"An unexpected error occurred while parsing player data: {e}")