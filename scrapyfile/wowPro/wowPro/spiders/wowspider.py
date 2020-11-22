# -*- coding: utf-8 -*-
import scrapy
from redis import Redis
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import  DetailItem


class WowspiderSpider(CrawlSpider):
    name = 'wowspider'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://wow.178.com/all/index.html']
    #link_detail = LinkExtractor(allow='wow\.178\.com\/[0-9]{6}\/[0-9]{12}')
    rules = (  # 规则解析器
        Rule(LinkExtractor(allow=r'wow\.178\.com\/all\/index[_]{0,1}\d{0,2}'), callback='parse_item', follow=True),
    )
    coon=Redis(host="127.0.0.1",port=6379)
    def parse_item(self, response):
        infos = response.xpath('//div[@class="container"]/a')
        for info in infos:
            url=info.xpath('./@href').extract_first()
            #title = info.xpath('./img/@alt').extract_first()
            ex=self.coon.sadd("url",url)
            if ex==1:
                yield scrapy.Request(url=url,callback=self.parse_detail)
            else:
                print("无数据更新")


    def parse_detail(self, response):
        content = response.xpath('//div[@class="bd"]/p/text()').extract()
        content = ''.join(content)
        # print(content)
        item = DetailItem()
        item["content"] = content
        yield item
