# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import MdaReportsItem


class CompaniesSpider(scrapy.Spider):
    name = 'companies'
    allowed_domains = ['www.set.or.th', 'market.sec.or.th']
    start_urls = ['https://www.set.or.th/set/commonslookup.do?language=en&country=US']
    start_date = '20100101'
    end_date = '20200101'

    def parse(self, response):
            letters = response.xpath("//div[@class='col-xs-12 padding-top-10 text-center capital-letter']/a")
            for letter in letters:
                character = letter.xpath(".//text()").get()
                link = letter.xpath(".//@href").get()

                absolute_stock_url = f"https://www.set.or.th{link}"
                yield scrapy.Request(url=absolute_stock_url,
                                        callback=self.parse_company,
                                        meta={'character': character})

    def parse_company(self, response):
        character = response.request.meta['character']
        rows = response.xpath("//td/a/../..")
        for row in rows:
            symbol = row.xpath(".//td[1]/a/text()").get()
            company = row.xpath(".//td[2]/text()").get()
            market = row.xpath(".//td[3]/text()").get()

            absolute_file_url = f"https://market.sec.or.th/public/idisc/en/Viewmore/fs-mda?searchSymbol={symbol}&dateFrom={self.start_date}&dateTo={self.end_date}"
            yield scrapy.Request(url=absolute_file_url,
                                    callback=self.parse_file,
                                    meta={
                                        'character': character,
                                        'symbol': symbol,
                                        'company': company,
                                        'market': market})

    def parse_file(self, response):
        character = response.request.meta['character']
        symbol  = response.request.meta['symbol']
        company = response.request.meta['company']
        market = response.request.meta['market']
        rows = response.xpath("//td/a/../..")
        for row in rows:
            date = row.xpath(".//td[1]/text()").get()
            time = row.xpath(".//td[2]/text()").get()
            heading = row.xpath(".//td[3]/text()").get()
            file_src = row.xpath(".//td[4]/a/@href").get()

            loader = ItemLoader(item=MdaReportsItem())

            loader.add_value('date', date)
            loader.add_value('time', time)
            loader.add_value('character', character)
            loader.add_value('symbol', symbol)
            loader.add_value('company', company)
            loader.add_value('market', market)
            loader.add_value('heading', heading)
            loader.add_value('file_urls', file_src)
            yield loader.load_item()
