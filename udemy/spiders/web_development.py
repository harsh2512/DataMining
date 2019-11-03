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
            course_link = course.xpath(".//a/@href").get()

            yield {
                'Course_Link' : course_link
            }
        
        next_page = response.xpath("//ul[@class='pagination pagination-expanded']/li[position()=last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)