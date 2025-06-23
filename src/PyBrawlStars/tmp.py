from client import BSClient
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    battlelog = await client.get_player_battlelog("2qquclvll")
    
    for battle in battlelog:
        print(battle.battle_result.trophy_change)
        print(battle.battle_result.star_player.name)
        print(battle.battle_result.star_player.brawler.name)
        print(battle.battle_result.star_player.brawler.power)

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())