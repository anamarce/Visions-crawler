# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst, MapCompose, Join

def clean(value):
	return value.replace('\t','').replace('\n','').replace('\r','').strip()

class Product(scrapy.Item):
	category = Field(
		input_processor = MapCompose(clean),
		output_processor = Join()
		)
	title = Field(
		input_processor = MapCompose(clean),
		output_processor = Join()
		)
	url = Field(output_processor = TakeFirst())
	regPrice = Field(
		output_processor = TakeFirst()
		)
	salePrice = Field(		
		output_processor = TakeFirst()
		)
	availability = Field(output_processor = TakeFirst())

