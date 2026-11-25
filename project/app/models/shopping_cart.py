class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):

        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                item['price'] = price
                return

        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def remove_item(self, name):

        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                return
