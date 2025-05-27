from client import BSClient

import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    player = await client.get_player("2qquclvll")
    print(player)

    await client.close() # make sure to close the client when finished

asyncio.run(main())