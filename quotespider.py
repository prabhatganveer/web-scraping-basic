import scrapy
from .. items import QuotestutorialItem
class QuoteSpider(scrapy.Spider):

    name = "Quotes"
    start_urls = [
        'https://quotes.toscrape.com/',
    ]

    def parse(self, response):

        items = QuotestutorialItem()

        all_quotes = response.css("div.quote")

        for quote in all_quotes:

            title  = quote.css("span.text::text").extract()
            author = quote.css("small.author::text").extract()
            tag    = quote.css("a.tag::text").extract()

            items['title']  = title
            items['author'] = author
            items['tag']    = tag

            yield items