# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
class AudiproPipeline(object):
    def open_spider(self,spider):
        self.images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "img")
        if not os.path.exists(self.images_path):
            os.mkdir(self.images_path)
    def process_item(self, item, spider):
        title=item["title"]
        new_url=item['new_url']
        title_path=os.path.join(self.images_path,title.replace(" ",""))
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        name=new_url.split("_")[-1]
        request.urlretrieve(new_url,os.path.join(title_path,name))
        print(os.path.join(title_path,name))

        return item
