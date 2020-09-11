import datetime
from threading import Timer
import crawler

start = datetime.datetime.today()
end = start.replace(day = start.day, hour = 1, minute = 0, second = 0, microsecond = 0) + datetime.timedelta(days = 1)
t_diff = end - start
secs = t_diff.total_seconds()



task = Timer(secs, crawler.scrape())
task.terminate()
task.start()

