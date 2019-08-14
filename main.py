import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    vk_token = os.getenv("ACCESS_TOKEN")
    group_id = os.getenv("GROUP_ID")
    album_id = os.getenv("ALBUM_ID")
    print(album_id)