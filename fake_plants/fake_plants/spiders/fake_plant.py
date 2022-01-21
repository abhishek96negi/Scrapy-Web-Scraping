import scrapy


class FakePlantSpider(scrapy.Spider):
    name = 'fake_plant'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['http://fake-plants.co.uk/']

    def parse(self, response):
        for link in response.css('li.product-category a::attr(href)'):
            yield response.follow(link.get(), callback=self.page2parser, headers=response.request.headers)

    def page2parser(self, response):
        for product in response.css('div.astra-shop-summary-wrap'):

            yield {
                'Categories': product.css('span.ast-woo-product-category::text').get().strip(),
                'Name': product.css('h2.woocommerce-loop-product__title::text').get().strip(),
                'Price': product.css('bdi::text').get()
            }

