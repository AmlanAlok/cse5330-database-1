


def display_menu():
    print('Choose one of the below numbers for corresponding actions')
    print('1. New Member')

    option = int(input('Choose Option'))
    return option


def new_member():
    print('Enter new member information below')
    member_name = input('Member Name')
    ssn = input('SSN')
    campus_address = input('Campus Address')
    home_address = input('Home Address')
    phone_number = input('Phone Number')




def main():
    option = display_menu()
    if option == 1:
        new_member()




if __name__ == '__main__':
    main()