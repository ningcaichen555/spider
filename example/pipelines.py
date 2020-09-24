# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import hashlib
import os
from datetime import datetime
from urllib.parse import to_bytes, urlparse

import scrapy
from pymysql import cursors
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline

from .items import ImageItems, md5_convert, MusicItems
from .settings import MY_SETTINGS
from twisted.enterprise import adbapi
from .image.ImageUp import ImageUp

INSERT_SQL = """INSERT INTO article ( title, author, pub_time, origin_url, article_id, content, word_count, view_count, comment_count, like_count, subjects ) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"""

UPDATE_SQL = """update article set content = %s where article_id= %s
"""


class JianshuspiderPipeline:
    # 创建初始化函数，当通过此类创建对象时首先被调用的方法
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        settings = MY_SETTINGS
        settings['cursorclass'] = cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **settings)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.db_insert, item)
        query.addErrback(self.handle_error, item)
        return item

    def handle_error(self, failure, item):
        print('============================', failure, item)

    def db_insert(self, cursor, item):
        tt = cursor._connection._connection
        try:
            tt.ping()
        except Exception as e:
            print("=======" + e)
            self.dbpool.close()
            settings = MY_SETTINGS
            settings['cursorclass'] = cursors.DictCursor
            self.dbpool = adbapi.ConnectionPool("pymysql", **settings)

        print("添加数据========================")
        cursor.execute(
            INSERT_SQL,
            (item['title'], item['author'], item['pub_time'], item['origin_url'], item['article_id'],
             item['content'], item['word_count'], item['view_count'], item['comment_count'],
             item['like_count'], item['subjects']))
        return item


class UploadImagePipeline:
    # 创建初始化函数，当通过此类创建对象时首先被调用的方法
    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.imageUp = ImageUp()

    @classmethod
    def from_settings(cls, settings):
        settings = MY_SETTINGS
        settings['cursorclass'] = cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **settings)
        return cls(dbpool)

    def process_item(self, item, spider):
        index = 0
        content = item['content']
        while index < len(item["image_urls"]):
            imagePath = item["image_urls"][index]
            realImagePath = item["origin_image"][index]
            realImagePath = realImagePath.replace("https:", "")
            key = os.path.basename(imagePath)
            ret, info = self.imageUp.upload(key, "../images/" + imagePath)
            # print("上传七牛之后图片地址" + "http://qew7yirqe.hn-bkt.clouddn.com/" + ret["key"])
            newImagePath = ret["key"]
            content = content.replace(realImagePath, newImagePath)
            item['content'] = content
            query = self.dbpool.runInteraction(self.db_update, item)
            query.addErrback(self.handle_error, item)
            index = index + 1
        return item

    def handle_error(self, failure, item):
        print('============================', failure, item)

    def db_update(self, cursor, item):
        print("更新数据========================" + item['article_id'])
        cursor.execute(
            UPDATE_SQL,
            (item['content'], item['article_id'])
        )
        return item


class SaveImagePipeline(ImagesPipeline):
    default_headers = {
        'referer': '',
    }

    def get_media_requests(self, item, info):
        # 下载图片，如果传过来的是集合需要循环下载
        # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        if isinstance(item, ImageItems) and item.get('image_urls'):
            self.default_headers['referer'] = item["name"]
            for url in item['image_urls']:
                yield Request(url=url, headers=self.default_headers,
                              meta={'publish_date': item['publish_date']})

    def item_completed(self, results, item, info):
        '''所有图片处理完毕后（不管下载成功或失败），会调用item_completed进行处理
           results是一个list 第一个为图片下载状态,
           get_media_requests在图片下载完毕后，处理结果会以二元组的方式返回给item_completed()函数的
           results，图片下载状态定义如下：
               (success, image_info_or_failure)
               success表示图片是否下载成功；image_info_or_failure是一个字典
        '''
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_urls'] = image_path
        return item

    def file_path(self, request, response=None, info=None):
        filePath = u'%s/%s.jpg' % (request.meta['publish_date'], md5_convert(request.url))
        return filePath


class SelfDefineFilePipline(FilesPipeline):
    """
    继承FilesPipeline，更改其存储文件的方式
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_media_requests(self, item, info):
        if isinstance(item, MusicItems) and item.get('file_urls'):
            t = 0
            for url in item.get('file_urls'):
                request = Request(
                    url=url,
                    meta={"name": item.get("names")[t]},
                    dont_filter=True)
                t += 1
                yield request

    def file_path(self, request, response=None, info=None):
        name = request.meta.get("name")
        filePath = u'%s.mp3' % name
        return filePath

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['file_urls'] = image_path
        return item
