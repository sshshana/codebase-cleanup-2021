import os
from datetime import datetime
from pandas import read_csv

def to_usd(my_price):
    """
    Formats a number as USD with dollar sign and two decimals (and also thousands separator)

    Params my_price is a number (int or float) that we want to format

    Examples: format_usd(10) / Result: $10.00
    """
    return f"${my_price:,.2f}"

# READ INVENTORY OF PRODUCTS

products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
products_df = read_csv(products_filepath)
products = products_df.to_dict("records")

# CAPTURE PRODUCT SELECTIONS

selected_products = []
while True:
    selected_id = input("Please select a product identifier: ")
    if selected_id.upper() == "DONE":
        break
    else:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        if any(matching_products):
            selected_products.append(matching_products[0])
        else:
            print("OOPS, Couldn't find that product. Please try again.")

checkout_at = datetime.now()

subtotal = sum([float(p["price"]) for p in selected_products])
tax = subtotal * 0.0875
total = subtotal + tax




# PRINT RECEIPT

print("---------")
print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
print("---------")
for p in selected_products:
    print("SELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"]))

print("---------")
print(f"SUBTOTAL: {to_usd(subtotal)}")
print(f"TAX: {to_usd(tax)}")
print(f"TOTAL: {to_usd(total}")
print("---------")
print("THANK YOU! PLEASE COME AGAIN SOON!")
print("---------")












# WRITE RECEIPT TO FILE

receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

with open(receipt_filepath, "w") as receipt_file:
    receipt_file.write("------------------------------------------")
    for p in selected_products:
        receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"]))

    receipt_file.write("\n---------")
    receipt_file.write(f"\nSUBTOTAL: {subtotal}")
    receipt_file.write(f"\nTAX: {tax}")
    receipt_file.write(f"\nTOTAL: {total}")
    receipt_file.write("\n---------")
    receipt_file.write("\nTHANK YOU! PLEASE COME AGAIN SOON!")
    receipt_file.write("\n---------")
