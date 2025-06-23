"""
PyBrawlStars - An asynchronous Python API wrapper for the Brawl Stars API

A modern, async-first Python library for interacting with the Brawl Stars API.
Provides easy access to player statistics, club information, battle logs, and more.
"""

from .client import BSClient
from .models.errors.api_error import APIError  
from .models.errors.network_error import NetworkError
from .models.errors.client_error import ClientError

# Game-related models
from .models.event import Event
from .models.game_mode import GameMode
from .models.match import Match
from .models.match_team import MatchTeam
from .models.match_team_player import MatchTeamPlayer

# Player-related models
from .models.player_club import PlayerClub
from .models.player_entry import PlayerEntry
from .models.player_entry_completed_game import PlayerEntryCompletedGame
from .models.player_icon import PlayerIcon
from .models.player_match_status import PlayerMatchStatus
from .models.player_ranking import PlayerRanking
from .models.player_ranking_club import PlayerRankingClub

# Club-related models
from .models.club_ranking import ClubRanking
from .models.club_role import ClubRole
from .models.club_type import ClubType

# Brawler-related models
from .models.brawler_info import BrawlerInfo
from .models.brawler_stat import BrawlerStat
from .models.star_power import StarPower
from .models.accessory import Accessory
from .models.gear_stat import GearStat

# Battle-related models
from .models.battle_region import BattleRegion
from .models.battle_result import BattleResult
from .models.banned_brawler_entry import BannedBrawlerEntry
from .models.completed_game import CompletedGame
from .models.completed_game_team import CompletedGameTeam

# Game mechanics models
from .models.event_modifier import EventModifier
from .models.game_info import GameInfo
from .models.game_phase import GamePhase
from .models.match_location import MatchLocation
from .models.match_mode import MatchMode
from .models.match_state import MatchState
from .models.register_match_request import RegisterMatchRequest
from .models.register_match_response import RegisterMatchResponse
from .models.service_version import ServiceVersion
from .models.siege_stats import SiegeStats
from .models.stats import Stats
from .models.termination_reason import TerminationReason
from .models.timer_preset import TimerPreset

__version__ = "1.0.6"
__author__ = "EntchenEic"
__license__ = "MIT"

__all__ = [
    "BSClient",
    "APIError",
    "NetworkError", 
    "ClientError",

        # Core models
    "Player",
    "Club", 
    "ClubMember",
    "Brawler",
    "Battle",
    "ScheduledEvent",
    
    # Game-related models
    "Event",
    "GameMode",
    "Match",
    "MatchTeam",
    "MatchTeamPlayer",
    
    # Player-related models
    "PlayerClub",
    "PlayerEntry",
    "PlayerEntryCompletedGame",
    "PlayerIcon",
    "PlayerMatchStatus",
    "PlayerRanking",
    "PlayerRankingClub",
    
    # Club-related models
    "ClubRanking",
    "ClubRole",
    "ClubType",
    
    # Brawler-related models
    "BrawlerInfo",
    "BrawlerStat",
    "StarPower",
    "Accessory",
    "GearStat",
    
    # Battle-related models
    "BattleRegion",
    "BattleResult",
    "BannedBrawlerEntry",
    "CompletedGame",
    "CompletedGameTeam",
    
    # Game mechanics models
    "EventModifier",
    "GameInfo",
    "GamePhase",
    "MatchLocation",
    "MatchMode",
    "MatchState",
    "RegisterMatchRequest",
    "RegisterMatchResponse",
    "ServiceVersion",
    "SiegeStats",
    "Stats",
    "TerminationReason",
    "TimerPreset",
]