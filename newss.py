import os
from cleaning import clear_file


lands = ['ru', 'uk', 'fr', 'de']
for i in range(4):
    clear_file(f'data/data_{lands[i]}.json')
    os.system(f'python3.7 -m scrapy runspider auto_{lands[i]}.py --output=data/data_{lands[i]}.json -L WARNING')
    print(f'{lands[i]}  -- ok')
os.system('python3.7 render.py')
os.system('xdg-open index.html')
