from resources.yt_Resources import YTThumb
import easyocr


def test():
    ocr = easyocr.Reader(['pt', 'en'], gpu=False)
    result = ocr.readtext('https://i.ytimg.com/vi/Q2-DC-68IRI/sddefault.jpg')
    return result


for a, b, c in test():
    print(a, b, c)
