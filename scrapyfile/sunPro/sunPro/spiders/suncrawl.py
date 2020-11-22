# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunproItem,DetailItem


class SuncrawlSpider(CrawlSpider):
    name = 'suncrawl'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://wow.178.com/all/index.html']
    link_detail = LinkExtractor(allow='wow\.178\.com\/[0-9]{6}\/[0-9]{12}')
    rules = (#规则解析器
        Rule(LinkExtractor(allow=r'wow\.178\.com\/all\/index[_]{0,1}\d{0,2}'), callback='parse_item', follow=False),
    Rule(link_detail,callback="parse_detail",follow=False))
    def parse_item(self, response):
        infos=response.xpath('//div[@class="container"]/a')
        for info in infos:
            title=info.xpath('./img/@alt').extract_first()
            #print(title)
            item=SunproItem()
            item["title"]=title
            yield item
    def parse_detail(self,response):
        content=response.xpath('//div[@class="bd"]/p/text()').extract()
        content=''.join(content)
        #print(content)
        item=DetailItem()
        item["content"]=content
        yield item
