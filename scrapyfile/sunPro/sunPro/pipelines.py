# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SunproPipeline(object):
    def process_item(self, item, spider):
        if item.__class__.__name__=="DetailItem":
            print(item["content"])
        else:
            print(item["title"])

        return item
