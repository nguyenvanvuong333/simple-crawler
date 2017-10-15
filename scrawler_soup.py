import bs4
from bs4 import BeautifulSoup
import urllib.request  as urllib2

startingURL = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

filename = "products.csv"
f = open(filename,'w')
headers = "brand, description, price, ship\n"
f.write(headers)
page = urllib2.urlopen(startingURL)
html = page.read()
page.close()
soup = BeautifulSoup(html,'lxml')
#thong tin cac 
containers = soup.findAll('div',{"class":"item-container"})#1 san pham dat trong the div - class = item-container
for container in containers:#tung san pham
	brand = container.div.div.a.img['title']
	description = container.findAll("a",{"class":"item-title"})[0].text
	price_current = container.findAll("li",{"class":"price-current"})[0]
	price = price_current.strong.text + price_current.sup.text
	ship = container.findAll("li",{"class":"price-ship"})[0].text.strip()
	f.write(brand + ',' + description+ ',' + price + ',' + ship +"\n")
