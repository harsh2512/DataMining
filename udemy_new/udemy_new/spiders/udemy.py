# -*- coding: utf-8 -*-
import warnings

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import ScrapyDeprecationWarning
#from scrapy_cloudflare_middleware.middlewares import CloudFlareMiddleware


class UdemySpider(CrawlSpider):
    name = 'udemy'
    allowed_domains = ['udemy.com']
    #start_urls = ['https://www.udemy.com/courses/development/']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.udemy.com/courses/development', headers={
            'User-Agent': self.user_agent
        })


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='list-view-course-card--title--2pfA0']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Categories' : response.xpath("(//a[@class='topic-menu__link'])[1]").get(),
            'Sub_categories' : response.xpath("(//a[@class='topic-menu__link'])[2]").get(),
            'Topic' : response.xpath("(//a[@class='topic-menu__link'])[3]").get(),
            'Course URL' : response.url
        }
