from urllib import request
from pytube import YouTube
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class YTThumb():
    def __init__(self, url: str, dir: str = None):
        self.url = url
        self.dir = dir

    def thumb_download(self):
        self.title = YouTube(self.url).title
        self.img_url = YouTube(self.url).thumbnail_url
        request.urlretrieve(
            BASE_DIR + self.img_url, self.title + '.jpg')
        if self.dir:
            request.urlretrieve(
                self.img_url, BASE_DIR + self.dir + '/' + self.title + '.jpg')

            # return BASE_DIR + self.dir + '/' + 'self.title' + '.jpg'

    def thumb_info(self):
        return [self.title, self.img_url, self.img_url]


if __name__ == '__main__':
    YTThumb().thumb_download()
