from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Stats:
    """
    Represents statistics from a game or battle.

    Attributes:
        objectives_stolen: Number of objectives stolen.
        brawl_ball_shots_on_goal: Number of shots on goal in Brawl Ball.
        brawl_ball_shots_saved: Number of shots saved in Brawl Ball.
        healing_done: Total healing done.
        damage_dealt: Total damage dealt.
        average_latency: Average latency during the game.
        damage_received: Total damage received.
        kills: Number of kills.
        deaths: Number of deaths.
        total_damage_to_safe: Total damage dealt to the safe.
        total_damage_to_pets: Total damage dealt to pets.
        siege_damage_to_robot: Damage dealt to siege robots.
        siege_bolts_collected: Number of siege bolts collected.
        brawl_ball_goals_scored: Number of goals scored in Brawl Ball.
        gem_grab_gems_collected: Number of gems collected in Gem Grab.
        gem_grab_gems_lost: Number of gems lost in Gem Grab.
        bounty_stars_gained: Number of bounty stars gained.
        bounty_stars_lost: Number of bounty stars lost.
        super_used_count: Number of times super was used.
        gadget_used_count: Number of times gadget was used.
        bounty_picked_middle_star: Number of middle stars picked in Bounty.
        match_end_kill_streak: Kill streak at the end of the match.
        max_kill_streak: Maximum kill streak achieved.
        hot_zone_inside_zone_percentage: Percentage of time spent inside hot zone.
        healing_done_to_self: Amount of self-healing done.
        healing_done_to_team_mates: Amount of healing done to teammates.
        objectives_recovered: Number of objectives recovered.
    """
    def __init__(
        self,
        objectives_stolen: int = 0,
        brawl_ball_shots_on_goal: int = 0,
        brawl_ball_shots_saved: int = 0,
        healing_done: int = 0,
        damage_dealt: int = 0,
        average_latency: int = 0,
        damage_received: int = 0,
        kills: int = 0,
        deaths: int = 0,
        total_damage_to_safe: int = 0,
        total_damage_to_pets: int = 0,
        siege_damage_to_robot: int = 0,
        siege_bolts_collected: int = 0,
        brawl_ball_goals_scored: int = 0,
        gem_grab_gems_collected: int = 0,
        gem_grab_gems_lost: int = 0,
        bounty_stars_gained: int = 0,
        bounty_stars_lost: int = 0,
        super_used_count: int = 0,
        gadget_used_count: int = 0,
        bounty_picked_middle_star: int = 0,
        match_end_kill_streak: int = 0,
        max_kill_streak: int = 0,
        hot_zone_inside_zone_percentage: int = 0,
        healing_done_to_self: int = 0,
        healing_done_to_team_mates: int = 0,
        objectives_recovered: int = 0
    ):
        """
        Initialize a new Stats instance.

        All parameters default to 0 if not provided.
        """
        self.objectives_stolen = objectives_stolen
        self.brawl_ball_shots_on_goal = brawl_ball_shots_on_goal
        self.brawl_ball_shots_saved = brawl_ball_shots_saved
        self.healing_done = healing_done
        self.damage_dealt = damage_dealt
        self.average_latency = average_latency
        self.damage_received = damage_received
        self.kills = kills
        self.deaths = deaths
        self.total_damage_to_safe = total_damage_to_safe
        self.total_damage_to_pets = total_damage_to_pets
        self.siege_damage_to_robot = siege_damage_to_robot
        self.siege_bolts_collected = siege_bolts_collected
        self.brawl_ball_goals_scored = brawl_ball_goals_scored
        self.gem_grab_gems_collected = gem_grab_gems_collected
        self.gem_grab_gems_lost = gem_grab_gems_lost
        self.bounty_stars_gained = bounty_stars_gained
        self.bounty_stars_lost = bounty_stars_lost
        self.super_used_count = super_used_count
        self.gadget_used_count = gadget_used_count
        self.bounty_picked_middle_star = bounty_picked_middle_star
        self.match_end_kill_streak = match_end_kill_streak
        self.max_kill_streak = max_kill_streak
        self.hot_zone_inside_zone_percentage = hot_zone_inside_zone_percentage
        self.healing_done_to_self = healing_done_to_self
        self.healing_done_to_team_mates = healing_done_to_team_mates
        self.objectives_recovered = objectives_recovered

    def __str__(self) -> str:
        """
        Returns the string representation of the stats.

        Returns:
            str: A summary of the most important stats.
        """
        return (
            f"Kills: {self.kills}, Deaths: {self.deaths}, "
            f"Damage Dealt: {self.damage_dealt}, Damage Received: {self.damage_received}, "
            f"Healing Done: {self.healing_done}"
        )

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Stats":
        """
        Creates a Stats instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Stats: A new Stats instance.

        Raises:
            ParseException: If the JSON data is invalid.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for stats data, got {type(json_data)}")

        try:
            return Stats(
                objectives_stolen=int(json_data.get("objectivesStolen", 0)),
                brawl_ball_shots_on_goal=int(json_data.get("brawlBallShotsOnGoal", 0)),
                brawl_ball_shots_saved=int(json_data.get("brawlBallShotsSaved", 0)),
                healing_done=int(json_data.get("healingDone", 0)),
                damage_dealt=int(json_data.get("damageDealt", 0)),
                average_latency=int(json_data.get("averageLatency", 0)),
                damage_received=int(json_data.get("damageReceived", 0)),
                kills=int(json_data.get("kills", 0)),
                deaths=int(json_data.get("deaths", 0)),
                total_damage_to_safe=int(json_data.get("totalDamageToSafe", 0)),
                total_damage_to_pets=int(json_data.get("totalDamageToPets", 0)),
                siege_damage_to_robot=int(json_data.get("siegeDamageToRobot", 0)),
                siege_bolts_collected=int(json_data.get("siegeBoltsCollected", 0)),
                brawl_ball_goals_scored=int(json_data.get("brawlBallGoalsScored", 0)),
                gem_grab_gems_collected=int(json_data.get("gemGrabGemsCollected", 0)),
                gem_grab_gems_lost=int(json_data.get("gemGrabGemsLost", 0)),
                bounty_stars_gained=int(json_data.get("bountyStarsGained", 0)),
                bounty_stars_lost=int(json_data.get("bountyStarsLost", 0)),
                super_used_count=int(json_data.get("superUsedCount", 0)),
                gadget_used_count=int(json_data.get("gadgetUsedCount", 0)),
                bounty_picked_middle_star=int(json_data.get("bountyPickedMiddleStar", 0)),
                match_end_kill_streak=int(json_data.get("matchEndKillStreak", 0)),
                max_kill_streak=int(json_data.get("maxKillStreak", 0)),
                hot_zone_inside_zone_percentage=int(json_data.get("hotZoneInsideZonePercentage", 0)),
                healing_done_to_self=int(json_data.get("healingDoneToSelf", 0)),
                healing_done_to_team_mates=int(json_data.get("healingDoneToTeamMates", 0)),
                objectives_recovered=int(json_data.get("objectivesRecovered", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse stats data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing stats data: {e}")