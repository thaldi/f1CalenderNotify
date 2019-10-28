from bs4 import BeautifulSoup
import pip._vendor.requests as reqer


class HtmlParserHelper:
    def __init__(self, url):
        self.url = url

    def GetContentByUrl(self, url=""):
        reqUrl = url if url != "" else self.url
        htmlResult = reqer.get(reqUrl)
        return BeautifulSoup(htmlResult.content)

    def GetElements(self):
        source = self.GetContentByUrl()
        return source.select('a[class="event-item-wrapper event-item-link"]')

    def GetPelementFromHref(self, url):
        source = self.GetContentByUrl(url)
        return source.find(
            "p",
            attrs={
                "class": "race-weekend-dates f1-color--white f1-bg--carbonBlack f1--xxs"
            },
        )
