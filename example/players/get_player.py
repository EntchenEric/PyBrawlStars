from pybrawlstars import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    player = await client.get_player("2qquclvll")
    
    print(player)

    print(player.trophies)
    print(player.tag)
    print(player.club)

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())