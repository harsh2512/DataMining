# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BestMoviesSpider(CrawlSpider):
#     name = 'best_movies'
#     allowed_domains = ['imdb.com']
#     #start_urls = ['http://imdb.com/']

#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

#     def start_requests(self):
#         yield scrapy.Request(url='https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc', headers={
#             'User-Agent': self.user_agent
#         })

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
#         Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent'),
#     )
#     def set_user_agent(self, request):
#         request.headers['User-Agent'] = self.user_agent
#         return request

#     def parse_item(self, response):
#         yield {
#             'title': response.xpath("//h3[@class='lister-item-header']/a/text()").get(),
#             'year': response.xpath("//div[@class='lister-item mode-advanced']/div/h3/span[2]/text()").get(),
#             'duration': response.xpath("//div[@class='lister-item mode-advanced']/div/p[1]/span[3]/text()").get(),
#             'genre': response.xpath("(//div[@class='lister-item mode-advanced']/div/p[1]/span[5]/text()").get(),
#             'rating': response.xpath("//div[@class='ratings-bar']/div/strong/text()").get(),
#             'movie_url': response.url
#         }
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration': response.xpath("normalize-space((//time)[1]/text())").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'movie_url': response.url
        }