# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#import sqlite3
import mysql.connector


class QuotestutorialPipeline:

    def __init__(self):
        print("----------------------init")
        self.create_conection()
        self.create_table()

    def create_conection(self):
        self.conn = mysql.connector.connect("myquotes_mysql.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists quotes_mysql_tb""")
        self.curr.execute("""
            create table quotes_mysql_tb(title text, author text,tag text)
        """)

    def store_tb(self,item):
        self.curr.execute("""insert into quotes_mysql_tb values(%s,%s,%s)""",
        (
                item['title'][0],
                item['author'][0],
                item['tag'][0]
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_tb(item)
        return item
