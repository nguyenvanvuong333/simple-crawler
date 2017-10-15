from urllib.parse import urlparse

#Get sub domain name(xxx.example.org)
def get_sub_domain_name(url):
	 try:
	 	return urlparse(url).netloc
	 except:
	 	return ''

#get_domain_name (eg:xxx.example => example.com)
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''