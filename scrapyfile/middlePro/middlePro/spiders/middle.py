# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=IP']

    def parse(self, response):
        with open("ip.html","w",encoding="utf-8")as fp:
            print("写入成功")
            fp.write(response.text)

