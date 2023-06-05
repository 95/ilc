import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        return htmls

async def main():
    urls = [
        "http://youtube.com",
        "http://google.com",
        "http://evergreen.edu",
        "http://github.com"
    ]
    htmls = await fetch_all(urls)
    for url, html in zip(urls, htmls):
        print(f"Webpage URL: {url}, Content length: {len(html)}")

if __name__ == "__main__":
    asyncio.run(main())
