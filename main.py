import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
THEAD_NUM = 8
QUEUE = Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Create theads
def create_threads():
	for thead in range(THEAD_NUM):
		print("threading")
		t = threading.Thread(target = work)
		t.daemon = True
		t.start()

#work
def work(Num = 30):
	print("Work")
	while True and Num > 0:
		link = QUEUE.get()
		Spider.crawl_page(threading.current_thread().name, link)
		QUEUE.task_done()
		Num -= 1


#add links to QUEUE for thread
def create_jobs():
	print("create_jobs()")
	queue_links = file_to_set(QUEUE_FILE)
	for link in queue_links:
		QUEUE.put(link)
	QUEUE.join()

#check queue has links, if so crawl the links
def crawl():
	print("crawl()")
	queue_links = file_to_set(QUEUE_FILE)
	if len(queue_links) > 0:
		print(str(len(queue_links)) + ' links in the queue')
		create_jobs()


create_threads()
crawl()