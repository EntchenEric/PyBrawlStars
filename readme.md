# PyBrawlStars

[![PyPI version](https://badge.fury.io/py/pybrawlstars.svg)](https://badge.fury.io/py/pybrawlstars)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![API](https://img.shields.io/badge/Brawl%20Stars%20API-v1-orange.svg)](https://developer.brawlstars.com)

An **asynchronous** Python API wrapper for the [Brawl Stars API](https://developer.brawlstars.com) that provides easy access to player statistics, club information, battle logs, and more.

## 🚀 Features

- **Fully Asynchronous**: Built with `httpx` for high-performance async operations
- **Type Hints**: Complete type annotations for better IDE support and code reliability
- **Comprehensive Models**: Rich data models for all Brawl Stars entities
- **Error Handling**: Proper exception handling with custom error types
- **Auto Tag Parsing**: Automatic handling of Brawl Stars player/club tags
- **Session Management**: Efficient HTTP session management with connection pooling
- **Rate Limiting Ready**: Built to handle API rate limits gracefully
- **Easy Installation**: Available on PyPI for simple pip installation

## 📦 Installation

Install the package from PyPI:

```bash
pip install pybrawlstars
```

## 🔑 Getting Started

### 1. Get Your API Key

First, obtain your API key from the [Brawl Stars Developer Portal](https://developer.brawlstars.com).

### 2. Basic Usage

```python
import asyncio
from pybrawlstars import BSClient

async def main():
    # Initialize the client with your API key
    client = BSClient("YOUR_API_KEY")
    
    try:
        # Get player information
        player = await client.get_player("2PPQVUQ8J")
        print(f"Player: {player.name}")
        print(f"Trophies: {player.trophies}")
        
        # Get club information
        club = await client.get_club("2L90CG289")
        print(f"Club: {club.name}")
        print(f"Members: {len(club.members)}")
        
    finally:
        # Always close the client when done
        await client.close()

# Run the async function
asyncio.run(main())
```

### 3. Using Context Manager (Recommended)

```python
import asyncio
from pybrawlstars import BSClient

async def main():
    async with BSClient("YOUR_API_KEY") as client:
        player = await client.get_player("2PPQVUQ8J")
        print(f"Player: {player.name}")
        # Client automatically closes when exiting the context

asyncio.run(main())
```

## 📚 API Reference

### BSClient

The main client class for interacting with the Brawl Stars API.

**Note**: Due to Brawl Stars API limitations, only the following 7 routes are supported:
- `get_player` - Get player profile
- `get_battlelog` - Get player battle log  
- `get_club` - Get club information
- `get_club_members` - Get club members
- `get_brawlers` - Get all brawlers
- `get_brawler` - Get specific brawler by ID
- `get_event_rotation` - Get current event rotation

#### Constructor

```python
BSClient(
    api_key: str,
    base_url: str = "https://api.brawlstars.com",
    version: int = 1,
    timeout: int = 10
)
```

#### Methods

##### Player Methods

```python
# Get player profile
await client.get_player(tag: str)

# Get player battle log
await client.get_battlelog(tag: str)
```

##### Club Methods

```python
# Get club information
await client.get_club(tag: str)

# Get club members
await client.get_club_members(tag: str)
```

##### Brawler Methods

```python
# Get all brawlers
await client.get_brawlers()

# Get specific brawler by ID
await client.get_brawler(id: int)
```

##### Event Methods

```python
# Get current event rotation
await client.get_event_rotation()
```

## 💡 Examples

### Get Player Statistics

```python
import asyncio
from pybrawlstars import BSClient

async def get_player_stats():
    async with BSClient("YOUR_API_KEY") as client:
        player = await client.get_player("PLAYER_TAG")
        
        print(f"🏆 {player.name}")
        print(f"Trophies: {player.trophies}")
        print(f"Experience Level: {player.exp_level}")
        print(f"3v3 Victories: {player.victories_3vs3}")
        print(f"Solo Victories: {player.solo_victories}")
        print(f"Duo Victories: {player.duo_victories}")
        
        if player.club:
            print(f"Club: {player.club.name}")

asyncio.run(get_player_stats())
```

### Analyze Club Members

```python
import asyncio
from pybrawlstars import BSClient

async def analyze_club():
    async with BSClient("YOUR_API_KEY") as client:
        club = await client.get_club("CLUB_TAG")
        
        print(f"📊 Club Analysis: {club.name}")
        print(f"Description: {club.description}")
        print(f"Total Members: {len(club.members)}")
        print(f"Required Trophies: {club.required_trophies}")
        
        # Group members by role
        roles = {}
        for member in club.members:
            role = member.role.name
            roles[role] = roles.get(role, 0) + 1
        
        print("\n👥 Member Roles:")
        for role, count in roles.items():
            print(f"  {role}: {count}")

asyncio.run(analyze_club())
```

### Track Battle History

```python
import asyncio
from pybrawlstars import BSClient

async def analyze_battles():
    async with BSClient("YOUR_API_KEY") as client:
        battles = await client.get_battlelog("PLAYER_TAG")
        
        wins = sum(1 for battle in battles if battle.battle.result == "victory")
        total = len(battles)
        win_rate = (wins / total) * 100 if total > 0 else 0
        
        print(f"⚔️ Recent Battle Performance")
        print(f"Total Battles: {total}")
        print(f"Victories: {wins}")
        print(f"Win Rate: {win_rate:.1f}%")
        
        # Analyze game modes
        modes = {}
        for battle in battles:
            mode = battle.event.mode
            modes[mode] = modes.get(mode, 0) + 1
        
        print("\n🎮 Game Modes Played:")
        for mode, count in sorted(modes.items(), key=lambda x: x[1], reverse=True):
            print(f"  {mode}: {count} battles")

asyncio.run(analyze_battles())
```

### Browse All Brawlers

```python
import asyncio
from pybrawlstars import BSClient

async def list_brawlers():
    async with BSClient("YOUR_API_KEY") as client:
        brawlers = await client.get_brawlers()
        
        print(f"🤖 Available Brawlers ({len(brawlers)}):")
        
        for brawler in sorted(brawlers, key=lambda b: b.name):
            print(f"\n{brawler.name} (ID: {brawler.id})")
            
            if brawler.star_powers:
                print("  Star Powers:")
                for sp in brawler.star_powers:
                    print(f"    - {sp.name}")
            
            if brawler.gadgets:
                print("  Gadgets:")
                for gadget in brawler.gadgets:
                    print(f"    - {gadget.name}")

asyncio.run(list_brawlers())
```

## 🏗️ Data Models

The library provides rich data models for all API responses:

- **Player**: Complete player profile with statistics and brawler progression
- **Club**: Club information including members and settings
- **Battle**: Individual battle results with participants and outcomes
- **Brawler**: Brawler information including star powers and gadgets
- **Event**: Current and upcoming game events
- **And many more!** Explore all available models in the library

## ⚠️ Error Handling

The library provides specific exception types for different error scenarios:

```python
import asyncio
from pybrawlstars import BSClient
from pybrawlstars.models.errors import APIError, NetworkError, ClientError

async def safe_api_call():
    async with BSClient("YOUR_API_KEY") as client:
        try:
            player = await client.get_player("INVALID_TAG")
        except APIError as e:
            print(f"API Error {e.status_code}: {e.message}")
        except NetworkError as e:
            print(f"Network Error: {e}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except TimeoutError as e:
            print(f"Request timed out: {e}")

asyncio.run(safe_api_call())
```

## 🏷️ Tag Formats

Player and club tags can be provided in multiple formats:
- With hashtag: `#2PPQVUQ8J`
- Without hashtag: `2PPQVUQ8J`

The library automatically handles tag parsing and URL encoding.

## 📋 Requirements

- **Python 3.8+**
- **httpx**: For async HTTP requests
- **typing-extensions**: For enhanced type hints (Python < 3.10)

## 🔄 Version History

### Latest Release
Check [PyPI](https://pypi.org/project/pybrawlstars/) for the latest version and changelog.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/pybrawlstars.git
cd pybrawlstars

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [PyPI Package](https://pypi.org/project/pybrawlstars/)
- [Brawl Stars API Documentation](https://developer.brawlstars.com/api)
- [Brawl Stars Developer Portal](https://developer.brawlstars.com)
- [Report Issues](https://github.com/yourusername/pybrawlstars/issues)

## ⚡ Performance Tips

1. **Use Context Managers**: Always use `async with BSClient()` for automatic resource cleanup
2. **Batch Requests**: Group related API calls together when possible
3. **Cache Results**: Consider caching frequently accessed data like brawler lists
4. **Handle Rate Limits**: The API has rate limits; implement appropriate delays if needed
5. **Reuse Client**: Create one client instance and reuse it for multiple requests

## 🆘 Support

- 📖 Check the [documentation](https://github.com/yourusername/pybrawlstars/wiki) for detailed guides
- 🐛 Report bugs on [GitHub Issues](https://github.com/yourusername/pybrawlstars/issues)
- 💬 Join discussions on [GitHub Discussions](https://github.com/yourusername/pybrawlstars/discussions)

---

**Note**: This is an unofficial API wrapper. Brawl Stars is a trademark of Supercell Oy. 