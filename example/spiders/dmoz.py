from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from example.items import ArticelItemLoader, JianshuspiderItem
import json


class DmozSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    subjects = ["HighCharts"]
    rules = [
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail'),
    ]

    def start_requests(self):
        # subjects = ["ios", "java", "python", "c++", "c", "html", "vue", "mysql", "nosql", "linux","HTML/CSS","HTML5","BootStrap","css","JacaScript"]
        # AngularJS JS React TypeScript jQuery  EasyUI Node ajax JSON Echarts HighCharts Docker Ruby Perl Servlet JSP Lua Rust Scala Go PHP Django 设计模式
        # 正则表达式 Maven NumPy ASP AppMl VB SQlite MongoDb Redis Swift Ionic Kotlin Xml DTD XmlDom XSLT Xpath Xquery Xlink Xpointer XmlSchema
        # SVG ASP.NET C# WebFroms webService WSDL SOAP RSS RDF Eclipse Git Svn MarkDown HTTP W3C TCP/IP androidStudio as vsCode Pycharm PhpStorm subLime
        for subject in self.subjects:
            for num in range(1, 200):
                request = Request("https://www.jianshu.com/search?q=" + subject + "&page=" + str(num) + "&type=note")
                request.meta["subject"] = subject
                yield request

    def parse_detail(self, response):
        article_itemLoader = ArticelItemLoader(item=JianshuspiderItem(), response=response)
        json_response = response.xpath("//script[@id='__NEXT_DATA__']//text()").get()
        dict_response = json.loads(json_response)
        note_dict = dict_response.get("props").get("initialState").get("note").get("data")
        article_itemLoader.add_value("title", note_dict.get("public_title"))
        article_itemLoader.add_value("author", note_dict.get("user").get("nickname"))
        article_itemLoader.add_value("pub_time", note_dict.get("last_updated_at"))
        article_itemLoader.add_value("origin_url", response.url)
        article_itemLoader.add_value("article_id", response.url)
        article_itemLoader.add_value("content", note_dict.get("free_content"))
        article_itemLoader.add_value("word_count", note_dict.get("user").get("wordage"))
        article_itemLoader.add_value("view_count", note_dict.get("views_count"))
        article_itemLoader.add_value("comment_count", note_dict.get("comments_count"))
        article_itemLoader.add_value("like_count", note_dict.get("likes_count"))
        article_itemLoader.add_value("subjects", self.subjects[0])
        item = article_itemLoader.load_item()
        yield item
        # url_list = response.xpath("//ul[@class='note-list']/li/div/a/@href").extract()
        # if (url_list):
        #     for articleUrl in url_list:
        #         article_real_url = parse.urljoin(response.url, articleUrl)
        #         request = Request(article_real_url, callback=self.parse_detail)
        #         request.meta['subject'] = response.meta['subject']
        #         yield request
