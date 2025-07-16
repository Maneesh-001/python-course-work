
# 1. Product ID (int)
product_id = int(input("Enter Product ID (integer): "))

# 2. Product Name (str)
product_name = input("Enter Product Name: ")

# 3. Price (float)
price = float(input("Enter Price (e.g., 12.99): $"))

# 4. Categories (list)
categories_input = input("Enter categories (separated by commas): ")
categories = [cat.strip() for cat in categories_input.split(",")]

# 5. Stock Details (tuple)
available_stock = int(input("Enter available stock: "))
sold_items = int(input("Enter number of items sold: "))
stock_details = (available_stock, sold_items)

# 6. Discount Percentage (float)
discount = float(input("Enter discount percentage (e.g., 15 for 15%): "))

# 7. Product Features (set)
features_input = input("Enter unique features (separated by commas): ")
product_features = {feature.strip() for feature in features_input.split(",")}

# 8. Supplier Details (dict)
supplier_name = input("Enter supplier name: ")
supplier_contact = input("Enter supplier contact number: ")
supplier_location = input("Enter supplier location: ")
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# Display collected data
print("\n" + "="*60)
print("Collected Product Information (Amazon Music Style)")
print("="*60)

print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Categories: {categories}")
print(f"Stock Details (Available, Sold): {stock_details}")
print(f"Discount: {discount}%")
print(f"Product Features: {product_features}")
print(f"Supplier Details: {supplier_details}")
print("="*60)





# --- Assuming values are already collected from Task 1 ---
# If running separately, include the input section from Task 1 above

# Display using Comma Separation
print("\n" + "-"*60)
print("Product Details Using Comma Separation (sep=',')")
print("-"*60)
print("Stock (Available, Sold):", stock_details[0], stock_details[1], sep=', ')
print("Discount:", discount, "%", sep='')
print("Features:", *product_features, sep=', ')
print("Supplier:", supplier_details['name'], supplier_details['contact'], supplier_details['location'], sep=', ')

# Display using Percentage (%) Formatting
print("\n" + "-"*60)
print("Product Details Using Percentage Formatting")
print("-"*60)
print("Product ID: %d" % product_id)
print("Product Name: %s" % product_name)
print("Price: $%.2f" % price)
print("Discount: %.1f%%" % discount)
print("Stock: Available = %d, Sold = %d" % stock_details)
print("Supplier: %s, %s, %s" % (supplier_details['name'], supplier_details['contact'], supplier_details['location']))

# Display using f-strings
print("\n" + "-"*60)
print("Product Details Using f-Strings")
print("-"*60)
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Categories: {', '.join(categories)}")
print(f"Stock: Available = {stock_details[0]}, Sold = {stock_details[1]}")
print(f"Discount: {discount:.1f}%")
print(f"Features: {', '.join(product_features)}")
print(f"Supplier: {supplier_details['name']}, {supplier_details['contact']}, {supplier_details['location']}")

# Display using .format() method
print("\n" + "-"*60)
print("Product Details Using .format() Method")
print("-"*60)
print("Product ID: {}".format(product_id))
print("Product Name: {}".format(product_name))
print("Price: ${:.2f}".format(price))
print("Categories: {}".format(", ".join(categories)))
print("Stock: Available = {}, Sold = {}".format(*stock_details))
print("Discount: {:.1f}%".format(discount))
print("Features: {}".format(", ".join(product_features)))
print("Supplier: {}, {}, {}".format(
    supplier_details['name'],
    supplier_details['contact'],
    supplier_details['location']
))
