import os
from datetime import datetime
from pandas import read_csv

def format_usd(my_price):
    """
    Formats a number as USD with dollar sign and two decimals (and also thousands separator)

    Parameter my_price is a number (int or float) that we want to format

    Examples: format_usd(10) / Result: $10.00
    """
    return f"${my_price:,.2f}"

def lookup_product(product_id, all_products):
    """
    Params:
        product_id (str) like "8"
        all_products (list of dict) each dict should have "id", "name", "department", "aisle", and "price" attributes
    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None

def receipt_summary(selected_products):
    """
    Params:
        selected_products (list of dict) each dict should have "id", "name", "department", "aisle", and "price" attributes
    """
    return f"""---------
SUBTOTAL: {format_usd(subtotal)}
TAX: {format_usd(tax)}
TOTAL: {format_usd(total)}
---------
THANK YOU! PLEASE COME AGAIN SOON!
---------
    """

if __name__ == "__main__":

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
            matching_product = lookup_product(selected_id, products)
            if matching_product:
                selected_products.append(matching_product)
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
        print("SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))
    print(receipt_summary(selected_products))


    # WRITE RECEIPT TO FILE

    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("---------")
        for p in selected_products:
            receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))
        receipt_file.write("\n---------")
        receipt_file.write(receipt_summary(selected_products))

