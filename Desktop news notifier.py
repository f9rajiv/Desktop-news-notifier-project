from bs4 import BeautifulSoup
from plyer import notification
import requests
import time
# rss feed url
url = 'https://english.onlinekhabar.com/feed'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'lxml')

news_list = soup.find_all('item')


for news in news_list:

    notification.notify(
                        title='News Update',
                        message=news.title.text,
                        timeout=1)
  
    time.sleep(5)
