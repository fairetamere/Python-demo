# -*- coding: utf-8 -*-
import scrapy
from ..items import AudiproItem


class AudiSpider(scrapy.Spider):
    name = 'audi'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['https://car.autohome.com.cn/pic/series/5912.html']

    def parse(self, response):
        infos=response.xpath('//div[contains(@class,"uibox-con carpic-list03") ]/ul/li[position()<=8]')
        for info in infos:
            item=AudiproItem()
            item['title']=info.xpath('./a/@title').extract_first()+"第{}张".format(infos.index(info)+1)
            item['new_url']="https:"+info.xpath('./a/img/@src').extract_first()
            yield item



