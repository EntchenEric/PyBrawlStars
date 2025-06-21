import os
from pybrawlstars import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    events = await client.get_event_rotation()
    
    for event in events:
        print(event.event.mode)
        print(event.start_time)
        print(event.end_time)

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())