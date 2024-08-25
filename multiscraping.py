from url_extractor import extract
import asyncio

subreddits_list = ["funny", "Jokes", "facepalm", "mildlyinteresting", "wholesomememes"]

destination = "D:\\Addy\\Python Files\\Reddit Video Downloader"

async def multi_scraper(subreddits_list, pages, destination):
    await asyncio.gather(*(asyncio.create_task(extract(subreddit, pages, destination)) 
                           for subreddit in subreddits_list)
)


if __name__ == "__main__":
    asyncio.run(multi_scraper(subreddits_list, 3, destination))

