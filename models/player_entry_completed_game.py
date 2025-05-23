from models.brawler_info import BrawlerInfo
from models.stats import Stats

class PlayerEntryCompletedGame:
    brawler: BrawlerInfo
    statistics: Stats
    tag: str
    account_id: str