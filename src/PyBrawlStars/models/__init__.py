"""
PyBrawlStars Models

All data models for the PyBrawlStars library.
"""

# Core models
from .player import Player
from .club import Club
from .club_member import ClubMember
from .brawler import Brawler
from .battle import Battle
from .scheduled_event import ScheduledEvent

# Game-related models
from .event import Event
from .game_mode import GameMode
from .match import Match
from .match_team import MatchTeam
from .match_team_player import MatchTeamPlayer

# Player-related models
from .player_club import PlayerClub
from .player_entry import PlayerEntry
from .player_entry_completed_game import PlayerEntryCompletedGame
from .player_icon import PlayerIcon
from .player_match_status import PlayerMatchStatus
from .player_ranking import PlayerRanking
from .player_ranking_club import PlayerRankingClub

# Club-related models
from .club_ranking import ClubRanking
from .club_role import ClubRole
from .club_type import ClubType

# Brawler-related models
from .brawler_info import BrawlerInfo
from .brawler_stat import BrawlerStat
from .star_power import StarPower
from .accessory import Accessory
from .gear_stat import GearStat

# Battle-related models
from .battle_region import BattleRegion
from .battle_result import BattleResult
from .battle_player import BattlePlayer
from .battle_brawler import BattleBrawler
from .banned_brawler_entry import BannedBrawlerEntry
from .completed_game import CompletedGame
from .completed_game_team import CompletedGameTeam

# Game mechanics models
from .event_modifier import EventModifier
from .game_info import GameInfo
from .game_phase import GamePhase
from .match_location import MatchLocation
from .match_mode import MatchMode
from .match_state import MatchState
from .register_match_request import RegisterMatchRequest
from .register_match_response import RegisterMatchResponse
from .service_version import ServiceVersion
from .siege_stats import SiegeStats
from .stats import Stats
from .termination_reason import TerminationReason
from .timer_preset import TimerPreset

# Error models
from .errors import APIError, NetworkError, ClientError

__all__ = [
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
    "BattlePlayer",
    "BattleBrawler",
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
    
    # Error models
    "APIError",
    "NetworkError", 
    "ClientError",
]
