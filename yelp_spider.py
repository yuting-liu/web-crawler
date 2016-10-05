import scrapy
class yelpSpider(scrapy.Spider):
    name = "yelp"
    start_urls = [
        "https://www.yelp.com/search?find_loc=chicago&start=0"
    ]
    
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)