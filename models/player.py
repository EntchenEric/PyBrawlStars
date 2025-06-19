from models.parse_error import ParseException
from models.player_club import PlayerClub
from models.player_icon import PlayerIcon
from models.brawler import Brawler
from models.club import Club
from typing import Any, TYPE_CHECKING, List, Optional
if TYPE_CHECKING:
    from client import BSClient
        
class Player:
    """
    Represents a player in the game.

    Attributes:
        club: The player's club information.
        icon: The player's icon.
        tag: The player's unique tag.
        name: The player's name.
        trophies: The player's total trophies.
        exp_level: The player's experience level.
        exp_points: The player's experience points.
        highest_trophies: The player's highest trophy count.
        power_play_points: The player's power play points.
        highest_power_play_points: The player's highest power play points.
        brawlers: List of the player's brawlers.
        duo_victories: Number of duo victories.
        solo_victories: Number of solo victories.
        trio_victories: Number of 3v3 victories.
        best_robo_rumble_time: Best time in Robo Rumble.
        best_time_as_big_brawler: Best time as Big Brawler.
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

    brawlers: list[Brawler]
    """A list of `Brawler` objects, representing the player's brawlers and their stats."""

    name_color: str
    """The hexadecimal color code for the player's name (e.g., '0xffc03aff')."""

    client: "BSClient"
    """The brawlstars Client."""

    power_play_points: int
    """The player's power play points."""

    highest_power_play_points: int
    """The player's highest power play points."""

    trio_victories: int
    """The total number of 3v3 victories. Defaults to 0."""

    def __init__(
        self,
        client: "BSClient",
        club: PlayerClub | None,
        is_qualified_from_championship_challenge: bool,
        three_vs_three_victories: int,
        icon: PlayerIcon,
        tag: str,
        name: str,
        trophies: int,
        exp_level: int,
        exp_points: int,
        highest_trophies: int,
        power_play_points: int,
        highest_power_play_points: int,
        brawlers: list[Brawler],
        duo_victories: int,
        solo_victories: int,
        trio_victories: int,
        best_robo_rumble_time: int,
        best_time_as_big_brawler: int,
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
            power_play_points: The player's power play points.
            highest_power_play_points: The player's highest power play points.
            brawlers: List of player's brawlers with their stats.
            duo_victories: Total duo Showdown wins.
            solo_victories: Total solo Showdown wins.
            trio_victories: Total 3v3 wins.
            best_robo_rumble_time: Best Robo Rumble score/time.
            best_time_as_big_brawler: Best time as Big Brawler.
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
        self.power_play_points = power_play_points
        self.highest_power_play_points = highest_power_play_points
        self.brawlers = brawlers
        self.duo_victories = duo_victories
        self.solo_victories = solo_victories
        self.trio_victories = trio_victories
        self.best_robo_rumble_time = best_robo_rumble_time
        self.best_time_as_big_brawler = best_time_as_big_brawler
        self.name_color = name_color

    def __str__(self) -> str:
        """
        Returns the string representation of the player.

        Returns:
            The player's name.
        """
        club_str = f" [{self.club.name}]" if self.club else ""
        return f"{self.name}{club_str} ({self.tag}) - {self.trophies} trophies"

    async def fetch_club(self) -> Club | None:
        await self.client.get_club(self.club.tag)

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Player":
        """
        Creates a Player instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Player: A new Player instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player data, got {type(json_data)}")

        try:
            club_data = json_data.get("club")
            club = PlayerClub.from_json(club_data, client) if isinstance(club_data, dict) else None

            icon_data = json_data.get("icon")
            if not isinstance(icon_data, dict):
                raise ParseException(f"Expected 'icon' to be a dictionary, got {type(icon_data)}")
            icon = PlayerIcon.from_json(icon_data, client)

            brawlers_data = json_data.get("brawlers", [])
            if not isinstance(brawlers_data, list):
                raise ParseException(f"Expected 'brawlers' to be a list, got {type(brawlers_data)}")
            brawlers = [Brawler.from_json(b, client) for b in brawlers_data if isinstance(b, dict)]

            return Player(
                client=client,
                club=club,
                is_qualified_from_championship_challenge=bool(json_data.get(
                    "isQualifiedFromChampionshipChallenge", False
                )),
                three_vs_three_victories=int(json_data.get("3vs3Victories", 0)),
                icon=icon,
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "N/A")),
                trophies=int(json_data.get("trophies", 0)),
                exp_level=int(json_data.get("expLevel", 0)),
                exp_points=int(json_data.get("expPoints", 0)),
                highest_trophies=int(json_data.get("highestTrophies", 0)),
                power_play_points=int(json_data.get("powerPlayPoints", 0)),
                highest_power_play_points=int(json_data.get("highestPowerPlayPoints", 0)),
                brawlers=brawlers,
                duo_victories=int(json_data.get("duoVictories", 0)),
                solo_victories=int(json_data.get("soloVictories", 0)),
                trio_victories=int(json_data.get("3vs3Victories", 0)),
                best_robo_rumble_time=int(json_data.get("bestRoboRumbleTime", 0)),
                best_time_as_big_brawler=int(json_data.get("bestTimeAsBigBrawler", 0)),
                name_color=str(json_data.get("nameColor", "0x00000000")),
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player data: {e}")