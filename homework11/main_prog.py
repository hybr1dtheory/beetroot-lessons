import json
from os import path
import contactslist as clst


contacts_list = []
file_name = 'contacts_data.json'
if path.isfile(file_name):
    with open(file_name, 'r') as f:
        contacts_list = json.load(f)

print('Welcome to the contacts list program!')
while True:
    print('Select the option you want to use (enter an integer):')
    choice = input("""1 - add new contact \n2 - delete contact \n3 - search by name \n4 - search by phone number 
5 - search contact by location \n6 - update contact info \n7 - print full list \n8 - close the program\n""")
    match choice:
        case '1':
            clst.add_contact(contacts_list)
        case '2':
            clst.del_by_name(contacts_list)
        case '3':
            clst.search_by_name(contacts_list)
        case '4':
            clst.search_by_number(contacts_list)
        case '5':
            clst.search_by_loc(contacts_list)
        case '6':
            clst.update_contact(contacts_list)
        case '7':
            clst.print_contacts(contacts_list)
        case '8':
            with open(file_name, 'w') as f:
                json.dump(contacts_list, f)
            break
        case _:
            print('Incorrect input')
