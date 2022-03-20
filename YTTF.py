from resources.yt_resources import YTThumb
import easyocr


class YTStats():
    def single_video(url: str, gpu: str = False, download: bool = False):
        try:
            _info = YTThumb().thumb_info(url=url, download=download)
            _ocr = easyocr.Reader(['pt', 'en'], gpu=gpu)
            result = _ocr.readtext(_info['img_url'])
            words = []
            for _bbox, text, prob in result:
                if prob > 0.5:
                    words.append(text)

            _info['text'] = ' '.join(words)
            _info.pop('img_url')

            return _info

        except Exception as error:
            raise error

    def channel_videos(url: str, gpu: str = False, download: bool = False):
        _info = YTThumb().thumb_info_channel()
        return _info

