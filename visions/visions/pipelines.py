# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import PprintItemExporter, JsonItemExporter
#Will print a json file that can be found in the root, the name will be visionsSpider.json
class VisionsJsonPipeline(object):
    def __init__(self):
        self.exporter = None

    def open_spider(self, spider):
        self.exporter = JsonItemExporter(open('%s.json' %spider.name, 'wb'))
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()

#Will print a txt file that can be found in the root, the name will be visionsSpider.txt
class VisionsPrettyPipeline(object):
    def __init__(self):
        self.exporter = None

    def open_spider(self, spider):
        self.exporter = PprintItemExporter(open('%s.txt' %spider.name, 'w'))
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
