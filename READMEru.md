#  Машины марки Шкода Йети, собранные с нескольких сайтов
Программа сканирует сайты: auto.ru, www.autotrader.co.uk, voiture.trovit.fr, www.autoscout24.de собирает информацию из объявлений в json-файл(каждый в свой) и на основе их создает html страницу с выводом объявлений и ссылками.
## Установка
Программа написана на пайтоне3.7 и ожидается, что он уже установлен
В случае конфликта с пайтон2 использульте pip3.Установите необходимы модули:

	pip install -r requirements.txt 
## Использование
Если вы используете  Linux и модуль Scrapy, который установлен как модуль python3.7(т.е запускается как: python3.7 -m scrapy shell 'www.google.com'):
	python3.7 newss.py
Модуль запустит поочередно четыре паука(auto_ru.py, auto_uk.py, auto_fr.py, auto_de.py) на четыре сайта, соберет информацию и запустит обработчик(render.py) шаблона(templates/index.html), который создаст новый файл(index.html), отображающий собранную информацию. При нажатии на Ctr+C автоматически откроет файл в привязанном приложении.
Иначе:
```
python3.7 -m scrapy runspider auto_ru.py -o data/data_ru.json
python3.7 -m scrapy runspider auto_uk.py -o data/data_uk.json
python3.7 -m scrapy runspider auto_fr.py -o data/data_fr.json
python3.7 -m scrapy runspider auto_de.py -o data/data_de.json
python3.7 render.py
```
Затем открыть файл(index.html).
## Описание проекта
Данный проект написан в учебных целях по парсингу страниц. Идея программы devman. 

