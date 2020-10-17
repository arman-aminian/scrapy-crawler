import scrapy
import json
from scrapy import Selector
from ..items import TgjucrawlerItem


class TGJUSpider(scrapy.Spider):
    name = "sekee"
    allowed_domains = ['api.tgju.online']
    start_urls = [
        'https://api.tgju.online/v1/market/indicator/summary-table-data/sekee?lang=fa&order_dir=asc&draw=2&columns'
        '%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable'
        '%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D'
        '%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D'
        '=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D'
        '%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D'
        '=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D'
        '%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D'
        '=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D'
        '%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D'
        '=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D'
        '%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D'
        '=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D'
        '%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D'
        '=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D'
        '%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D'
        '=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=3081'
        '&search=&order_col=&order_dir=&from=&to=&convert_to_ad=1&_=1602022756372/']

    def parse(self, response, **kwargs):
        item = TgjucrawlerItem()
        json_response = json.loads(response.body)
        json_data = json_response['data']

        for daily in json_data:
            item['first'] = daily[0]
            item['min'] = daily[1]
            item['max'] = daily[2]
            item['last'] = daily[3]
            item['change_value'] = Selector(text=daily[4]).xpath("//span/text()").extract_first()
            if Selector(text=daily[4]).xpath("//@class").extract_first() == 'low':
                item['change_value'] = '-' + item['change_value']
            item['change_percent'] = Selector(text=daily[5]).xpath("//span/text()").extract_first()
            if Selector(text=daily[5]).xpath("//@class").extract_first() == 'low':
                item['change_percent'] = '-' + item['change_percent']
            item['gregorian_date'] = daily[6]
            item['solar_date'] = daily[7]
            yield item
