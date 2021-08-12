from psaw import PushshiftAPI
import datetime as dt
import pandas as pd
import time


# Description: gets historical data after X and before X
def get_reddit_histo(after, before, subreddit, limit):
	# convert string times into datetimes/epoch
	after = int(dt.datetime.strptime(after, '%Y-%m-%d %H:%M:%S').timestamp())
	before = int(dt.datetime.strptime(before, '%Y-%m-%d %H:%M:%S').timestamp())
	# get data from PushShiftAPI
	api = PushshiftAPI()
	data = list(api.search_submissions(after=after,
							before=before,
                            subreddit=subreddit,
                            filter=['url','author', 'title', 'subreddit'],
                            limit=limit))
	return data


# Description: gets recent X mins of data from reddit
def get_reddit_recent(minutes):
	# convert to datetime/epoch
	after=int((dt.datetime.now() - dt.timedelta(minutes=minutes)).timestamp())
	# get data from PushShiftAPI
	data = list(api.search_submissions(after=after,
                            subreddit=subreddit,
                            filter=['url','author', 'title', 'subreddit'],
                            limit=1000))
	return data
