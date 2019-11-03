# -*- coding: utf-8 -*-
import scrapy


class WebDevelopmentSpider(scrapy.Spider):
    name = 'web_development'
    allowed_domains = ['www.udemy.com']
    #start_urls = ['https://www.udemy.com/courses/development/web-development']

    def start_requests(self):
        yield scrapy.Request(url='https://www.udemy.com/courses/development/web-development', callback=self.parse, headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        })


    def parse(self, response):
        courses = response.xpath("//div[@class='curriculum-course-card--container--1ZgwU']")
        for course in courses:
            course_link = response.urljoin(course.xpath(".//a/@href").get())

            yield {
                'Course_Link' : course_link
            }
