'''
    Shopify

    SCRIPT FOR PRIVATE APP ONLY!!!
'''


import shopify



API_KEY = '3f39jalskdjaklsjdaskldjas5c2400fc10c5'
PASSWORD = '22cd7593a2ed9a7f819b2dalskd234298'

shop_url = "https://%s:%s@SHOP-dev.myshopify.com/admin" % (API_KEY, PASSWORD)
#debug, helps when there is an error like::: <urlopen error [Errno 8] nodename nor servname provided, or not known>
print(shop_url)

shopify.ShopifyResource.set_site(shop_url)




# Show the methods to be used for the shopify OBJECT :
dir(shopify.Product)

'''

You can use the following too:
    type()
    dir()


    id()
    getattr()
    hasattr()
    globals()
    locals()
    callable()
'''



#search product by ID
product = shopify.Product.find(12312312345)


'''
    Search by handle, the CSV file from Shopify will give you only the handle.
    returns a list!
'''
product = shopify.Product.find(handle ='zula-dress')

#print the first element of the list and its ID
product[0].id

#delete the product, if there is a product
if product:
    product[0].destroy()



