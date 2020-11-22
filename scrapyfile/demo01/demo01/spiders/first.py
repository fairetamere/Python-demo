# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/','http://www.163.com/']

    def parse(self, response):
        print(response)
        pass
