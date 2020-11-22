# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class HosproPipeline(object):
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='192.168.153.129', port=3306, password='Wowxd7080$', user="user1",
                                    db="doc", charset="utf8")
    def process_item(self, item, spider):
        if item.__class__.__name__ == "HosproItem":
            self.cursor = self.conn.cursor()
            print(item)
            try:
                sql='insert into institutions(hospital_name,scores,' \
                    'hospital_qualification,create_time) values(%s, %s, %s, %s)'
                self.cursor.execute(sql,(item["hos_name"],item["hos_score"],item["hos_qualification"],item["hos_date"]))
                self.conn.commit()
                print("医院信息数据库写入成功")
            except Exception as e:
                print(e)
                self.conn.rollback()
            return item
        elif item.__class__.__name__ == "DocItem":
            self.cursor = self.conn.cursor()
            print(item)
            try:
                sql='insert into doctor(name,doctor_title) values(%s, %s)'
                self.cursor.execute(sql,(item["doc_name"],item["doc_duties"]))
                self.conn.commit()
                print("医生信息数据库写入成功")
            except Exception as e:
                print(e)
                self.conn.rollback()

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class imagesPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item.__class__.__name__ == "HosproItem":
            for img in item["hos_img"]:
                yield scrapy.Request(img,meta={"item":item},headers={'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
                ' Gecko) Chrome/77.0.3865.90 Safari/537.36'})


    def file_path(self, request, response=None, info=None):
        filename=request.url.split("/")[-1]
        print(filename+"已下载")
        return filename

    def item_completed(self, results, item, info):
        return item
