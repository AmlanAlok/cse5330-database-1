from database_connection import *


def get_fk(table_name, col_name, field_value):
    sql_query = "select id from " + table_name + " where " + col_name + " = '" + field_value + "'"
    fk_id = connect_db_fetch_data(sql_query)
    return fk_id


def save_member(db_record):
    sql_query = "insert into member (`member_name`,`ssn`,`campus_address`,`home_address`,`phone_no`," \
                "`card_issue_date`,`card_expiry_date`,`borrowed_count`,`member_type_id`,`member_status_id`) " \
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


def save_book(db_record):
    sql_query = "insert into book (`title`, `description`, `book_category_id`, `author_id`, `subject_area_id`, " \
                "`binding_id`, `lang_id`) values (%s, %s, %s, %s, %s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


def get_all(table_name):
    sql_query = "select * from " + table_name
    return connect_db_fetch_all(sql_query)


if __name__ == '__main__':
    # get_member_status_fk('active')
    print('start')
    print(type(x('lang')))