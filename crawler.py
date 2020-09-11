import config
import mod
import collector
import base_op

def scrape():
	while(mod.count > 0):
		base_op.create()
		mod.cur_it.append(config.i_url) #initating from the base url
		#if the previous index is to be deleted during every start from the base url remove '#' from the following statement
		#base_op.erase()
		for url in (mod.cur_it):
			collector.scraper(url) #passing urls from the array of current iteration one by one for crawling

			if(mod.count == config.limit):
				config.logger.info('L I M I T  R E A C H E D') #to notify crawling limit has reached
			else:
				pass
		mod.cur_it = mod.nex_it #setting collected urls for next stage iteration


def quer(): #to print entries inside the index
	base_op.val()

def collapse(): #to delete the index from the database
	base_op.erase()



