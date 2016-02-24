import re
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from visions.items import Product
from scrapy.loader import ItemLoader

class VisionsSpider(CrawlSpider):
    name = "visionsSpider"
    domain_name = "visions.ca"
    start_urls = ["http://www.visions.ca/"]

    download_delay = 0.5

    """The rules obtain all the links for the categories and follow the links"""
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths=(
                    '//li[contains(@class,"menulevel-0")]//div/a',
                    '//li[contains(@class,"menulevel-0")]/a[not(contains(./following-sibling::div/@id,"menu"))and contains(@href,"837")]'
            ),
                               unique=True), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths=('//a[contains(@id,"lnkNextpage")]'),
                               unique=True), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths=('//div//a[contains(@id,"lnkBrand")]'),
                               unique=True),follow=True),
        Rule(
            SgmlLinkExtractor(restrict_xpaths=(
                '//div[contains(@class,"bundleItem")]//td/a[contains(@id,"hplBundleName")]',
                '//div[contains(@class,"productresult")]//a[contains(@id,"lnk")]'),
                               unique=True),callback='parse_item', follow=True),
        )
    def parse_item(self,response):
        sel = Selector(response)
        il = ItemLoader(item=Product(), response=response)

        cat = il.get_xpath('//div[contains(@id, "ctl00_pnlBreadCrumbs")]/a[last()]/text()')
        availability = il.get_xpath('//a[contains(@id,"hplddToCart") or contains(@class,"addToCart")]/text()')
        price = il.get_css('span#ctl00_ContentPlaceHolder1_ctrlProdDetailUC_lblRegprice > font::text')
        sale = il.get_css('span#ctl00_ContentPlaceHolder1_ctrlProdDetailUC_lblSaleprice > font::text')
       
        """If the xpath doesn't retunr a category, the product belongs to the Bundle category"""
        if not cat:
            il.add_value("category", "Bundle")
        else:
            il.add_value("category", cat)
       
        il.add_css("title", "span#ctl00_ContentPlaceHolder1_ctrlProdDetailUC_lblProdTitle::text")
        il.add_value("url",response.url)
       
        """If a product can be added to the cart, the product is available online, if not, the product is not available online"""
        if "ADD TO CART" in availability:
            il.add_value("availability", "Product is available online")
        else:
            il.add_value("availability", "Product is not available online")

        """If there's a sale price present but not a regular price present, it switches the sale price for the regular price as shown in the website"""
        if not price:
            il.add_value("regPrice",sale)
            il.add_value("salePrice", None)
        else:
            il.add_value("regPrice", price)
            il.add_value("salePrice",sale)
        return il.load_item()