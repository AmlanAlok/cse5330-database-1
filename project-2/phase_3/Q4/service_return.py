from repository import *
import datetime


def init_book_return(member_id, isbn):
    print('inside init_book_return')
    member_record = get_record(table_name=MEMBER_DICT[TABLE_NAME], col_name=MEMBER_DICT[COL_NAME],
                               field_value=member_id)

    date_today = datetime.date.today()
    date_of_return = date_today.strftime('%Y-%m-%d')

    status = update_book_return(member_id, isbn, date_of_return)

    if status == 'Success':
        lending_record = get_record(table_name=BOOK_FOR_LENDING_DICT[TABLE_NAME],
                                    col_name=BOOK_FOR_LENDING_DICT[COL_NAME],
                                    field_value=isbn)

        if lending_record:
            pk, loan_count, available_count = lending_record[0], lending_record[1], lending_record[2]

            update_status = update_book_for_lending(str(loan_count - 1), str(available_count + 1), str(pk))

            if update_status == 'Success':
                borrow_count = member_record[8] - 1
                borrow_count_status = update_member_borrow_count(str(member_id), str(borrow_count))

                if borrow_count_status == "Success":
                    book_member_rec = get_book_member(member_id, isbn)
                    date_of_borrowing = book_member_rec[2]

                    book_rec = get_record(table_name='book', col_name='isbn', field_value=isbn)
                    title = book_rec[1]

                    return 'Book returned successfully.\n Book Returned = ' + title + '\n Date of Borrowing = ' + \
                           str(date_of_borrowing) + '\nDate of Return = ' + str(date_of_return)
                else:
                    return 'Failed to update borrow count in member table'
            else:
                return 'Failed to update book for lending'
        else:
            return 'Lending record does not exist'
    else:
        return 'Updating book returned failed'
