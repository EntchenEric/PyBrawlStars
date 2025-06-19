import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from client import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    battlelog = await client.get_player_battlelog("2qquclvll")
    
    for battle in battlelog:
        print(battle.battle_result.trophy_change)

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())