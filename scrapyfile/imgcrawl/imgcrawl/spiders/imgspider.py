# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImgcrawlItem


class ImgspiderSpider(CrawlSpider):
    name = 'imgspider'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.aitaotu.com/tag/dudou.html']
    l=[]
    rules = (
        Rule(LinkExtractor(allow=r'dudou\/\d{1}\.html')),
        Rule(LinkExtractor(allow=r"[a-z]{5,7}\/\d{5}\.html"),callback=None,follow=True),
        Rule(LinkExtractor(allow=r"guonei\/\d{5}_\d{1,2}\.html"),callback="parse_item",follow=True)
    )

    def parse_item(self, response):
        print(response.url)
        infos = response.xpath('//p[@align="center"]/a')
        for info in infos:
            title = info.xpath("./img/@alt").extract_first()
            src = info.xpath("./img/@src").extract_first()
            item = ImgcrawlItem()
            item["title"] = title
            item["src"] = src
            item["referer"] = response.url
            yield item

