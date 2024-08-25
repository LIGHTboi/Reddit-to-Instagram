from instagrapi import Client
from os import listdir

def uploader(destination, postId, title, attachmentType, cl):
    if attachmentType == "gallery":     
        cl.album_upload([destination + f"\\media\\{postId}\\" + file for file in listdir(destination + f"\\media\\{postId}")], 
                    title + " #trending #meme #funny #funnyvideos")
        
    elif attachmentType == "video":
        cl.clip_upload(destination + f"\\media\\{postId}.mp4",
                       title + " #trending #meme #funny #funnyvideos")
        
    elif attachmentType == "image":
        cl.photo_upload(destination + f"\\media\\{postId}.jpeg",
                       title + " #trending #meme #funny #funnyvideos")


if __name__ == "__main__":

    toUpload = {"t3_1e5vbkn": ("Talks about protecting children while leaving his out to dry", "gallery"),
            "t3_1e664b3": ("Introducing: The Throatsy Boys", "video"),
            "t3_1e6g6ki": ("The sign is here, spooky season has begun!", "image")}
    
    cl = Client()
    cl.login("shithead0032", "minimilitia1")

    destination = f"D:\\Addy\\Python Files\\Reddit Video Downloader\\shithead0032\\reddit"

    # print(tuple((postId, title, attachmentType) for postId, (title, attachmentType) in toUpload.items()))

    for postId, (title, attachmentType) in toUpload.items():
        uploader(destination, postId, title, attachmentType)


# f"{post[:-(post[::-1].index('.') + 1)]}


