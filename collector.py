import bs4
import requests
import re
from elasticsearch import Elasticsearch as es
import config
import mod
import base_op
def scraper(urls):
	config.logger.info('crawling.....') #to notify begining of crawling
	config.logger.info(urls)
	web = requests.get(urls) #http request
	soup = bs4.BeautifulSoup(web.text, 'html.parser') #soup object
	for link in soup.find_all('a'):
		l_href = link.get('href') #extracting the href value
		if(type(l_href) == str): #avoiding urls with href value NoneType
			if(len(l_href) >= 2): #avoiding page refreshing links
				div = re.split('/', link.get('href'))
				if(len(div) >= 2): #avoiding javascripts
					if(div[0] == 'https:'):
						i = 0
						for it in (mod.nex_it):
							if(it == l_href):
								i = i+1
							else:
								continue

						if( i == 0 ):
							mod.nex_it.append(l_href) #collecting url
							config.logger.info(l_href)
						else:
							continue

					elif(div[0] == 'http:'):
						i = 0
						for it in (mod.nex_it):
							if(it == l_href):
								i = i+1
							else:
								continue

						if( i ==0 ):
							mod.nex_it.append(l_href) #collecting url
							config.logger.info(l_href)
						else:
							continue

					else:
						i = 0
						temp_href = urls + l_href
						for it in (mod.nex_it):
							if(it == temp_href):
								i = i+1
							else:
								continue

						if(i == 0):
							mod.nex_it.append(temp_href) #collecting url
							config.logger.info(temp_href)
						else:
							continue

				else:
					continue

			else:
				continue

		else:
			continue

	base_op.put(urls) #passing for database operations
	mod.count = mod.count + 1 #iteration object
	config.logger.info('F E E D E D  T O  D A T A B A S E') #notifying 

