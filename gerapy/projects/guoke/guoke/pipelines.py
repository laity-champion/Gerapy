# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class GuokePipeline:
    def __init__(self):
        self.f = open('gk.csv', mode='a', encoding='utf-8', newline='')
        self.csv_writer = csv.DictWriter(self.f, fieldnames=['title', 'url', 'summary'])
        self.csv_writer.writeheader()

    def process_item(self, item, spider):
        self.csv_writer.writerow(item)  # 写入数据到csv
        return item

    def close_spider(self, spider):
        self.f.close()
