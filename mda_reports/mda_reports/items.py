# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class MdaReportsItem(scrapy.Item):
    date = scrapy.Field(
        output_processor = TakeFirst()
    )
    time = scrapy.Field(
        output_processor = TakeFirst()
    )
    character = scrapy.Field(
        output_processor = TakeFirst()
    )
    symbol = scrapy.Field(
        output_processor = TakeFirst()
    )
    company = scrapy.Field(
        output_processor = TakeFirst()
    )
    market = scrapy.Field(
        output_processor = TakeFirst()
    )
    heading = scrapy.Field(
        output_processor = TakeFirst()
    )

    file_urls = scrapy.Field()
    files = scrapy.Field()
