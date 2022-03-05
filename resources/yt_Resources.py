from urllib import request
from pytube import YouTube
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class YTThumb():
    def __init__(self, url: str):
        self.url = url
        self.dir = dir

    def thumb_info(self) -> None:
        self.title = YouTube(self.url).title
        self.img_url = YouTube(self.url).thumbnail_url
        return {
            "title": self.title, "img_url": self.img_url, "url": self.url
            }

    def thumb_download(self, dir: str = None):
        request.urlretrieve(
            self.img_url, BASE_DIR / (self.title + '.jpg'))
        if self.dir:
            request.urlretrieve(
                self.img_url, BASE_DIR / self.dir / (self.title + '.jpg'))