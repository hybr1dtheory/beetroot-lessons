class Warehouse:
    def __init__(self):
        self.products = {}

    def add_new(self, name: str, amount: int, price: float):
        prod_id = 0
        if self.products:
            prod_id = max(self.products.keys()) + 1
        prod = {'name': name, 'amount': amount, 'price': price}
        self.products[prod_id] = prod
        return prod_id

    def add_to(self, prod_id: int, amount: int):
        self.products[prod_id]['amount'] += amount

    def del_prod(self, prod_id: int):
        del self.products[prod_id]

    def sell_prod(self, prod_id: int, amount: float):
        self.products[prod_id]['amount'] -= amount

    def search_prod(self, name):
        found_prods = []
        for prod_id, prod in self.products.items():
            if name in prod['name']:
                found_prods.append((prod_id, prod['name'], prod['amount'], prod['price']))
        return found_prods

    def get_info(self):
        count = len(self.products)
        total_amount = 0
        total_price = 0
        for prod in self.products.values():
            total_amount += prod['amount']
            total_price += prod['price'] * prod['amount']
        return count, total_amount, total_price


def add_product(wh: Warehouse):
    print('Select option (enter an integer):')
    ch = input('1 - add new product \n2 - add to existing product\n')
    match ch:
        case '1':
            name = input('Enter product name:\n')
            count = int(input('Enter amount of product (integer):\n'))
            price = float(input('Enter the price of the product (float):\n'))
            prod_id = wh.add_new(name, count, price)
            print(f'Product {name} with id {prod_id} was successfully added')
        case '2':
            prod_id = int(input('Enter product id:\n'))
            count = int(input('Enter amount of product to add:\n'))
            if prod_id in wh.products:
                wh.add_to(prod_id, count)
                print(f'Product with id {prod_id} was successfully updated')
            else:
                print(f'Product with id {prod_id} was not found!')
        case _:
            print('ERROR: Incorrect input')


def sell_product(wh: Warehouse):
    prod_id = int(input('Enter the id of the product to sell (integer):\n'))
    count = int(input('Enter amount of the product to sell (integer):\n'))
    if prod_id in wh.products:
        if wh.products[prod_id]['amount'] >= count:
            wh.sell_prod(prod_id, count)
            print(f'Product with id {prod_id} in the amount of {count} was excluded from warehouse')
        else:
            print(f'ERROR: Product id {prod_id} is available only in the amount of {wh.products[prod_id]["amount"]}')
    else:
        print(f'ERROR: Product with id {prod_id} was not found!')


def print_general_info(wh: Warehouse):
    prods, total_cnt, total_cost = wh.get_info()
    print('General information about warehouse:')
    print(f'Unique items: {prods}', f'Total amount: {total_cnt}', f'Total cost: {total_cost}', sep='\n')


def print_full_list(wh: Warehouse):
    if wh.products:
        print('Product ID', 'NAME', 'AMOUNT', 'PRICE', sep='\t')
        for pid, prod in sorted(wh.products.items(), key=lambda x: x[1]['name']):
            print(pid, prod['name'], prod['amount'], prod['price'], sep='\t')
    else:
        print('There are no products in the warehouse')


# main program
warehouse = Warehouse()
print('Welcome to warehouse program!\n')
while True:
    print_full_list(warehouse)
    print('Select the option you want to use (enter an integer):')
    choice = input("""1 - add new product \n2 - exclude products for sale 
3 - print general info \n4 - close the program\n""")
    match choice:
        case '1':
            add_product(warehouse)
        case '2':
            sell_product(warehouse)
        case '3':
            print_general_info(warehouse)
        case '4':
            break
        case _:
            print('Incorrect input')
