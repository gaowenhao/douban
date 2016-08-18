import scrapy
from scrapy import Request
from douban.items import MovieLink


class MovieLinkSpider(scrapy.Spider):
    name = "movielink"
    start_urls = ['https://movie.douban.com/top250?start=0']
    allowed_domains = ['douban.com', 'movie.douban.com']

    def parse(self, response):
        for value in response.xpath('//ol/li/div[@class=pic]'):
            items = MovieLink()
            items['rank'] = value.xpath('em/text()').extract()
            items['link'] = value.xpath('a/@href').extract()
            items['name'] = value.xpath('a/img/@alt').extract()
            yield items

    def start_requests(self):
        yield Request("http://www.techbrood.com/",
                      headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"})