import scrapy

from sof.items import SofItem


class SofSpider(scrapy.Spider):
    name = "sof"
    start_urls = [
        "https://stackoverflow.com/questions/tagged/python"
    ]
    total = 1

    def parse(self, response):
        question_list = scrapy.Selector(response).xpath(
            '//*[@class="question-summary"]'
        )

        item = SofItem()
        for question in question_list:
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

        next_page = scrapy.Selector(response).xpath(
            './/a[@rel="next"]/@href'
        ).re_first(r'\w.*')

        if next_page and self.total < 100:
            self.total = self.total + 1
            next_page_url = 'https://stackoverflow.com/' + next_page
            yield scrapy.Request(url=next_page_url)
