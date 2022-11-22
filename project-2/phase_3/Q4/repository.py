from database_connection import *


def get_fk(table_name, col_name, field_value):
    sql_query = "select id from " + table_name + " where " + col_name + " = '" + field_value + "'"
    fk_id = connect_db_fetch_data(sql_query)
    return fk_id


def save_member(db_record):
    sql_query = "insert into member (`member_name`,`ssn`,`campus_address`,`home_address`,`phone_no`," \
                "`card_issue_date`,`card_expiry_date`,`borrowed_count`,`member_type_id`,`member_status_id`,`renewed`)" \
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


def save_book(db_record):
    sql_query = "insert into book (`title`, `description`, `book_category_id`, `author_id`, `subject_area_id`, " \
                "`binding_id`, `lang_id`) values (%s, %s, %s, %s, %s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


def save_book_for_lending(db_record):
    sql_query = "insert into book_for_lending (`loan_count`,`available_count`,`book_isbn`) values (%s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


def save_interest_to_acquire(db_record):
    sql_query = "insert into interested_to_acquire (`book_isbn`,`reason_id`) values (%s, %s)"
    return connect_db_save_data(sql_query, db_record)


def save_loan(db_record):
    sql_query = "insert into book_member (`book_isbn`,`member_id`,`date_of_borrowing`,`last_date_to_return`) " \
                "values (%s, %s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


def update_book_return(member_id, isbn, date_of_return):
    sql_query = "update book_member set date_of_return ='" + date_of_return + "' where member_id = '" + \
                member_id + "' and book_isbn = '" + isbn + "'"
    return connect_db_update_data(sql_query)


def update_book_for_lending(loan_count, available_count, pk):
    sql_query = "update book_for_lending set loan_count ='" + loan_count + "', available_count ='" \
                + available_count + "' where id = '" + pk + "'"
    return connect_db_update_data(sql_query)


def update_member_borrow_count(member_id, borrow_count):
    sql_query = "update member set borrowed_count = '" + borrow_count + "' where id = '" + member_id + "'"
    return connect_db_update_data(sql_query)


def update_member_renewal(member_id, card_issue_date, card_expiry_date, renewed_flag, member_status_id):
    print(member_id, card_issue_date, card_expiry_date, renewed_flag, member_status_id)
    sql_query = "update member set card_issue_date ='" + card_issue_date + "', card_expiry_date = '" + \
                card_expiry_date + "', renewed = '" + renewed_flag + \
                "', member_status_id = '" + member_status_id + \
                "' where id = '" + member_id + "'"

    return connect_db_update_data(sql_query)


def get_all(table_name):
    sql_query = "select * from " + table_name
    return connect_db_fetch_all(sql_query)


def get_record(table_name, col_name, field_value):
    sql_query = "select * from " + table_name + " where " + col_name + " = '" + str(field_value) + "'"
    return connect_db_fetch_record(sql_query)


def get_book_member(member_id, isbn):
    sql_query = "select * from book_member where member_id = '" + member_id + "' and book_isbn = '" + isbn + "'"
    return connect_db_fetch_record(sql_query)
