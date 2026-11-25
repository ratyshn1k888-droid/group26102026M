import pytest
from models.shopping_cart import ShoppingCart


class TestShoppingCart:

    def setup_method(self):
        self.cart = ShoppingCart()
    def test_empty_cart(self):
        assert self.cart.items == []
    def test_add_item(self):
        self.cart.add_item('Apple', 10, 2)

        assert self.cart.items == [
            {
                'name': 'Apple',
                'price': 10,
                'quantity': 2
            }
        ]

    def test_add_existing_item(self):
        self.cart.add_item('Apple', 10, 2)
        self.cart.add_item('Apple', 15, 3)

        assert self.cart.items == [
            {
                'name': 'Apple',
                'price': 15,
                'quantity': 5
            }
        ]

    def test_remove_item(self):
        self.cart.add_item('Apple', 10, 2)
        self.cart.add_item('Banana', 20, 3)

        self.cart.remove_item('Apple')

        assert self.cart.items == [
            {
                'name': 'Banana',
                'price': 20,
                'quantity': 3
            }
        ]
    def test_remove_nonexistent_item(self):
        self.cart.add_item('Apple', 10, 2)

        self.cart.remove_item('Banana')

        assert len(self.cart.items) == 1
