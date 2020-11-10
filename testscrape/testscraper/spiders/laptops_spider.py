import scrapy
from testscraper.items import TestscraperItem

class LaptopsSpider(scrapy.Spider):
  name='laptops_spider'

  start_urls=[
    'https://webscraper.io/test-sites/e-commerce/static/computers/laptops',
  ]

  def parse(self, response):
    #laptops = response.xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div')
    for laptop in response.css('div.thumbnail'):  #laptops

      title = laptop.css('div.caption h4 a.title::text').get(),
      image = laptop.css('img.img-responsive::attr(src)').get(),
      description = laptop.css('div.caption p.description::text').get(),
      price = laptop.css('div.caption h4.price::text').get()

      item = TestscraperItem()
      item["title"] = title
      item["image"] = image
      item["description"] = description
      item["price"] = price

      yield item

    next_page = response.css('li.page-item a[rel="next"]::attr(href)').get()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)




"""
  allowed_domains = ['blog.scrapinghub.com']
  start_urls=[
    'https://blog.scrapinghub.com/',
  ]
  def parse(self, response):
    
    for post in response.css('div.post-item'):

      title = post.css('.post-header h2 a::text').get()
      image = post.css('.hs-featured-image::attr(src)').get()
      author = post.css('.author a::text').get()
      comments_string = post.css('.custom_listing_comments a::text').get().split()[0]
      comments = int(comments_string)

      item = TestscraperItem()
      item["title"] = title
      item["image"] = image
      item["author"] = author
      item["comments"] = comments

      yield item

    next_page = response.css('a.next-posts-link::attr(href)').get()
    if next_page is not None:
      absolute_next_page = response.urljoin(next_page)
      yield scrapy.Request(absolute_next_page, callback=self.parse)

"""