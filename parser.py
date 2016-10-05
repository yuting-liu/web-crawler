from bs4 import BeautifulSoup
import sys, os, scrapy
import urllib2
import re

# entry: search chicago in yelp or zomoto

def yelp_parser(url):
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    # RESTURANT NAME
    nameLine = soup.find_all('h1', {'class' : 'biz-page-title'})
    name = re.split(r'[\t\n]', str(nameLine[0]))[1].strip()
    
    # RESTAURANT RATE
    RateDiv = soup.find_all('div', {'class' : 'rating-info clearfix'})
    RateDiv = re.split(r'[\n]', str(RateDiv[0]))[3]
    rate = RateDiv.split()[2]
    rate = rate[6 : len(rate) - 1]
    
    # RESTAURANT PHONE
    phoneLine = soup.find_all('span', {'class' : 'biz-phone'})
    phone = re.split(r'[\t\n]', str(phoneLine[0]))[1].strip()
    
    # RESTAURANT PRICE
    priceLine = soup.find_all('span', {'class' : 'business-attribute price-range'})[0]
    price = re.split(r'[<>\n]', str(priceLine))[2]
    
    # RESTAURANT ADDRESS
    addressLine = soup.find_all('address')[0]
    addr = re.split(r'[\n]', str(addressLine))[1].strip()
    zipcode = addr[len(addr) -  5 : len(addr)]
    state = addr[len(addr) - 8 : len(addr) - 6]
    city = addr[len(addr) - 17 : len(addr) - 10]
    addr = addr[0 : len(addr) - 19]
    
    # HIGHLIGHTS OF RESTAURANTS
    dls = soup.find_all('dl')
    delivery = False
    takeout = False
    outdoor = False
    bikeParking = False
    parking = 'No'
    wifi = 'No'
    for d in dls:
        attr = str(d)
        if 'Delivery' in attr:
            if 'Yes' in attr:
                delivery = True
        elif "Take-out" in attr:
            if 'Yes' in attr:
                takeout = True
        elif 'Outdoor Seating' in attr:
            if 'Yes' in attr:
                outdoor = True
        elif 'Parking' in attr and 'Bike Parking' not in attr:
            parking = str(d.find_all('dd')[0])
            parking = re.split(r'[\n]', parking)[1].strip()
        elif 'wifi' in attr:
            if 'Yes' or 'Free' in attr:
                wifi = 'Free'

    print name, phone, rate, price, zipcode, state, city, addr, delivery, takeout, outdoor, parking, wifi

if __name__ == "__main__":
    # take this url as example for the yelp website crawler
    yelp_parser('https://www.yelp.com/biz/ninis-deli-chicago?hrid=W3HHQtfPwL4ivYAK7yy97A')



