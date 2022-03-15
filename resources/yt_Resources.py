from urllib import request
from pytube import YouTube
from pytube.contrib.channel import Channel
from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent.parent


class YTThumb():
    def __init__(self, url: str):
        # if re.match(
        #     (r'(?:https:\/\/)?(:?www\.)?(?:youtu)(?:[.be]{3})?(?:com)?'
        #      r'\/watch\?v=[\w\-\_]{11}'), url):
        self.url = url
        # else:
        #     raise Exception('Invalid URL.')

    def thumb_info(self, dir: str = None, download: bool = False):
        title = YouTube(self.url).title
        img_url = YouTube(self.url).thumbnail_url
        views = YouTube(self.url).views
        if download:
            request.urlretrieve(
                img_url, BASE_DIR / (self.title + '.jpg'))
            if dir:
                request.urlretrieve(
                    img_url, BASE_DIR / self.dir / (self.title + '.jpg'))
        return {
            "title": title, "img_url": img_url, "url": self.url, "views": views
            }

    def thumb_info_channel(self, dir: str = None, download: bool = False):
        max = len(Channel(self.url))
        list = []
        for video in Channel(self.url):
            title = YouTube(video).title
            img_url = YouTube(video).thumbnail_url
            views = YouTube(video).views
            list.append(
                {
                    "title": title, 'img_url': img_url, 'url': self.url,
                    'views': views
                    }
                )
        return list

