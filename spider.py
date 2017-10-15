from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file =''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.project_name + '/queue.txt'
		Spider.crawled_file = Spider.project_name + '/crawled.txt'
		#Spider.depth = depth
		self.boot()
		self.crawl_page('First spider', Spider.base_url)

	@staticmethod	
	def boot():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)

#		gather links in page_url if page_url was not  crawled
	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print(thread_name + ' is crawling ' + page_url)
			print('queue ' + str(len(Spider.queue)) + ' | ' + 'crawled ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_file()

	@staticmethod
	def gather_links(page_url): 
		html_string = ''
		try:
			response = urlopen(page_url)#Fetch the page
			if response.getheader('Content-Type') == 'text/html':
				html_bytes = response.read()
				html_string = html_bytes.decode('utf-8')
				finder = LinkFinder(Spider.base_url, page_url)
				finder.feed(html_string)
				return finder.page_links()
		except:
			print('Error: Can not scrawl page')
			return set()

	@staticmethod
	def add_links_to_queue(links):
		for link in links:
			if link in Spider.queue:
				continue
			if link in Spider.crawled:
				continue
			if Spider.domain_name not in link:
				continue
			Spider.queue.add(link)

	@staticmethod		
	def update_file():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)