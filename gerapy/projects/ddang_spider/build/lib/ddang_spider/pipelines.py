# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DdangSpiderPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='wang9264', db='cd_li',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()  # 创建游标对象
        try:
            self.cursor.execute('insert into ddbook values(0,"%s","%s","%s","%s","%s","%s","%s")' % (
                item["name"], item["author"], item["introduction"], item["price"], item["press"], item["time"],
                item["comment"]))
            self.conn.commit()
        # author = item['author']
        # content = item['content']
        except Exception as err:
            print(err)
            self.conn.rollback()  # 数据回滚
        return item

    def close_spiser(self, spider):
        print('爬虫结束')
        self.cursor.close()
        self.conn.close()
