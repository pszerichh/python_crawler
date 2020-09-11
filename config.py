import logging


es_address = 'localhost:9200' #setting the connection address


limit = 100 #crawling limit, can be changed to 5000 as per the project


i_url = 'https://google.com' #base url


logging.basicConfig(filename = 'crawl_result.log', format = '%(asctime)s %(message)s', level = logging.NOTSET, filemode = 'w' ) #configuring logger
logger = logging.getLogger() #creating logger object
