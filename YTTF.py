from resources.yt_Resources import YTThumb
import easyocr


class YTStats():

    def single_video(url: str, gpu: str = False, download: str = False):
        try:
            _info = YTThumb(url).thumb_info(download=download)
            _ocr = easyocr.Reader(['pt', 'en'], gpu=gpu)
            result = _ocr.readtext(_info['img_url'])
            words = []
            for _bbox, text, prob in result:
                if prob > 0.5:
                    words.append(text)

            return {
                'text': ' '.join(words), 'title': _info['title'],
                'url': _info['url']
                }

        except Exception as error:
            raise error

    # def channel_videos(url: str, gpu: str = False):
    #     try:
    #         _info = YTThumb(url)


print(YTStats.single_video("https://www.youtube.com/watch?v=Xl5T6zFUezc"))
