# Додати замовлення
def add_order(orders_list):
    if orders:
        add_id: int = orders_list[-1]['id'] + 1
    else:
        add_id = 0
    name = input('Enter client name:\n')
    n = int(input('Enter count of dishes in order:\n'))
    dishes = {}
    for i in range(n):
        print(f"""Enter the name of the dish #{i + 1} and the quantity of this dish in the order
(string and integer separated by a space) Please use correct names of dishes from menu:""")
        dish, amount = input().split()
        dishes[dish] = int(amount)
    order = {'id': add_id, 'name': name, 'dishes': dishes}
    orders_list.append(order)
    print(f'Order was successfully added to the list! Order id: {add_id}')


# Видалення замовлення
def del_order(orders_list, del_id: int):
    for i in range(len(orders_list)):
        if orders_list[i]['id'] == del_id:
            del orders_list[i]
            print(f'Order {del_id} was deleted')
            break
    else:
        print(f'Order {del_id} was not found in the list')


# Обчислення суми замовлення
def calc_order_amount(orders_list, price, calc_id):
    total = 0
    for order in orders_list:
        if order['id'] == calc_id:
            for d, p in order['dishes'].items():
                total += price[d] * p
            print(f'Total amount of the order {calc_id}: {total}')
            break
    else:
        print('Order {id} was not found in the list')


def print_orders(orders_list):
    for order in orders_list:
        print(f'Order {order["id"]}: {order["name"]}')
        for d, cnt in order['dishes'].items():
            print('\t', d, '-', cnt)


menu = {'BurgerM': 80, 'BurgerL': 100, 'BurgerXL': 120,
        'Hotdog': 70, 'KebabM': 90, 'KebabL': 110, 'KebabXL': 130}

# Main program
orders = []
print('New list of orders was created. You can start working with it.')
print('Actual menu:')
for k, v in menu.items():
    print(k, '-', v, 'UAH')
while True:
    print('Select the option you want to use (enter an integer):')
    choice = input("""1 - add new order \n2 - delete order \n3 - calculate total amount of the order
4 - print orders \n5 - close the program\n""")
    match choice:
        case '1':
            add_order(orders)
        case '2':
            order_id = int(input('Enter id of the order you want to delete:\n'))
            del_order(orders, order_id)
        case '3':
            order_id = int(input('Enter id of the order you want to calculate:\n'))
            calc_order_amount(orders, menu, order_id)
        case '4':
            print_orders(orders)
        case '5':
            break
        case _:
            print('Incorrect input')
