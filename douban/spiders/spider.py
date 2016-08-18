import scrapy
from scrapy import Request
from douban.items import MovieLink


class MovieLinkSpider(scrapy.Spider):
    name = "movielink"
    allowed_domains = ['douban.com', 'movie.douban.com']

    def parse(self, response):
        for x in response.xpath('//div[@class="item"]'):
            items = MovieLink()
            items['rank'] = x.xpath('//div[@class="pic"]/em/text()').extract()
            items['link'] = x.xpath('//div[@class="pic"]/a/@href').extract()
            items['name'] = x.xpath('//div[@class="pic"]/a/img/@alt').extract()
            items['star'] = x.xpath('//div[@class="info"]/div[@class="bd"]/'
                                    'div[@class="star"]/span[@class="rating_num"]/text()').extract()
            items['people'] = x.xpath('//div[@class="info"]/'
                                      'div[@class="bd"]/div[@class="star"]/span[not(@property)]/text()').extract()
            items['description'] = x.xpath('//div[@class="info"]/'
                                           'div[@class="bd"]/p[@class="quote"]/span/text()').extract()
        yield items

    def start_requests(self):
        for x in range(0, 250, 25):
            yield Request(url="https://movie.douban.com/top250?start=%d&" % x,
                          headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"})