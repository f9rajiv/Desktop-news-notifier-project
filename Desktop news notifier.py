from bs4 import BeautifulSoup
from plyer import notification
import requests
import time
# rss feed url
url = 'https://english.onlinekhabar.com/feed'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'lxml')
# find data items
news_list = soup.find_all('item')
# list first  10  news data+654
news_list = news_list[0:10]
# iterate through news list
for news in news_list:
    # notifier to display News
    notification.notify(
                        title='News Update',
                        message=news.title.text,
                        timeout=1)
    # display new update after
    # in seconds waiting time
    time.sleep(5)
