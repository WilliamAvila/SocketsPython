__author__ = 'william'
import HTMLParser
from requests import get

def getTasas():
    r = get('https://www.bac.net/honduras/esp/banco/')

    class MyHTMLParser(HTMLParser):
        lista =''
        def handle_data(self, data):
            if str(data).__contains__('Lps.'):
                self.lista+= str(data).replace('Lps.','').strip()+','

    parser = MyHTMLParser()
    parser.feed(r.text)

    return parser.lista