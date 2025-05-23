from models.brawler_info import BrawlerInfo

class PlayerMatchStatus:
    brawler: BrawlerInfo
    is_ready: bool
    is_in_battle: bool
    is_online: bool
    has_joined: bool
    tag: str