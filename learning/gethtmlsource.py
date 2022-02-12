#Test py to fetch html source from a web page and create a BeautifulSoup object

from bs4 import BeautifulSoup
import requests


#print ('please input url: ')
#url = input()
#try:
#    html = requests.get(url)
#    soup = BeautifulSoup(html.text)
#
#    print (f'your input is: {url} \n')
#    print (f'type of html is: {type(html)}')
#    print (f'type of soup is: {type(soup)}')
#    print (f'The response code is : {html.status_code}')
#except:
#    print (f'There is errors! \n The response code is: {html.status_code}')
#
#################################################
#   Mak a Class for requesting html source 
#   and response the html source or soup object.
#
#################################################

class Websouce(url):
    def __init__(self, url):
        self.url = url

    html = ""
    get_response = ""
    soup = ""
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.text)
    finally:
        get_response = html.status_code

url = input()
web = Websource(url)
print (f'the html type is {type(web.html)}')
print (f'thd soup type is {type(web.soup)}')

