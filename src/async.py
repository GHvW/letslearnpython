import aiohttp
import asyncio
from json import loads
import sys

async def get_dad_joke() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}) as response:
            json = await response.text()
            result = loads(json)
            # print(result["joke"])
            return result["joke"]


async def main():
    dad_joke = await get_dad_joke()
    print(dad_joke)


if sys.platform == 'win32':
    # Set the policy to prevent "Event loop is closed" error on Windows - https://github.com/encode/httpx/issues/914
    # https://stackoverflow.com/questions/63860576/asyncio-event-loop-is-closed-when-using-asyncio-run
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
asyncio.run(main())