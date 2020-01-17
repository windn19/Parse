import scrapy
from cleaning import clear_price


class Spider(scrapy.Spider):
    name = 'Spider2'
    start_urls = [
        'https://www.autoscout24.de/lst/skoda/yeti?sort=standard&desc=0&ustate=N%2CU&cy=D&atype=C&ac=0']

    def parse(self, response):
        for item in response.css('div.cl-list-element-gap'):
            title_list = item.css('div.cldt-summary-title h2::text').getall()
            title = ''.join(title_list)
            href = item.css('a::attr(href)').get()
            data_list = item.css('div.cldt-summary-vehicle-data li::text').getall()
            long = data_list[0].strip()
            year = data_list[1].strip()
            rawprice = item.css('div.cldt-summary-payment span::text').get()
            price = clear_price(rawprice)
            img = item.css('div.cldt-summary-gallery img::attr(data-src)').get()
            place = '-'.join(item.css('div.cldf-summary-seller-contact-address span::text').getall())
            yield {
                'title': title,
                'href': response.urljoin(href),
                'year': year,
                'long': long,
                'price_eur': price,
                'img': img,
                'place': place
            }
        for href in range(2, 10):
            yield response.follow(f'https://www.autoscout24.de/lst/skoda/yeti?&sort=standard&desc=0&ustate=N%2CU&size=20&cy=D&atype=C&ac=0&page={href}',
                                  callback=self.parse)
