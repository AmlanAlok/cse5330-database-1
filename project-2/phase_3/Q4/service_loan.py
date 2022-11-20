from repository import *
from service import *


def get_book_loan(member_id, isbn):
    validate_member = validate_member_for_loan(member_id)

    if validate_member == 'Success':

        validate_loan = validate_lending_for_loan(isbn)

        if validate_loan == "Success":

            pass
        else:
            return validate_loan


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
