# Ana Marcela N. - Visions Crawler
This is my assessment for the 360pi assessment challenge.

#Description
My crawler goes to the www.visions.ca website and checks every category to obtain the title, url, regular price, sale price and availability for each product.

#Things to consider
To complete the challenge I had to assume the following:
* The categories included what's listed on the site as departments, subcategories for each department and the sub-subcategories displayed on the menu.
* Availability is whether or not you can buy a product online. If you can add a product to your cart, the product is available online, if not, the product is not available online.

#Special Scenarios:
Two specials scenarios can happen on the site:
* A product does not have a price listed (sale or regular price)
E.g.: http://www.visions.ca/Catalogue/Category/Details.aspx?categoryId=599&productId=26638&sku=BXPERIAZ3COMP
* A product only has a regular Price, for this case I had to create a condition that switches the "sale price" for the "regular price". On the website the price is shown as the regular price (styling) however, on code, the price displayed is using the sales label.

#Running instructions
Go to the root folder and run the following command:

scrapy crawl visionsSpider
