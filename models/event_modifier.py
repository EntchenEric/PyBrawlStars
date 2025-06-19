from enum import Enum


class EventModifier(Enum):
    """
    Represents possible event modifiers in Brawl Stars.

    Attributes:
        UNKNOWN: Unknown modifier.
        NONE: No modifier.
        ENERGY_DRINK: Energy Drink modifier.
        ANGRY_ROBO: Angry Robo modifier.
        METEOR_SHOWER: Meteor Shower modifier.
        GRAVEYARD_SHIFT: Graveyard Shift modifier.
        HEALING_MUSHROOMS: Healing Mushrooms modifier.
        BOSS_FIGHT_ROCKETS: Boss Fight Rockets modifier.
        TAKEDOWN_LASERS: Takedown Lasers modifier.
        TAKEDOWN_CHAIN_LIGHTNING: Takedown Chain Lightning modifier.
        TAKEDOWN_ROCKETS: Takedown Rockets modifier.
        WAVES: Waves modifier.
        HAUNTED_BALL: Haunted Ball modifier.
        SUPER_CHARGE: Super Charge modifier.
        FAST_BRAWLERS: Fast Brawlers modifier.
        SHOWDOWN_PLUS: Showdown+ modifier.
        PEEK_A_BOO: Peek A Boo modifier.
        BURNING_BALL: Burning Ball modifier.
    """

    UNKNOWN = "unknown"
    NONE = "none"
    ENERGY_DRINK = "energyDrink"
    ANGRY_ROBO = "angryRobo"
    METEOR_SHOWER = "meteorShower"
    GRAVEYARD_SHIFT = "graveyardShift"
    HEALING_MUSHROOMS = "healingMushrooms"
    BOSS_FIGHT_ROCKETS = "bossFightRockets"
    TAKEDOWN_LASERS = "takedownLasers"
    TAKEDOWN_CHAIN_LIGHTNING = "takedownChainLightning"
    TAKEDOWN_ROCKETS = "takedownRockets"
    WAVES = "waves"
    HAUNTED_BALL = "hauntedBall"
    SUPER_CHARGE = "superCharge"
    FAST_BRAWLERS = "fastBrawlers"
    SHOWDOWN_PLUS = "showdown+"
    PEEK_A_BOO = "peekABoo"
    BURNING_BALL = "burningBall"
