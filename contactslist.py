# function for adding contact (dict) to the contacts (list)
def add_contact(contacts):
    while True:
        name = input('Please, enter the name of the contact:\n')
        names = [c['name'] for c in contacts]
        if not names or name not in names:
            break
        else:
            print('This name is already in the contacts! Please enter unique name')
    while True:
        phone = input('Enter phone number of the contact:\n(12 digits)\n')
        if phone.isdigit() and len(phone) == 12:
            break
        else:
            print('Wrong number! Please enter correct phone number')
    contacts.append({'name': name, 'phone': phone})
    print()


# deleting contact by name
def del_by_name(contacts):
    name = input('Enter the name of contact for deleting:\n')
    for i in range(len(contacts)):
        if contacts[i]['name'] == name:
            del contacts[i]
            print(f'Contact {name} was successfully deleted')
            break
    else:
        print(f'The name {name} was not found')
    print()


# searching contact in list by name
def search_name(contacts):
    name = input('Enter the name of contact for searching:\n')
    for cont in contacts:
        if cont['name'] == name:
            print(f'Contact name: {name} \nphone number: {cont["phone"]}')
            break
    else:
        print(f'The name {name} was not found')
    print()


# searching contact in list by phone number
def search_number(contacts):
    number = input('Enter phone number of contact for searching:\n')
    for cont in contacts:
        if cont['phone'] == number:
            print(f'Contact name: {cont["name"]} \nphone number: {number}')
            break
    else:
        print(f'Phone number {number} was not found')
    print()


# main program
contacts_list = []
while True:
    print('Select the option you want to use (enter an integer):')
    choice = input("""1 - add new contact \n2 - delete contact \n3 - search contact by name
4 - search contact by phone number \n5 - close the program\n""")
    match choice:
        case '1':
            add_contact(contacts_list)
        case '2':
            del_by_name(contacts_list)
        case '3':
            search_name(contacts_list)
        case '4':
            search_number(contacts_list)
        case '5':
            break
        case _:
            print('Incorrect input')
