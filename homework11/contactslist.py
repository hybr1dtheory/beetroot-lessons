from re import fullmatch


# function for adding contact (dict) to the contacts (list)
def add_contact(contacts):
    while True:
        try:
            name = input('Please, enter first name of the contact:\n')
            assert name.isalpha()
            surname = input('Please, enter last name of the contact:\n')
            assert surname.isalpha()
            break
        except AssertionError:
            print('Wrong input! Name and surname must contain only letters.')
        except Exception as e:
            print(f'Unexpected error: {e} \n Please try to enter data again')
    location = input('Enter the contact`s city or region of residence:\n')
    pattern = r'\+?3?8?0\d{9}'
    while True:
        phone = input('Enter phone number of the contact:\n(ukrainian number 10-12 digits with or without +)\n')
        m = fullmatch(pattern, phone)
        if m:
            break
        else:
            print('Wrong number! Please enter correct phone number')
    contacts.append({'name': name + ' ' + surname, 'location': location, 'phone': phone})
    print('New contact was successfully added!')
    print()


# deleting contact by name
def del_by_name(contacts):
    name = input('Enter the name, surname or full name of contact for deleting:\n')
    found = []
    for i in range(len(contacts)):
        if name in contacts[i]['name']:
            info = f'ID: {i} \t Name: {contacts[i]["name"]} Phone: {contacts[i]["phone"]}'
            found.append(info)
    if found:
        print('These contacts were found:', *found, sep='\n')
        try:
            cid = int(input('Enter the ID of contact you want to delete (integer):\n'))
            del contacts[cid]
            print(f'The contact with ID {cid} was successfully deleted')
        except ValueError:
            print('Wrong input! ID must be a number (integer)')
        except IndexError:
            print('Wrong input! This ID does not exist')
    else:
        print(f'The name {name} was not found')
    print()


# searching contact in list by location
def search_by_loc(contacts):
    loc = input('Enter the name of city or region to search:\n')
    found = []
    i = 1
    for c in contacts:
        if loc in c['location']:
            info = f'{i}. {c["phone"]} \t {c["name"]} ({c["location"]})'
            found.append(info)
            i += 1
    if found:
        print('These contacts were found:', *found, sep='\n')
    else:
        print(f'The contact with location {loc} was not found')
    print()


# searching contact in list by name
def search_by_name(contacts):
    name = input('Enter the name, surname or full name of contact to search:\n')
    found = []
    i = 1
    for c in contacts:
        if name in c['name']:
            info = f'{i}. {c["phone"]} \t {c["name"]} ({c["location"]})'
            found.append(info)
            i += 1
    if found:
        print('These contacts were found:', *found, sep='\n')
    else:
        print(f'The contact {name} was not found')
    print()


# searching contact in list by phone number
def search_by_number(contacts):
    number = input('Enter phone number of contact or part of it to search:\n')
    found = []
    i = 1
    for c in contacts:
        if number in c['phone']:
            info = f'{i}. {c["phone"]} \t {c["name"]} ({c["location"]})'
            found.append(info)
            i += 1
    if found:
        print('These contacts were found:', *found, sep='\n')
    else:
        print(f'The contact with number {number} was not found')
    print()


def update_contact(contacts):
    name = input('Enter the name, surname or full name of contact you want to update:\n')
    found = []
    for i in range(len(contacts)):
        if name in contacts[i]['name']:
            info = f'ID: {i} \t Name: {contacts[i]["name"]} Phone: {contacts[i]["phone"]}'
            found.append(info)
    if found:
        print('These contacts were found:', *found, sep='\n')
        while True:
            try:
                cid = int(input('Enter the ID of contact you want to update (integer):\n'))
                print(f'Start updating of the contact with ID {cid}\n')
                break
            except ValueError:
                print('Wrong input! ID must be a number (integer)')
            except IndexError:
                print('Wrong input! This ID does not exist')

        while True:
            print('Select the information you want to update (enter an integer):\n')
            choice = input("1 - Name \n2 - Phone number \n3 - location\n")
            match choice:
                case '1':
                    try:
                        name = input('Please, enter first name of the contact:\n')
                        assert name.isalpha()
                        surname = input('Please, enter last name of the contact:\n')
                        assert surname.isalpha()
                        contacts[cid]["name"] = name + ' ' + surname
                        break
                    except AssertionError:
                        print('Wrong input! Name and surname must contain only letters.')
                    except Exception as e:
                        print(f'Unexpected error: {e} \n Please try to enter data again')
                case '2':
                    pattern = r'\+?3?8?0\d{9}'
                    while True:
                        phone = input('Enter phone number:\n(ukrainian number 10-12 digits with or without +)\n')
                        m = fullmatch(pattern, phone)
                        if m:
                            contacts[cid]["phone"] = phone
                            break
                        else:
                            print('Wrong number! Please enter correct phone number')
                case '3':
                    location = input('Enter the contact`s city or region of residence:\n')
                    contacts[cid]["location"] = location
                case _:
                    print('Incorrect input')
        print('Contact was successfully updated!')
    else:
        print(f'The name {name} was not found')
    print()


def print_contacts(contacts):
    if len(contacts) > 0:
        for contact in sorted(contacts, key=lambda x: x["name"]):
            name, number, loc = contact.values()
            print(name.ljust(20), number, loc, sep='\t')
        print()
    else:
        print('Contact list is empty\n')
