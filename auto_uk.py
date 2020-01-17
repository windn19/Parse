import scrapy
from cleaning import clear_price
from pycbrf import ExchangeRates
import os


def curs():
    rates = ExchangeRates()
    funt = rates['GBP']
    euro = rates['EUR']
    cur = euro[4]/funt[4]
    return cur


def clear_long(rlong):
    result = ""
    for char in rlong:
        if char.isdigit():
            result += char
    return float(result)


def mile_to_km(long):
    return round(long * 1.60934, 2)


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = [
        'https://www.autotrader.co.uk/car-search?search-target=usedcars&postcode=WC2N5DU&radius=&make=SKODA&model=YETI&price-from=&price-to=&year-from=&maximum-mileage=&fuel-consumption=&zero-to-60=&quantity-of-doors=&minimum-seats=&annual-tax-cars=&colour=&keywords=&fuel-type=&maximum-badge-engine-size=&transmission=&co2-emissions-cars=&maximum-seats=&insura1nceGroup=&seller-type']
    cur = curs()

    def __init__(self):
        super().__init__()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data1.json')
        if os.path.exists(path):
            os.remove(path)

    def parse(self, response):
        for car_div in response.css('.search-listing'):
            link = car_div.css('.listing-title a.listing-fpa-link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            des = car_div.css('ul.listing-key-specs li::text').getall()
            ades = []
            for item in des:
                if item.strip() != '':
                    ades.append(item)
            year = ades[0][:4]
            long = f'{mile_to_km(clear_long(ades[2]))} кm'
            raw_price = car_div.css('.vehicle-price::text').get()
            price = clear_price(text=raw_price)*Spider.cur
            img_url = car_div.css('.listing-main-image img::attr(src)').get()
            place = car_div.css('span.seller-town::text').get()

            yield {
                'title': title,
                'href': response.urljoin(href),
                'price_eur': price,
                'img': response.urljoin(img_url),
                'place': place.title() if place else 'Неуказано',
                'year': year,
                'long': long,
            }
        for i in range(2, 6):
            yield response.follow(f'https://www.autotrader.co.uk/car-search?sort=relevance&postcode=WC2N5DU&radius=1500&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&make=SKODA&model=YETI&page={i}',
                                  callback=self.parse)
