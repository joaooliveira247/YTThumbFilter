from resources.yt_Resources import YTThumb
import easyocr


def test(url: str, gpu: str = False):
    _info = YTThumb(url).thumb_info()
    _ocr = easyocr.Reader(['pt', 'en'], gpu=gpu)
    result = _ocr.readtext(_info['img_url'])
    for _bbox, text, prob in result:
        if prob > 0.5:
            print(text)
