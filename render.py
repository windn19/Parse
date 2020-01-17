from staticjinja import Site
import json
import locale
import os


def formated_price(value):
    if value is None:
        return value
    value = float(value)
    formatted_price = locale.currency(value, grouping=True, symbol=False)
    return formatted_price


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    new_cars = []
    #locale._override_localeconv = {'thousands_sep': ' '}
    for file in [x for x in os.listdir('data/') if x.endswith('json')]:
        with open(f'data/{file}') as f:
            cars = json.loads(f.read())
        new_cars += cars
    new_cars.sort(key=lambda x: float(x['price_eur']))
    context = {
        'cars': new_cars
    }
    filters = {
        'format_price': formated_price,
    }
    site = Site.make_site(env_globals=context, filters=filters)

    site.render(use_reloader=True)
