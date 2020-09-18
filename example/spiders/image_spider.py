import datetime
import json
import re
from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.spiders import Spider, Rule
from ..items import ImageItems, ImageItemLoader


class ImageSpider(Spider):
    name = 'jianshu_image'
    rules = [
        Rule(LinkExtractor(allow='(\\"|\\()(//upload-images.*?)(\\"|\\()'), callback='parse'),
    ]

    data = {
        'page': '0',
        'limit': '10'
    }

    def start_requests(self):
        while (True):
            self.data["page"] = int(self.data["page"])
            request = scrapy.Request(
                url='http://182.92.97.72:8080/article/select',
                method="POST",
                headers={'Content-Type': 'application/json'},
                body=json.dumps(self.data),
                callback=self.parse,
                dont_filter=True)
            print(request.body)
            self.data["page"] += 10
            yield request

    def parse(self, response, **kwargs):
        resStr = response.body.decode("utf8")
        json_response = json.loads(resStr)
        data = json_response.get("data")
        for obj in data:
            content = obj.get("content")
            article_id = obj.get("articleId")
            originUrl = obj.get("originUrl")
            imageRes = re.findall('(\"|\()(//upload-images.*?)(\"|\))', content)
            if imageRes:
                realImagePath = []
                for i, imagePath, j in imageRes:
                    realImagePath.append("https:" + imagePath)

                imageItemLoader = ImageItemLoader(item=ImageItems())
                imageItemLoader.add_value("image_urls", realImagePath)
                imageItemLoader.add_value("image_id", "")
                imageItemLoader.add_value("origin_image", realImagePath)
                imageItemLoader.add_value("publish_date", "")
                imageItemLoader.add_value("name", originUrl)
                imageItemLoader.add_value("content", content)
                imageItemLoader.add_value("article_id", article_id)
                yield imageItemLoader.load_item()
