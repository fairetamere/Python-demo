# -*- coding: utf-8 -*-
import scrapy
import re
from ImgPro.items import ImgproItem
import time
class ImgSpider(scrapy.Spider):
    name = 'img'
    #允许域
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.aitaotu.com/tag/qingquzhuang.html']
    url="https://www.aitaotu.com{}"
    #重写父类方法
    def parse(self, response):
        infos=response.xpath('//*[@id="mainbodypul"]/li')
        for info in infos:
            img_link=info.xpath('./a/@href').extract_first()
            yield scrapy.Request("https://www.aitaotu.com"+img_link,callback=self.parse_detail)
        if response.css("div#pageNum a:nth-last-child(2)::text").extract()[0]=="下一页":
            new_url=self.url.format(response.css("div#pageNum a:nth-last-child(2)::attr(href)").extract()[0])
            #递归回调函数自身进行翻页，将新的请求压入调度器队列
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        infos=response.xpath('//p[@align="center"]/a')
        for info in infos:
            item = ImgproItem()
            title=info.xpath("./img/@alt").extract_first()
            src=info.xpath("./img/@src").extract_first()
            item["title"]=title
            item["src"]=src
            item["referer"]=response.url
            if item["src"]:
                #print(item)
                yield item
        '''for page in range(2,int(response.xpath('//span[@class="totalpage"]/text()').extract_first())+1):
            req = re.findall(r'\/[a-z]{4,8}\/\d{5}',response.url)
            newurl="https://www.aitaotu.com"+req[0]+"_{}".format(page)+".html"
            yield scrapy.Request(newurl,callback=self.parse_detail,dont_filter=False)'''
        if response.css("#nl"):
            newurl="https://www.aitaotu.com"+response.css("#nl>a::attr(href)").extract()[0]
            yield scrapy.Request(newurl, callback=self.parse_detail)










