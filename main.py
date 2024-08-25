from multiscraping import multi_scraper
from downloader import download
from instagrapi import Client
from instagram_uploader import uploader
import asyncio
import json
import os
import shutil

account = "fight.corn"
password = "Fights@112026"
cl = Client()
cl.login(account, password)

destination = f"D:\\Addy\\Python Files\\Reddit Video Downloader\\{account}\\reddit"
subreddits_list = ["fightporn", "StreetMartialArts", "TotalKalesh"]
posts_per_subreddit = 3
pages_scrape_number = 5

if not os.path.exists(destination):
    os.makedirs(destination)

if not os.path.exists(destination + f"\\reddit_posted.json"):
    with open(destination + f"\\reddit_posted.json", mode = 'w'):
        pass

if not os.path.exists(destination + "\\media"):
    os.makedirs(destination + "\\media")

if not os.path.exists(destination + "\\scraped"):
    os.makedirs(destination + "\\scraped")

def sorter_and_validator(scraped_sub, posts_number):
    with open(destination + f"\\scraped\\{scraped_sub}.json", encoding = 'utf-8') as f:
        data = json.load(f)

    posts_list = data["posts"]

    sorted_posts = sorted(posts_list, key = lambda p: p['postUpvotes'], reverse = True)

    valid_posts = []
    post_count = 0

    with open(destination + f"\\reddit_posted.json", mode = 'r', encoding = 'utf-8') as f:
        try:
            posted_data = json.load(f)['postsId']
        except:
            posted_data = []
    
    for post in sorted_posts:
        if post["postId"] not in posted_data:
            if post["attachmentType"] in ["video", "image", "gallery"]:
                valid_posts.append(post)
                post_count += 1
                posted_data.append(post["postId"])
            
        if post_count == posts_number:
            break

    with open(destination + f"\\reddit_posted.json", mode = "w", encoding = 'utf-8') as f:
        json.dump({"postsId": posted_data}, f, indent = 2, ensure_ascii = False)

    return valid_posts


asyncio.run(multi_scraper(subreddits_list, pages_scrape_number, destination))

valid_posts = []

for subreddit in subreddits_list:
    valid_posts.extend(sorter_and_validator(subreddit, posts_per_subreddit))

print("Downloading all posts...")

toUpload = dict()

for post in valid_posts:
    try:
        data = download(post, destination)
        toUpload[data[0]] = (data[1], data[2])
    except:
        pass

print("All posts have been downloaded successfully. Uploading now...")

for postId, (title, attachmentType) in toUpload.items():
    uploader(destination, postId, title, attachmentType, cl)


notDeleted = True

while notDeleted:
    try:
        shutil.rmtree(destination + "\\media")
        shutil.rmtree(destination + "\\scraped")
        notDeleted = False
    except:
        continue