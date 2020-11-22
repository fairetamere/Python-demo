# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class BossPipeline(object):
    conn=None
    cursor=None
    def open_spider(self,spider):
        self.conn=pymysql.Connect(host='192.168.153.129',port=3306,password='Wowxd7080$',user="user1",db="spider1",charset="utf8")
    def process_item(self, item, spider):
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute('insert into data2 values("{}","{}")'.format(item["job_name"],item["job_dec"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        #return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
