class Product:
    def __init__(self, ptype: str, name: str, price: float):
        self.type = ptype
        self.name = name
        self.price = price
        self.amount = 0

    def discount(self, percent):
        self.price = (self.price * percent) / 100

    def add(self, count: int):
        self.amount += count

    def sell(self, count: int):
        self.amount -= count


class ProductStore:
    def __init__(self):
        self._prod_list = []

    def add(self, product: Product, amount: int):
        if not isinstance(product, Product):
            raise ValueError("The product argument must be a Product type")
        product.price = product.price * 1.3
        self._prod_list.append(product.add(amount))

    def set_discount(self, identifier: str, percent: float, identifier_type="name"):
        if identifier_type not in ('name', 'type'):
            raise ValueError("The argument identifier_type may only be 'name' or 'type'")
        elif identifier_type == "name":
            for prod in self._prod_list:
                if prod.name == identifier:
                    prod.discount(percent)
        else:
            for prod in self._prod_list:
                if prod.type == identifier:
                    prod.discount(percent)

    def sell_product(self, prod_name: str, amount: int):
        for prod in self._prod_list:
            if prod_name == prod.name:
                if prod.amount >= amount:
                    prod.sell(amount)
                    break
                else:
                    print("The quantity of product is not enough to sell")
                    break
        else:
            print(f"The product with name {prod_name} was not found")
