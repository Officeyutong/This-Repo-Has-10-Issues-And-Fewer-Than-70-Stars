import aiohttp
import asyncio

import config
import aiofiles
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {config.OAUTH_TOKEN}"
}

async def fetch_stars(client: aiohttp.ClientSession):
    resp = await client.get(f"https://api.github.com/repos/Officeyutong/testrepo")
    json_resp = await resp.json()
    return json_resp["stargazers_count"]


async def update_repo_name(client: aiohttp.ClientSession, name: str):
    async with client.patch(f"https://api.github.com/repos/Officeyutong/testrepo", json={"name": name}) as resp:
        resp: aiohttp.client.ClientResponse
        return resp.status, await resp.json()


async def main():
    async with aiohttp.ClientSession(headers=HEADERS) as client:
        client: aiohttp.ClientSession
        while True:
            stars = await fetch_stars(client)
            print(stars)
            resp = await update_repo_name(client, f"This-Repo-Has-Less-Than-{stars+1}-Stars")
            print(resp)
            await asyncio.sleep(3)
asyncio.get_event_loop().run_until_complete(main())
