# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import WxproItem


class WxSpider(CrawlSpider):
    name = 'wx'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'mod=list&catid=1&page=\d+'), callback=None, follow=True),
        Rule(LinkExtractor(allow=r'\/article-\d+-\d+\.html'),callback='parse_detail',follow=False)
    )

    def parse_detail(self,reponse):
        item=WxproItem()
        title=reponse.xpath('//h1[@class="ph"]/text()').extract_first()
        item["title"]=title
        yield item
        print(title)