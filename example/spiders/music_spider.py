import json

import scrapy
from scrapy.spiders import Spider, Rule

from example.items import MusicItemLoader, MusicItems


class ImageSpider(Spider):
    name = 'music'

    def start_requests(self):
        request = scrapy.Request(
            # url='http://tool.liumingye.cn/music/?page=audioPage&type=migu&name=%E5%91%A8%E6%9D%B0%E4%BC%A6',
            url='http://tool.liumingye.cn/music/?page=audioPage&type=YQD&name=https%3A%2F%2Fmusic.163.com%2F%23%2Fplaylist%3Fid%3D5027070307',
            # url='http://tool.liumingye.cn/music/?page=audioPage&type=migu&name=%E8%B5%B5%E7%8E%BA',
            # url='http://tool.liumingye.cn/music/?page=audioPage&type=migu&name=%E9%AB%98%E7%9D%BF',
            callback=self.parse,
            meta={"Middleware": "Selenium"},
            dont_filter=True)
        yield request

    def parse(self, response, **kwargs):
        list = json.loads(response.body)
        for musicItem in list:
            musicItemLoader = MusicItemLoader(item=MusicItems())
            musicItemLoader.add_value("file_urls", musicItem["file_urls"])
            musicItemLoader.add_value("names", musicItem["names"])
            yield musicItemLoader.load_item()
