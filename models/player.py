from models.placer_club import PlayerClub
from models.player_icon import PlayerIcon
from models.brawler_stat import BrawlerStat

class Player:
    club: PlayerClub
    is_qualified_from_championship_challenge: bool
    three_vs_three_victories: bool
    icon: PlayerIcon
    tag: str
    name: str
    trophies: int
    exp_level: int
    exp_points: int
    highest_trophies: int
    solo_victories: int
    duo_victories: int
    best_robo_rumble_time: int
    best_time_as_big_brawler: int
    brawlers: list[BrawlerStat]
    name_color: str