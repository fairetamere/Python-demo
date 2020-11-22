# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import HosproItem, DocItem



class HoscrawlSpider(scrapy.Spider):
    name = 'Hoscrawl'
    # allowed_domains = ['https://y.soyoung.com/']
    page = 2
    start_urls = ['https://y.soyoung.com/hospital/page/1/']
    model_urls = "https://y.soyoung.com/hospital/page/{}/"

    def parse(self, response):
        hos_list = response.xpath('//div[@class="content"]')
        for hos in hos_list:
            if hos.xpath('./div[@class="name"]/a/span'):
                item_hos = HosproItem()
                hos_qualification = ["院", "诊", "科室"].index(
                    re.findall(r"院|诊|科室", re.sub(r"\s", "", hos.xpath('./p[@class="text"][1]/text()').extract_first()))[
                        0])
                item_hos["hos_qualification"] = hos_qualification
                yield scrapy.Request("https://y.soyoung.com" + hos.xpath('./div[@class="name"]/a[1]/@href').
                                     extract_first(), callback=self.parse_detail, meta={"item": item_hos})
        if self.page <= 10:
            yield scrapy.Request(self.model_urls.format(self.page), callback=self.parse)
            self.page += 1

    def parse_detail(self, response):
        item_hos = response.meta["item"]
        hos_name = response.xpath('//div[@class="name_box"]/a/@title').extract_first()
        item_hos["hos_name"] = hos_name
        hos_score = response.xpath('//div[@class="name_box"]/div[@class="score"]/span[1]/span/text()').extract_first()
        item_hos["hos_score"] = hos_score
        hos_logo = response.xpath('//div[@class="hos_head"]//img[2]/@src').extract_first()
        item_hos["hos_img"] = []
        item_hos["hos_img"].append(hos_logo)
        hos_date = response.xpath('//*[@id="bd"]/div[4]/div[1]/div[2]/p[3]/span[2]/text()').extract_first()
        item_hos["hos_date"] = hos_date
        hos_env_img = response.xpath('//ul[@class="list"]/li/a/img/@src').extract()
        item_hos["hos_img"].extend(hos_env_img)

        yield scrapy.Request(response.url + "xiangce/", callback=self.parse_licensing,
                             meta={"item": item_hos})
        yield scrapy.Request(response.url + "yisheng/", callback=self.parse_doc)

    def parse_licensing(self, response):
        item_hos = response.meta["item"]
        licensing_img_list = response.xpath('//ul/li/a/img/@src').extract()
        item_hos["hos_img"].extend(licensing_img_list)
        yield item_hos

    def parse_doc(self, response):
        for doc in response.xpath('//ul[@class="list after"]/li'):
            yield scrapy.Request("https://y.soyoung.com" + doc.xpath('./div/a/@href').extract_first(),
                                 callback=self.pase_doc_detail)

    def pase_doc_detail(self, response):
        item_doc = DocItem()
        doc_hos = response.xpath('//div[@class="name_box"]/a/@title').extract_first()
        item_doc["doc_hos"] = doc_hos
        doc_name = re.sub(r"\s", "", response.xpath('//div/p[1]/span[@class="c"]/text()').extract_first())
        item_doc["doc_name"] = doc_name
        doc_duties = re.sub(r"\s", "", response.xpath('//div/p[3]/span[@class="c"]/text()').extract_first())
        item_doc["doc_duties"] = doc_duties
        doc_job = response.xpath('//div/p/span[@class="c"]/a/text()').extract_first()
        item_doc["doc_job"] = doc_job
        doc_detail_info = re.sub(r"\s", "", response.xpath('//div/span[@class="c"]/text()').extract_first())
        item_doc["doc_detail_info"] = doc_detail_info
        yield item_doc
