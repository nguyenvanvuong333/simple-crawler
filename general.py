import os

#Each website you crawl is a separate folder
def create_project_dir(directory):
	"""create directory if it's not exists"""
	if not os.path.exists(directory):
		os.makedirs(directory)

#Create file in the folder
def create_data_files(project_name, url):
	queue = project_name + "/queue.txt"
	if not os.path.isfile(queue):
		write_file(queue, url)
	crawl = project_name + '/crawled.txt'
	if not os.path.isfile(crawl):
		write_file(crawl)

def write_file(path, data=''):
	f = open(path, 'w')
	f.write(data)
	f.close()

def delete_file_contents(path):
	with open(path,'w'):
		pass

def append_to_file(path, data=''):
	with open(path, 'a') as f:
		f.write(data + '\n')


def file_to_set(filename):
	results = set()
	with open(filename,'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

def set_to_file(links, file):
	delete_file_contents(file)#delete old data
	for link in sorted(links):
		append_to_file(file, link)