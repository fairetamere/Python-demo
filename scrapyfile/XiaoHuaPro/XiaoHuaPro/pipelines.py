# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class XiaohuaproPipeline(object):
    fp = None

    def open_spider(self, spider):
        print("开始爬虫")
        self.fp = open("./xiaohua.txt", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        name= item["name"]
        self.fp.write(name)
        print("文件写入成功")
        return item

    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()


class Mysql_pileline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='192.168.153.129', port=3306, password='Wowxd7080$', user="user1",
                                    db="spider1", charset="gbk")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into data2 values("{}")'.format(item["name"]))
            self.conn.commit()
            print("数据库写入成功")
        except Exception as e:
            print("出现异常")
            print(e)
            self.conn.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
