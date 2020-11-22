# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WowproPipeline(object):
    coon=None
    def open_spider(self,spider):
        self.coon=spider.coon
    def process_item(self, item, spider):
        self.coon.lpush("data",item["content"])
        print("写入数据库成功")
        return item
