import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from client import BSClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = BSClient(os.getenv("key"))

    club = await client.get_club("2L90CG289")
    
    print(club.name)
    print(club.description)

    for member in club.members:
        print(member.role.name.lower())
        print(member.name)

    await client.close() # Its recommended to close the Client when no longer needed.

if __name__ == "__main__":
    asyncio.run(main())