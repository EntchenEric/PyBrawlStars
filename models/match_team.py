from models.match_team_player import MatchTeamPlayer
from models.brawler_info import BrawlerInfo

class MatchTeam:
    players: list[MatchTeamPlayer]
    bans: list[BrawlerInfo]
    side: int