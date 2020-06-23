import pytest # type: ignore
from classic_strategy import (Customer, LineItem, Order, FidelityPromo, BulkItemPromo,
                              LargeOrderPromo)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

def test_single_item_order():
    cart = [LineItem('banana', 4, .5)]
    assert repr(Order(joe, cart, FidelityPromo())) == '<Order total: 2.00 due: 2.00>'

def test_fidelity_promo():
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    
    assert repr(Order(joe, cart, FidelityPromo())) == '<Order total: 42.00 due: 42.00>'
    assert repr(Order(ann, cart, FidelityPromo())) == '<Order total: 42.00 due: 39.90>'

def test_bulk_item_promo():
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    assert repr(Order(joe, banana_cart, BulkItemPromo())) == '<Order total: 30.00 due: 28.50>'
     
def test_large_order_promo():
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    assert repr(Order(joe, long_order, LargeOrderPromo())) == '<Order total: 10.00 due: 9.30>'

if __name__ == "__main__":
  pytest.main()