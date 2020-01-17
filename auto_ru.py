import scrapy
from cleaning import clear_price
import os


class Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = ['https://auto.ru/polevskoy/cars/skoda/yeti/all/?sort=fresh_relevance_1-desc&currency=EUR']

    def __init__(self):
        super().__init__()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.json')
        if os.path.exists(path):
            os.remove(path)

    def parse(self, response):
        for car_div in response.css('.ListingCars-module__listingItem'):
            link = car_div.css('a.ListingItemTitle-module__link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            year = car_div.css('div.ListingItem-module__year::text').get()
            long = car_div.css('div.ListingItem-module__kmAge::text').get()
            raw_price = car_div.css('.ListingItemPrice-module__content::text').get()
            price = clear_price(text=raw_price)
            img_url = car_div.css('.Brazzers__image::attr(data-src)').get()
            place = car_div.css('.MetroListPlace_nbsp::text').get()
            yield {'title': title,
                   'href': href,
                   'year': year,
                   'price_eur': price,
                   'long': long,
                   'img': response.urljoin(img_url),
                   'place': place}
        for href in response.css('.ListingPagination-module__page::attr(href)'):
            yield response.follow(href, callback=self.parse)
