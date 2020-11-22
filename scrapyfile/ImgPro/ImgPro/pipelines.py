# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import re


class imagesPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["src"],meta={"item":item},headers={'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
        ' Gecko) Chrome/77.0.3865.90 Safari/537.36','referer': item['referer']})

    def file_path(self, request, response=None, info=None):
        item=request.meta["item"]
        guid=item["title"].split("第")[-1]+".jpg"
        imgname=re.split(r"第\d{1,2}",item["title"])[0].replace(" ","")
        print(item["title"]+":下载成功")
        filename = '{0}/{1}'.format(imgname,guid )
        print(request.headers)
        return filename

    def item_completed(self, results, item, info):
        return item
