# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WxproPipeline(object):
    fp=None
    def open_spider(self,spider):
        self.fp=open('wx.txt',"w",encoding='utf-8')
    def process_item(self, item, spider):
        title=item["title"]
        self.fp.write(title)
        return item
    def colse_spider(self,spider):
        self.fp.close()
