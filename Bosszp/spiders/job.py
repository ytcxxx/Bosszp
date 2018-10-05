# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import quote
import logging

from Bosszp.items import BosszpItem


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['www.zhipin.com']
    base_url = 'https://www.zhipin.com/c100010000/h_100010000/?query='
    logger = logging.getLogger('testmsg')
    
    def start_requests(self):
        self.logger.debug('start crawl')
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword) + '&page=' + str(page) + '&ka=page-' + str(page)
                yield Request(url=url, callback=self.parse)
    
    def parse(self, response):
        results = response.xpath('//div[@class="job-list"]//li//div[@class="job-primary"]')
        for result in results:
            item = BosszpItem()
            item['job_name'] = result.xpath('.//h3[@class="name"]//div[@class="job-title"]//text()').extract_first()
            item['salary'] = result.xpath('.//h3[@class="name"]//span[@class="red"]//text()').extract_first()
            item['address'] = result.xpath('.//p//text()').extract()[0]
            item['work_experience'] = result.xpath('.//p//text()').extract()[1]
            item['education'] = result.xpath('.//p//text()').extract()[2]
            item['company_name'] = result.xpath(
                './/div[@class="info-company"]//h3[@class="name"]//text()').extract_first()
            item['company_status'] = result.xpath('.//p//text()').extract()[3:-1]
            item['release_date'] = result.xpath('.//p//text()').extract()[-1]
            item['release_man'] = result.xpath('.//div[@class="info-publis"]//h3[@class="name"]//text()').extract()[0]
            item['position'] = result.xpath('.//div[@class="info-publis"]//h3[@class="name"]//text()').extract()[1]
            yield item
