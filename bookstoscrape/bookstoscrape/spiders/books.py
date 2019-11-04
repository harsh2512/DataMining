# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BooksSpider(CrawlSpider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com/']

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//article[@class="product_pod"]/h3/a"), callback='parse_item', follow=True),
#         Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), callback='parse_item'),
#     )

#     def parse_item(self, response):
#         yield {
#             'title': response.xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a/text()").get(),
#             'price': response.xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/div[2]/p[1]/text()").get()
#         }
# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'price': response.xpath("(//div[@class='col-sm-6 product_main']/p)[1]/text()").get()
        }
