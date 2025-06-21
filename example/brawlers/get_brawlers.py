from pybrawlstars import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    brawlers = await client.get_brawlers()
    
    for brawler in brawlers:
        print(brawler.name)
        print(brawler.id)
        for star_power in brawler.star_powers:
            print(star_power.name.lower())

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())