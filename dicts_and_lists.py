def get_profit():
    nbr_products=int(input("enter the nbr of the products : "))
    products=[]
    for i in range (nbr_products):
        product={}
        product_name=input("enter the prodct name : ").lower()
        cost_price=float(input("enter the cost price: "))
        sell_price=float(input("enter the sell price: "))
        inventory=int(input("enter inventory: "))
        profit=inventory*(sell_price - cost_price)
        product['name']=product_name
        product['cost price']=cost_price
        product['sell price']=sell_price
        product['inventory']=inventory
        product['profit']=profit
        products.append(product)
    for product in products:
        print(f"the profit of '{product['name']}' is: '{product['profit']}")
    return products
print(get_profit())