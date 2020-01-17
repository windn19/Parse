# Skoda Yeti brand machines collected from several sites
The program scans sites: auto.ru, www.autotrader.co.uk, voiture.trovit.fr, www.autoscout24.de collects information from ads in a json file (each in its own) and on the basis of them creates an html page with the output of ads and links.
## Installation
The program is written in Python 3.7 and is expected to be already installed
In case of conflict with python2, use pip3. Install the required modules:

pip install -r requirements.txt
## Use
If you are using Linux and a Scrapy module that is installed as python3.7 (i.e. run as: python3.7 -m scrapy shell 'www.google.com'):

    python3.7 newss.py
The module will run four spiders (auto_en.py, auto_en.py, auto_fr.py, auto_de.py) in four sites, collect information and run a template render.py (templates / index.html), which will create a new file ( index.html) that displays the information collected. Clicking on Ctr + C will automatically open the file in the linked application.
Otherwise:
```
python3.7 -m scrapy runspider auto_ru.py -o data / data_ru.json
python3.7 -m scrapy runspider auto_uk.py -o data / data_uk.json
python3.7 -m scrapy runspider auto_fr.py -o data / data_fr.json
python3.7 -m scrapy runspider auto_de.py -o data / data_de.json
python3.7 render.py
```
Then open the file (index.html).
## Project description
This project is written for the purposes of page parsing. The idea behind the devman program.
