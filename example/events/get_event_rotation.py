import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from client import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    event_rotation = await client.get_event_rotation()
    
    for event in event_rotation:
        print(event.map_name)
        print(event.mode.name.lower())

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())