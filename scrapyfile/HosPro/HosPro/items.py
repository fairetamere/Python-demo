# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HosproItem(scrapy.Item):
    # define the fields for your item here like:
    hos_qualification= scrapy.Field()
    hos_name=scrapy.Field()
    hos_score=scrapy.Field()
    hos_img=scrapy.Field()
    hos_date=scrapy.Field()
class DocItem(scrapy.Item):
    doc_hos=scrapy.Field()
    doc_name=scrapy.Field()
    doc_duties=scrapy.Field()
    doc_job=scrapy.Field()
    doc_detail_info=scrapy.Field()
    # define the fields for your item here like:


