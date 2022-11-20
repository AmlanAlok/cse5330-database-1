from service import *


def display_menu():
    print('Choose one of the below numbers for corresponding actions')
    print('1. New Member')

    option = int(input('Choose Option'))
    return option


def new_member():
    print('Enter new member information below')
    member_name = input('Member Name: ')
    ssn = input('SSN: ')
    campus_address = input('Campus Address: ')
    home_address = input('Home Address: ')
    phone_number = input('Phone Number: ')

    return add_new_member(member_name, ssn, campus_address, home_address, phone_number)


def main():
    # option = display_menu()

    option = 1
    if option == 1:
        output = new_member()
    print(output)




if __name__ == '__main__':
    main()