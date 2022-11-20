from service import *


def display_menu():
    print('Choose one of the below numbers for corresponding actions')
    print('1. New Member')
    print('2. New Book')

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


def new_book():
    book_fk_lists, book_category_dict = get_book_fk_list()
    print(book_category_dict)
    print(book_fk_lists)
    print('Enter new book information below')
    title = input('Book Title: ')
    description = input('Description: ')
    print(book_fk_lists['author_list'])
    author_id = int(input('Choose one Author: '))
    print(book_fk_lists['subject_area_list'])
    subject_area_id = int(input('Choose subject area: '))
    print(book_fk_lists['binding_list'])
    binding_id = int(input('Choose binding type: '))
    print(book_fk_lists['lang_list'])
    lang_id = int(input('Choose language: '))
    print(book_fk_lists['book_category_list'])
    book_category_id = int(input('Choose book category: '))

    if book_category_id == book_category_dict['can be lent']:
        pass
    elif book_category_id == book_category_dict['interested to acquire']:
        pass
    else:
        add_new_book(title, description, book_category_id, author_id, subject_area_id, binding_id, lang_id)


def main():
    # option = display_menu()

    option = 2
    if option == 1:
        output = new_member()
    elif option == 2:
        output = new_book()

    print(output)




if __name__ == '__main__':
    main()