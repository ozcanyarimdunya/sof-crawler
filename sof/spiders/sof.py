import scrapy

from sof.items import SofItem


class SofSpider(scrapy.Spider):
    name = "sof"
    start_urls = [
        "https://stackoverflow.com/questions/tagged/python"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=lambda response: self.parse(response))

    def parse(self, response):
        change = scrapy.Selector(response).xpath(
            '//*[@class="question-summary"]'
        )

        item = SofItem()
        for question in change:
            item['title'] = question.xpath(
                './/div[@class="summary"]/h3/a/text()').re_first(r'\w.*')

            item['description'] = question.xpath(
                './/div[@class="excerpt"]/text()').re_first(r'\w.*')

            item['vote'] = question.xpath(
                './/span[contains(@class,"vote-count-post")]/strong/text()').re_first(r'\d')

            item['answer'] = question.xpath(
                './/div[contains(@class,"status")]/strong/text()').re_first(r'\d')

            item['view'] = question.xpath(
                './/div[contains(@class,"views")]/@title').re_first(r'\d')

            item['asked'] = question.xpath(
                './/div[contains(@class,"user-action-time")]/span/@title').re_first(r'\w.*')

            item['user'] = question.xpath(
                './/div[contains(@class,"user-details")]/a/text()').re_first(r'\w.*')

            yield item
