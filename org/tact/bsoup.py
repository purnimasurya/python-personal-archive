import requests
from bs4 import BeautifulSoup 



page = requests.get('https://docs.google.com/spreadsheets/d/1EfyD7A4YcdAzTfUO0t3yQ0HawetVF5pefS5pPyGVX4g/edit?usp=sharing')
soup = BeautifulSoup(page.text, 'html.parser')    

#print(soup)

'''
    class = .
    id = #
'''


div_tags = soup.select("div.Normal em")

#print(div_tags)

for dts in div_tags:
    print(dts.text)