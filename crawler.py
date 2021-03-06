__author__ = 'Shixuan Fan, Yuting Liu, Zhenyu Zhang'
__date__ = 'Oct 3th, 2016'
"""
We crawl roughly 3200 pages from Yelp and Zomato with detailed attributes
"""
from bs4 import BeautifulSoup
from urlparse import urljoin
import urllib2

YELP_DOMAIN = 'https://www.yelp.com'
YELP_START_URLS = ['https://www.yelp.com/search?find_loc=chicago&start=',
    'https://www.yelp.com/search?find_loc=New+York,+NY&start']
ZOMATO_START_URLS = ['https://www.zomato.com/chicago/restaurants?page=']


def yelp_crawler(file):
    # entry page 
    for start_url in YELP_START_URLS:
        for i in range(0, 10, 10):
            soup = BeautifulSoup(urllib2.urlopen(start_url + str(i)).read())
            urls = soup.find_all('a', {'class' : 'nowrap'})
            for url in urls:
                file.write(YELP_DOMAIN + url['href'] + '\n')

def zomato_crawler(file):
    for start_url in ZOMATO_START_URLS:
        for i in range(1, 2):
            soup = BeautifulSoup(urllib2.urlopen(start_url + str(i)).read())
            print soup.prettify()
            urls = soup.find_all('a', {'class' : 'item result-menu'})
            for url in urls:
                url = url['href']
                url = url[0 : len(url) - 12]
                file.write(url + '\n')
    
if __name__ == "__main__":
    yelpurl = open('yelpURL.txt', 'w')
    yelp_crawler(yelpurl)

    zomatourl = open('zomatoURL.txt', 'w')
    zomato_crawler(zomatourl)