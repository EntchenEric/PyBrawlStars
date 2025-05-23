from models.player_ranking_club import PlayerRankingClub
from models.player_icon import PlayerIcon

class PlayerRanking:
    club: PlayerRankingClub
    trophies: int
    icon: PlayerIcon
    tag: str
    name: str
    rank: int
    nameColor: str