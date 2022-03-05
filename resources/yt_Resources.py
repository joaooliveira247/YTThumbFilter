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
        # request.urlretrieve(
        #     self.img_url, BASE_DIR / (self.title + '.jpg'))
        # if self.dir:
        #     request.urlretrieve(
        #         self.img_url, BASE_DIR / self.dir / (self.title + '.jpg'))

        #     # return BASE_DIR + self.dir + '/' + 'self.title' + '.jpg'
        return self.title, self.img_url

    def thumb_info(self):
        return print([self.url, self.title, self.img_url])


if __name__ == '__main__':
    print(YTThumb('https://www.youtube.com/watch?v=Q2-DC-68IRI').thumb_download())
