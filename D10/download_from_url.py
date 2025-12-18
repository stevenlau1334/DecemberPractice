import requests
import os
import shutil
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')
url = "https://www.andysowards.com/blog/assets/creeper_minecraft_wallpaper__by_insert3199.jpg"

r = requests.get(url, stream=True)
r.raise_for_status()
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

download_file(url, DOWNLOADS_DIR)