from entities import *
import datetime


def add_new_member(member_name, ssn, campus_address, home_address, phone_number):
    date_today = datetime.date.today()
    card_issue_date = date_today.strftime('%Y-%m-%d')
    card_expiry_date = date_today.replace(year=date_today.year + MEMBERSHIP_LENGTH).strftime('%Y-%m-%d')

    member_type_id = get_fk(table_name=MEMBER_TYPE_DICT[TABLE_NAME],
                            col_name=MEMBER_TYPE_DICT[COL_NAME],
                            field_value=STANDARD)

    member_status_id = get_fk(table_name=MEMBER_STATUS_DICT[TABLE_NAME],
                              col_name=MEMBER_STATUS_DICT[COL_NAME],
                              field_value=ACTIVE)

    db_record = [member_name, ssn, campus_address, home_address, phone_number,
                 card_issue_date, card_expiry_date, INIT_BORROWED_COUNT,
                 member_type_id, member_status_id]

    return save_member(db_record)


def add_new_book(title, description, book_category_id, author_id, subject_area_id, binding_id, lang_id, book_fk_lists):
    db_record = [title, description, book_category_id, author_id, subject_area_id, binding_id, lang_id]
    saving_book, isbn = save_book(db_record)

    status = ''
    book_category_dict = get_book_category_dict(book_fk_lists['book_category_list'])

    if saving_book == 'Success':
        if book_category_id == book_category_dict['can be lent']:
            available_count = int(input('How many copies? '))
            loan_count = 0
            lending_record = [loan_count, available_count, isbn]
            status, book_for_lending_id = save_book_for_lending(lending_record)
            return status, isbn
        elif book_category_id == book_category_dict['interested to acquire']:
            print(book_fk_lists['reason_list'])
            reason_id = int(input('Choose one of the above reasons: '))
            interest_to_acquire_record = [isbn, reason_id]
            status, interested_to_acquire_id = save_interest_to_acquire(interest_to_acquire_record)
            return status, isbn
        else:
            return saving_book, isbn
    else:
        return saving_book, isbn


def get_book_category_dict(book_category_list):
    book_category_dict = {}

    for (i, v) in enumerate(book_category_list):
        book_category_dict[v[1]] = v[0]

    return book_category_dict


def get_book_fk_list():
    book_fk_list_dict = {
        'lang_list': get_all(LANG),
        'binding_list': get_all(BINDING),
        'subject_area_list': get_all(SUBJECT_AREA),
        'author_list': get_all(AUTHOR),
        'book_category_list': get_all(BOOK_CATEGORY),
        'reason_list': get_all(REASON)
    }

    return book_fk_list_dict


def validate_lending_for_loan(isbn):
    lending_record = get_record(table_name=BOOK_FOR_LENDING_DICT[TABLE_NAME], col_name=BOOK_FOR_LENDING_DICT[COL_NAME],
                                field_value=isbn)

    if lending_record:
        pk, loan_count, available_count = lending_record[0], lending_record[1], lending_record[2]

        if available_count == 0:
            return 'No copies available to lend at the moment'
        elif available_count > 0:
            update_status = update_book_for_lending(str(loan_count + 1), str(available_count - 1), str(pk))
            return update_status
    else:
        return 'This book is not for lending'


'''to check if he is within limit ot borrow'''

def get_member_status(member_status_id):
    member_status_record = get_record(table_name=MEMBER_STATUS_DICT[TABLE_NAME], col_name=MEMBER_STATUS_DICT[COL_NAME],
                                      field_value=member_status_id)
    return member_status_record[1]


def get_member_limit(member_type_id):
    member_type_record = get_record(table_name=MEMBER_STATUS_DICT[TABLE_NAME], col_name=MEMBER_STATUS_DICT[COL_NAME],
                                      field_value=member_type_id)
    return member_type_record[4]


def validate_member_for_loan(member_id):
    member_record = get_record(table_name=MEMBER_DICT[TABLE_NAME], col_name=MEMBER_DICT[COL_NAME],
                                field_value=member_id)

    member_type_id, member_status_id = member_record[9], member_record[10]
    borrow_count = member_record[8]

    member_status = get_member_status(member_status_id)

    if member_status == 'active':
        member_book_limit = get_member_limit(member_type_id)

        if borrow_count < member_book_limit:
            return 'Success'
        else:
            return 'Member has borrows books to their allowed limit'

    else:
        return 'Member is inactive. Cannot loan a book'


def get_book_loan(member_id, isbn):
    validate_member = validate_member_for_loan(member_id)

    if validate_member == 'Success':

        validate_loan = validate_lending_for_loan(isbn)

        if validate_loan == "Success":

            pass
        else:
            return update_status


if __name__ == '__main__':
    # get_member_status_active()
    print('start')
