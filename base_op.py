from elasticsearch import Elasticsearch as es
import config
import datetime
import mod

cli = es([config.es_address]) #creating client

body_map = { #setting body for index mapping
	"properties": {
		"url": {
			"type": "keyword"
		},
		"time": {
			"type": "date"
		}
	}
}

body_sort = { #setting body for index sorting, in case of query
	"size": mod.count,
	"query": { "match_all" : {}},
	"sort": {
		"time": "asc"
	}
}



def create():
	if(cli.indices.exists(index = 'crawled_urls')):
		pass
	else:
		cli.indices.create(index = 'crawled_urls') #creating index
		cli.indices.put_mapping(index = 'crawled_urls', body = body_map ) #applying mapping


def put(url):
	body_search= {
            "query": {
            "bool": {
            "must":{
            "match":{
            "url":url
            }
            }
            }
            }
            }
	cli.indices.refresh(index = 'crawled_urls')
	res = cli.search(index = 'crawled_urls', body = body_search)
	if(len(res['hits']['hits']) > 0):
		pass
	else:
		time = datetime.datetime.now() #getting current date & time
		cli.index('crawled_urls', body = {'url': url, 'time': time}) #feeding the url to the database with entry time
		cli.indices.refresh(index = 'crawled_urls')


def val(): #to get entries currently stored in the index
	cli.indices.refresh(index = 'crawled_urls')
	res = (cli.search(index = 'crawled_urls', body = body_sort)) #search command
	cli.indices.refresh('crawled_urls') #refreshing
	for blocks in res['hits']['hits']: #in case of printing entries in the index
		print(blocks['_source'])


def erase(): #to erase the index from the database
	if(cli.indices.exists(index = 'crawled_urls')):
		cli.indices.delete(index = 'crawled_urls') #to delete currently saved index before crawling the base url after 24 hours
	else:
		pass