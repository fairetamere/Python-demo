# -*- coding: utf-8 -*-
# -*- auther: Joyeuse -*-
# -*- date: 2020/9/24 -*-

import scrapy
from selenium import webdriver
from ..items import NeteaseproItem
class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    #allowed_domains = ['www.163.com']
    start_urls = ['https://news.163.com/']
    model_urls=[]
    def __init__(self):
        super(NeteaseSpider, self).__init__()
        self.wd = webdriver.Chrome(r"D:\webdiver\chromedriver.exe")
    def parse(self, response):
        infos=response.xpath('//li[contains(@class,"guonei")]|//li[contains(@class,"guoji")]'
                             '|//li[contains(@class,"hangkong")]|//li[contains(@class,"wurenji")]')
        for info in infos:
            model_url=info.xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        for url in self.model_urls:
            yield scrapy.Request(url ,callback=self.parse_model)
    def parse_model(self,response):
        infos=response.xpath('//div[@class="news_title"]')
        for info in infos:
            title=info.xpath('./h3/a[contains(@href,"163")]/text()').extract_first()
            news_link=info.xpath('./h3/a[contains(@href,"163")]/@href').extract_first()
            item=NeteaseproItem()
            item["title"]=title
            if news_link:
                yield scrapy.Request(news_link,callback=self.parse_detail,meta={"item":item})
    def parse_detail(self,response):
        content=response.xpath('//div[@class="content"]/p/text()').extract()
        content="".join(content)
        item = response.meta["item"]
        item["content"]=content
        yield item

    def closed(self,spider):
        self.wd.quit()
