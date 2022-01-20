import scrapy
from ..items import JessopsItem
from scrapy.loader import ItemLoader


class JessopsSpiderSpider(scrapy.Spider):
    name = 'jessops_spider'
    allowed_domains = ['jessops.com/drones']
    start_urls = [
        'https://www.jessops.com/drones/'
    ]

    def parse(self, response):
        for product in response.css('div.f-grid.prod-row'):
            # ---------------- using without items container --------------------

            # yield {
            #     'Image': product.css('img::attr(src)').get(),
            #     'URL': product.css('a::attr(href)').get(),
            #     'Image': product.css('a::text').getall()[1],
            #     'Description': ",".join(product.css('ul.f-list.j-list').css('li::text').getall()),
            #     'Price': product.css('p.price.larger::text').get()
            # }
            # ---------------------- using with item container  ----------------------
            # item = JessopsItem()
            # item['product_image'] = product.css('img::attr(src)').get()
            # item['product_url'] = product.css('a::attr(href)').get()
            # item['product_name'] = product.css('a::text').getall()[1]
            # item['product_description'] = ",".join(product.css('ul.f-list.j-list').css('li::text').getall())
            # item['product_price'] = product.css('p.price.larger::text').get()
            #
            # yield item

            # -------------------- using item loader ----------------------
            l = ItemLoader(item=JessopsItem(), selector=product)

            l.add_css('product_image', 'img::attr(src)')
            l.add_css('product_url', 'a::attr(href)')
            l.add_xpath('product_name', '//*[@id="products-list"]/div[1]/div[1]/div/div[2]/div/div[1]/h4/a/text()')
            l.add_css('product_description', 'ul.f-list.j-list')
            l.add_css('product_price', 'p.price.larger')

            yield l.load_item()

