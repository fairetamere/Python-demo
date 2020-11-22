# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fpsPro.items import FpsproItem

class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    #allowed_domains = ['www.xxx.com']
    #start_urls = ['http://www.xxx.com/']
    redis_key="fbs1"
    rules = (
        Rule(LinkExtractor(allow=r'wow\.178\.com\/all\/index[_]{0,1}\d{0,2}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        infos=response.xpath('//div[@class="container"]/a')
        for info in infos:
            title=info.xpath('./img/@alt').extract_first()
            #print(title)
            item=FpsproItem()
            item["title"]=title
            yield item
