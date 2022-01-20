# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_currency(value):
    return value.replace('£', '').strip()


def remove_extra_spaces(value):
    return ",".join([x.strip() for x in value.strip().split('\n')])


def product_url_modification(value):
    return f'www.jessops.com{value}'


class JessopsItem(scrapy.Item):
    # define the fields for your item here like:
    # --------------- without using item loader ---------------------
    # product_image = scrapy.Field()
    # product_url = scrapy.Field()
    # product_name = scrapy.Field()
    # product_description = scrapy.Field()
    # product_price = scrapy.Field()

    # ----------------- with item loader -------------------------
    product_image = scrapy.Field(output_processor=TakeFirst())
    product_url = scrapy.Field(input_processor=MapCompose(product_url_modification), output_processor=TakeFirst())
    product_name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    product_description = scrapy.Field(input_processor=MapCompose(remove_tags, remove_extra_spaces), output_processor=TakeFirst())
    product_price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency), output_processor=TakeFirst())