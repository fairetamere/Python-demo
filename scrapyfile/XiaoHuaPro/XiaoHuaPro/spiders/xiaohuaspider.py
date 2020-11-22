# -*- coding: utf-8 -*-
import scrapy
from XiaoHuaPro.items import XiaohuaproItem
class XiaohuaspiderSpider(scrapy.Spider):
    name = 'xiaohuaspider'
    #allowed_domains = ['www.xxx.com']
    start_urls = ["http://www.521609.com/meinvxiaohua/"]
    page=2
    url="http://www.521609.com/meinvxiaohua/list12{}.html"

    def parse(self, response):
        infos=response.xpath('//div[@class="index_img list_center"]/ul/li')
        for info in infos:
            name=info.xpath('./a[2]/text()|./a[2]/b/text()')[0].extract()
            item=XiaohuaproItem()
            item["name"]=name
            yield item
        if self.page<=11:
            new_url=self.url.format(self.page)
            self.page+=1
            yield scrapy.Request(url=new_url,callback=self.parse)
