# -*- coding: utf-8 -*-
import scrapy
from Boss.items import BossItem
import time

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['https://search.chinahr.com/cq/job/?key=Python']
    url="https://search.chinahr.com/cq/job/pn{}/?key=Python"
    page=2

    def parse(self, response):
        infos=response.xpath('//div[@class="job-list-box"]/div')
        for info in infos:
            item=BossItem()
            job_name=info.xpath("./ul[1]/li[1]/text()").extract_first()
            item["job_name"]=job_name
            detail_url=info.xpath("./@data-detail").extract_first()
            print(job_name)
            yield scrapy.Request(detail_url,callback=self.detail_parse,meta={'item':item})
        #分页操作
        if self.page<=2:
            new_url=self.url.format(self.page)
            self.page+=1
            yield scrapy.Request(new_url,callback=self.parse)

    def detail_parse(self, response):
        item = response.meta["item"]
        job_dec = response.xpath('//div[@class="desc_desc"]/div//text()|//div[@class="newJDuty"]//text()').extract()
        job_dec = "".join(job_dec)
        item["job_dec"] = job_dec
        print(job_dec)
        yield item

