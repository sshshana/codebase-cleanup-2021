import os
from pandas import read_csv
from app.shopping import format_usd, lookup_product

def to_usd(my_price):
    """
    Formats a number as USD with dollar sign and two decimals (and also thousands separator)

    Params my_price is a number (int or float) that we want to format

    Examples: format_usd(10) / Result: $10.00
    """
    return f"${my_price:,.2f}"


def test_lookups():
    valid_result = lookup_product("8", mock_products)
    assert valid_result == {
        'aisle': "Aisle C",
        'department': 'snacks',
        'id': '8',
        'name': 'Product 8'
        'price': 10.0

    }



mock_products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
mock_products_df = read_csv(products_filepath)
mock_products = products_df.to_dict("records")
