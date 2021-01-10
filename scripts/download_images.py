"""Download images."""
import time
import datetime
import os
import instaloader


NUM_POSTS = 1000
OUTPUT_FOLDER = "../data/"


class IGImageDownloader:
    def __init__(self, bot, hashtag):
        self.bot = bot
        self.hashtag = hashtag
        self.posts = instaloader.Hashtag.from_name(bot.context, hashtag).get_all_posts()
    
    def create_image_name(self, output_folder, post):
        date = post.date_utc.strftime("%Y%m%d_%H%M%S")
        mediaid = post.mediaid
        likes = post.likes
        path = os.path.join(output_folder, f"{self.hashtag}_{date}_{mediaid}_{likes}")
        return path
    
    def run(self, max_count, output_folder):
        for index in range(1, max_count + 1):
            post = next(self.posts)
            url = post.url
            # Download the post
            try:
                output_path = self.create_image_name(output_folder, post)
                bot.download_pic(output_path, url, datetime.datetime.now())
            except:
                break # If there are any errors, we break out of the loop
            time.sleep(2)


def main():
    bot = instaloader.Instaloader() # alternative: bot.login(user=USER, passwd=PWD)
    downloader = IGImageDownloader(bot, hashtag="selfcare")
    downloader.run(NUM_POSTS, OUTPUT_FOLDER)


if __name__ == "__main__":
    main()