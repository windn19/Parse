import scrapy
from cleaning import clear_price


class Spider(scrapy.Spider):
    name = 'Spider2'
    start_urls = [
        'https://voiture.trovit.fr/index.php/cod.search_adwords_cars/type.0/what_d.skoda%20yeti/tracking.%7B%22acc%22%3A64%2C%22c%22%3A121542818%2C%22a%22%3A4914930218%2C%22k%22%3A40791108338%2C%22d%22%3A%22c%22%7D/ppc_landing_type.2/origin.11/device.c?gclid=CjwKCAiApOvwBRBUEiwAcZGdGK-LGcgWWtz7oo1xdHiEwZeXFlYID2GNT8lTVdyEktFR_0dPV1ffrxoCjGsQAvD_BwE']

    def parse(self, response):
        for item in response.css('li div.js-item'):
            title = item.css('h4 a::attr(title)').get()
            href = item.css('a.js-item-title::attr(href)').get()
            prop = item.css('div.property::text').getall()
            if prop:
                long = prop[0] if prop[0] else 'Неуказано'
                year = prop[1][-4:] if len(prop) > 1 else 'Неуказано'
            else:
                continue
            rawprice = item.css('span.amount::text').get()
            price = clear_price(rawprice)
            img = item.css('div.image img::attr(src)').get()
            if not img:
                img = item.css('div.image img.js-lazyImage::attr(data-src)').get()
            place = item.css('h5 span::text').get()
            if not price:
                continue
            yield {
                'title': title,
                'href': href,
                'year': year,
                'long': long,
                'price_eur': price,
                'img': response.urljoin(img),
                'place': place
            }
        for href in response.css('div.js-paginador a'):
            yield response.follow(href, callback=self.parse)
