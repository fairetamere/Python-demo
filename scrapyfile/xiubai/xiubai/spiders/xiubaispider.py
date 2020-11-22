# -*- coding: utf-8 -*-
import scrapy
from xiubai.items import XiubaiItem
class XiubaispiderSpider(scrapy.Spider):
    name = 'xiubaispider'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/']
    #基于终端的永久化存储
    '''def parse(self, response):
        infos = response.xpath('//li[contains(@class,"item typs")]')
        all_data = []
        for info in infos:
            title = info.xpath('./div/a/text()')[0].extract()
            auther= info.xpath('./div/div/a/span/text()')[0].extract()
            dic={'title':title,'auther':auther}
            all_data.append(dic)
        print(all_data)
        return all_data'''
    def parse(self, response):
        infos = response.xpath('//li[contains(@class,"item typs")]')
        all_data = []
        for info in infos:
            title = info.xpath('./div/a/text()')[0].extract()
            auther= info.xpath('./div/div/a/span/text()')[0].extract()
            item=XiubaiItem()
            item["title"]=title
            item["auther"]=auther
            yield item

