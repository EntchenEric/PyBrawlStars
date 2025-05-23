from enum import Enum

class GamePhase(Enum):
    INIT = "init"
    BAN_HEROES = "banHeroes"
    PICK_HEROES = "pickHeroes"
    FINAL_PREPERATION = "finalPreperation"
    BATTLE = "battle"
    MATCH_RESULT = "matchResult"
    ENDING = "ending"