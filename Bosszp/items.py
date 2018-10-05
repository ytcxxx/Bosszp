# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BosszpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'jobs'
    job_name = Field()
    salary = Field()
    address = Field()
    work_experience = Field()
    education = Field()
    company_name = Field()
    company_status = Field()
    release_date = Field()
    release_man = Field()
    position = Field()
