from urllib import request
from pytube import YouTube
from pytube.contrib.channel import Channel
from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent.parent


class YTThumb():

    def thumb_info(self, url: str, dir: str = None, download: bool = False):
        if re.match(
            (r'(?:https:\/\/)?(:?www\.)?(?:youtu)(?:[.be]{3})?(?:com)?'
             r'\/watch\?v=[\w\-\_]{11}'), url):
            title = YouTube(url).title
            img_url = YouTube(url).thumbnail_url
            views = YouTube(url).views
            if download:
                request.urlretrieve(
                    img_url, BASE_DIR / (title + '.jpg'))
                if dir:
                    request.urlretrieve(
                        img_url, BASE_DIR / self.dir / (title + '.jpg'))
            return {
                "title": title, "img_url": img_url, "url": url,
                "views": views}
        else:
            raise Exception('Invalid URL.')

    def thumb_info_channel(url: str, dir: str = None, download: bool = False):
        if re.match(
            r'(?:https:\/\/)?(:?www\.)?(?:youtu)(?:[.be]{3})?(?:com)?\/c\/\w+',
                url):
            try:
                list = []
                for video in Channel(url):
                    title = YouTube(video).title
                    img_url = YouTube(video).thumbnail_url
                    views = YouTube(video).views
                    list.append(
                        {
                            "title": title, 'img_url': img_url, 'url': url,
                            'views': views
                            }
                        )
                return list
            except Exception:
                raise Exception('Invalid URL.')
