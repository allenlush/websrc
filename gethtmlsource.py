#Test py to fetch html source from a web page and create a BeautifulSoup object

from bs4 import BeautifulSoup
import requests

print ('please input url: ')
url = input()
try:
    html = requests.get(url)
    soup = BeautifulSoup(html.text)

    print (f'your input is: {url} \n')
    print (f'type of html is: {type(html)}')
    print (f'type of soup is: {type(soup)}')
except:
    print ('there is errors!')


