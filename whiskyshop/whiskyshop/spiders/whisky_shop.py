import scrapy
from ..items import WhiskyshopItem

class WhiskyShopSpider(scrapy.Spider):
    name = 'whisky_shop'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky/all'
                  ]

    def parse(self, response):
        for product_detail in response.css('div.product-item-info'):
            whisky_name = product_detail.css('a.product-item-link::text').extract()
            whisky_price = product_detail.css('span.price::text').extract()
            whisky_image_link = product_detail.xpath('//*[@id="maincontent"]/div/div/div[3]/ol/li[9]/div/a/span/span/img').get().split('"')[3]
#                css('.product-image-photo::attr(src)').extract()
            whisky_product_link = product_detail.css('a.product-item-link').attrib['href']
            yield {
                'whisky_name': whisky_name[0] if whisky_name else None,
                'whisky_price': whisky_price[0] if whisky_price else None,
                'whisky_image': whisky_image_link,
                'whisky_product_link': whisky_product_link
            }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)





