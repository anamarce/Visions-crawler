# Ana Marcela N. - Visions Crawler
This is my assesment for the 360pi assesment challenge.

#Description
My crawler goes to the www.visions.ca website and checks every category, obtains the title, url, regular price, sale price and availability for each product. Each product's information is written to a text file and a JSON file that can be found in the root folder once the spider has been run.

#Things to consider
To complete the challenge I had to assume the following:
* The Categories included what's listed on the site as Departments, subcategories for each department and the sub-subcategories displayed on the menu.
* Availability is whether or not you can add a product to your cart or just to your wishlist.

#Special Scenarios:
Two specials scenarios can happen on the site:
*A Product does not have a price listed (sale or regular price)
E.g.,: http://www.visions.ca/Catalogue/Category/Details.aspx?categoryId=599&productId=26638&sku=BXPERIAZ3COMP
*A Product only has a Regular Price, for this case I had to create a condition that switches the "sale price" for the "regular price". On the website the price is shown as the regular price (styling) however, on code, the price displayed is using the sales label.

#Running instructions
Go to the root folder and run the following:
scrapy crawl visionsSpider
