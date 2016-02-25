import re
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from visions.items import Category
from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader

class CategorySpider(CrawlSpider):
    name = "categorySpider"
    allow_domains = ["visions.ca"]
    start_urls = ["http://www.visions.ca/"]
    
    def parse(self, response):
        sel = Selector(response=response)
        
        links = self.getDepartments(sel)

        for name, url in links.items():
            category = Category()
            category['title'] = name
            category['url'] = url
            yield category

    def getDepartments(self, selector):
        departments = {}
        deptInfo = selector.css('#mastermenu-dropdown > li.menulevel-0')
        for dept in deptInfo:
            departments.update(self.getCategories(dept))
        return departments

    def getCategories(self, selector):
        categories = {}
        catInfo = selector.css('li.menulevel-0 > div.mastermenu-bigsub > div > div')
        if catInfo:
            for cat in catInfo:
                categories.update(self.getSubcategories(cat))
        else:
            name, url = self.getDepartmentsInfo(selector)
            categories[name] = url
        return categories

    def getSubcategories(self, selector):
        subcategories = {}
        subcatsInfo = selector.css('div > ul > li > a')
        if subcatsInfo:
            for subcat in subcatsInfo:
                name, url = self.getSubcategoriesInfo(subcat)
                subcategories[name] = url
        else:
            name, url = self.getCategoriesInfo(selector)
            subcategories[name] = url
        return subcategories

    def getDepartmentsInfo(self, dept):
        name = dept.css('li.menulevel-0 > a > span::text').extract()[0]
        url = dept.css('li.menulevel-0 > a::attr(href)').extract()[0]
        return name, url

    def getCategoriesInfo(self, cat):
        name = cat.css('div > a > span::text').extract()[0]
        url = cat.css('div > a::attr(href)').extract()[0]
        return name, url

    def getSubcategoriesInfo(self, cat):
        name = cat.css('a::text').extract()
        url = cat.css('a::attr(href)').extract()
        return name[0], url[0]