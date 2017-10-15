import urllib.request  as urllib2 
import lxml.html

startingURL = "http://lxml.de/xpathxslt.html"

def crawl(url, depth=3):
	if depth == 0:
		return None
	try:
		page = urllib2.urlopen(url)
	except (urllib2.URLError, ValueError):
		return None
	html = page.read()
	dom  = lxml.html.fromstring(html)
	root = {}
	root['childen'] = []
	root['url'] = url
	root['content'] = html

	print ('level {0:2d}: {1}' .format(depth, url))
	for link in dom.xpath('//a/@href'):
		child = crawl(link, depth - 1)
		if child is not None:
			root['childen'].append(child)
	return root

crawl(startingURL)