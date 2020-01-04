# -*- coding: utf-8 -*-
import scrapy


class ScrapyNewBookSpider(scrapy.Spider):
    name = 'Scrapy_New_Book'   #指定爬蟲的名字
    #allowed_domains = ['https://www.books.com.tw/web/books_nbtopm_19/']
         #紀錄網頁可允許及不允許, 建議#掉,因為怕主要要爬的爬不回來
    start_urls = ['https://www.books.com.tw/web/books_nbtopm_19//']
         #要爬的網頁

    def parse(self, response):
        for book in response.css("div.item"):
            name=book.css("div.msg h4 a::text").get()
            url=book.css("div.msg h4 a::attr(href)").get()
            prices=book.css("div.price_box ul.price li.set2 strong::text").getall()
            yield {
                "書名":name,
                "網址":url,
                "價格":prices[1],
                "折扣":prices[0]
            }







