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


def add_new_book(title, description, book_category_id, author_id, subject_area_id, binding_id, lang_id):

    db_record = [title, description, book_category_id, author_id, subject_area_id, binding_id, lang_id]

    saving_book = save_book(db_record)

    if saving_book == 'Success':
        pass
    else:
        return saving_book




def get_book_fk_list():

    book_fk_list_dict = {
        'lang_list': get_all(LANG),
        'binding_list': get_all(BINDING),
        'subject_area_list': get_all(SUBJECT_AREA),
        'author_list': get_all(AUTHOR),
        'book_category_list': get_all(BOOK_CATEGORY),
        'reason_list': get_all(REASON)
    }

    book_category_dict = {}

    for (i, v) in enumerate(book_fk_list_dict['book_category_list']):
        book_category_dict[v[1]] = v[0]

    return book_fk_list_dict, book_category_dict


if __name__ == '__main__':
    # get_member_status_active()
    print('start')




