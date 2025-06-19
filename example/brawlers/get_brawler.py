import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from client import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    brawler = await client.get_brawler(16000086)

    print(brawler.name)
    print(brawler.id)
    for gadget in brawler.gadgets:
        print(gadget.name)
    
    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())