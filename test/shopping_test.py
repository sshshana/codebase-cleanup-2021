import os
from pandas import read_csv
from app.shopping import format_usd, lookup_product

def test_format_usd():
    assert format_usd(9.5) == "$9.50"


mock_products_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "mock_products.csv")
mock_products_df = read_csv(mock_products_filepath)
mock_products = mock_products_df.to_dict("records")

def test_lookups():
    valid_result = lookup_product("8", mock_products)
    assert valid_result == {
        'aisle': "Aisle C",
        'department': 'snacks',
        'id': 8,
        'name': 'Product 8',
        'price': 10.0
    }

    # with invalid product id, returns None:
    invalid_result = lookup_product("88888888", mock_products)
    assert invalid_result == None