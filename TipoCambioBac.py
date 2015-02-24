__author__ = 'william'
from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')


print 'Buyers: ', buyers
print 'Prices: ', prices



pageBac = requests.get('https://www.bac.net/honduras/esp/banco/')
treeBac = html.fromstring(pageBac.text)

pageInterbanca = requests.get('https://www.interbanca.hn/INTERBANCA/INTERBANCA/BE_P_MOSTRARFACTOR?Pn_Empresa=1')
treeIB = html.fromstring(pageInterbanca.text)

Dolar = treeIB.xpath()

print Dolar


