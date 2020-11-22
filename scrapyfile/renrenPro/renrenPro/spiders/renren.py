# -*- coding: utf-8 -*-
import scrapy
import time

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def start_requests(self):
        url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp="
        fromdata = {"email": "197084185@qq.com",
                    "icode": "",
                    "origURL": "http://www.renren.com/home",
                    "domain": "renren.com",
                    "key_id": "1",
                    "captcha_type": "web_login",
                    "password": "574ae054a65a2ef8b604a2eed023b8398de455a8bd4ae4fd615ae199a3becc49",
                    "rkey": "c5c08b36d1daef7b10b7ae3c886850e6",
                    "f": ""}
        yield scrapy.FormRequest(url,formdata=fromdata,callback=self.parse_page)
    def parse_page(self, response):
        pass



