import asyncio

import aiomysql

INSERT_SQL = """INSERT INTO article ( title, author, pub_time, origin_url, article_id, content, word_count, view_count, comment_count, like_count, subjects ) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"""


class MysqlDb(object):
    def __init__(self, loop):
        self.host = "182.92.97.72"
        self.port = 3306
        self.user = "root"
        self.password = "caichen"
        self.db = "webset"
        self._pool = None
        self._loop = loop

    async def pool(self):
        if not self._pool:
            print('开始生成链接池')
            self._pool = await aiomysql.create_pool(host=self.host, port=self.port, user=self.user,
                                                    password=self.password, db=self.db, loop=self._loop)
            print(self._pool)
        return self._pool

    async def insertOpt(self, data=None):
        async with self._pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = 'insert into test_asyncio(age) value(%s);'
                try:
                    await cur.execute(sql, data)
                    await conn.commit()
                except Exception as e:
                    print(e)
                    await conn.rollback()

    async def selectOpt(self):
        async with self._pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = 'select content from article limit 0,10'
                try:
                    count = await cur.execute(sql)
                    await conn.commit()
                    return cur, count
                except Exception as e:
                    print(e)
                    await conn.rollback()
