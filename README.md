# Ana Marcela N. - Visions Crawler
This is my assessment for the 360pi assessment challenge.

#Description
My crawler goes to the www.visions.ca website and checks every category to obtain the title, url, regular price, sale price and availability for each product and a second spider returns all the category names and url's. Each product and category information is written to a text file and a JSON file that can be found in the root folder once the spider has been run.

I created two spiders: 
* "visionsSpider" (visions_spider.py): This spider returns all the product information and writes into a JSON file named "visionsSpider.json" and a text file named "visionsSpider.txt" found in the root folder.
* "categorySpider" (category_spider.py): This spider returns all the categories available on the website and writes the results to a JSON file named "categorySpider.json" and a text file named "categorySpider.txt" found in the root folder.

#Things to consider
To complete the challenge I had to assume the following:
* The categories include what is listed on the site as departments, categories for each department and the subcategories displayed on the menu.
* Availability is whether or not you can buy a product online. If you can add a product to your cart, the product is available online, if not, the product is not available online.

#Special Scenarios:
Two specials scenarios can happen on the site:
* A product does not have a price listed (sale or regular price). For this case I only display the availability, category, title and url.
E.g.: http://www.visions.ca/Catalogue/Category/Details.aspx?categoryId=599&productId=26638&sku=BXPERIAZ3COMP
* A product only has a regular price. On the website the price is then shown as the regular price (styling) however, on code, the price displayed is using the sales label. For this case I had to create a condition that switches the "sale price" for the "regular price".

#Running instructions
To get the categories available on the website, go to the root folder and run the following command:

scrapy crawl categorySpider

To get the products information, go to the root folder and run the following command:

scrapy crawl visionsSpider
