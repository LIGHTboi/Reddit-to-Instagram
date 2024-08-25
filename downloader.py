from RedDownloader import RedDownloader

destination = f"D:\\Addy\\Python Files\\Reddit Video Downloader\\"


def download(post, destination):
    destination = destination + "\\media\\"
    url = post["link"]
    postId = post["postId"]
    title = post["title"]
    attachmentType = post["attachmentType"]

    RedDownloader.Download(url , output = postId, destination = destination)

    return (postId, title, attachmentType)

post1 =    {
      "authorProfile": "https://www.reddit.com/user/Quirky-Material9725",
      "authorId": "t2_hp06zqfj4",
      "title": "Talks about protecting children while leaving his out to dry",
      "link": "https://www.reddit.com/r/facepalm/comments/1e5vbkn/talks_about_protecting_children_while_leaving_his/",
      "publishingDate": "2024-07-17T22:26:46.114000+0000",
      "postId": "t3_1e5vbkn",
      "postLabel": "",
      "postUpvotes": 2539,
      "commentCount": 247,
      "attachmentType": "gallery",
      "attachmentLink": "null"
    }

post2 =     {
      "authorProfile": "https://www.reddit.com/user/crimson_dovah",
      "authorId": "t2_kkbrdje8",
      "title": "Introducing: The Throatsy Boys",
      "link": "https://www.reddit.com/r/funny/comments/1e664b3/introducing_the_throatsy_boys/",
      "publishingDate": "2024-07-18T08:10:43.158000+0000",
      "postId": "t3_1e664b3",
      "postLabel": "null",
      "postUpvotes": 174,
      "commentCount": 21,
      "attachmentType": "video",
      "attachmentLink": "https://v.redd.it/0xpp9glmj8dd1/DASH_96.mp4"
    }

post3 =     {
  "authorProfile": "https://www.reddit.com/user/Power-of-Erised",
  "authorId": "t2_lpqc6",
  "title": "The sign is here, spooky season has begun!",
  "link": "https://www.reddit.com/r/funny/comments/1e6g6ki/the_sign_is_here_spooky_season_has_begun/",
  "publishingDate": "2024-07-18T16:53:16.330000+0000",
  "postId": "t3_1e6g6ki",
  "postLabel": "null",
  "postUpvotes": 39,
  "commentCount": 20,
  "attachmentType": "image",
  "attachmentLink": "null"
}

# download({'authorProfile': 'https://www.reddit.com/user/Marc2NL', 'authorId': 't2_3fnzhpqk', 'title': 'There is always one.', 'link': 'https://www.reddit.com/r/funny/comments/1e5rrxq/there_is_always_one/', 'publishingDate': '2024-07-17T20:00:12.761000+0000', 'postId': 't3_1e5rrxq', 'postLabel': None, 'postUpvotes': 39061, 'commentCount': 603, 'attachmentType': 'video', 'attachmentLink': 'https://v.redd.it/r6gr15t7x4dd1/DASH_96.mp4'}, 
#          destination)

