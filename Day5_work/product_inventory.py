
categories=[]
products=[]
stocks=[]
num_categories=int(input("Enter the number of categories: "))
for i in range (num_categories):
        category=input(f"Enter the name of category {i+1}: ")
        categories.append(category)
        num_products=int(input(f"Enter the number of products in {category}: "))
        product_list=[]
        stock_list=[]
        for j in range(num_products):
            product=input(f"Enter the name of product {j+1} for {category}: ")
            stock=int(input(f"Enter the stock for {product}: "))
            product_list.append(product)
            stock_list.append(stock)
        products.append(product_list)
        stocks.append(stock_list)
        print("     Inventory Report     ")
        for i in range(num_categories):
            print(f"\nCategory: {categories[i]}")
            for j in range(len(products[i])):
                print(f"{products[i][j]}: {stocks[i][j]} units")