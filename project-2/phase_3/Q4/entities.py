import pymysql
from constants import *

DB = LOCAL_DB


def connect_db_fetch_data(sql_query):

    try:
        print('Start DB connection')
        connection = pymysql.connect(host=DB[HOSTNAME], user=DB[USERNAME], password=DB[PASSWORD], database=DB[DATABASE],
                                     port=3306)
        cursor = connection.cursor()

        cursor.execute(sql_query)
        output = cursor.fetchone()

        connection.close()

        return output[0]
    except Exception as e:
        print('Exception -> ', e)
        return 'Failed'


def connect_db_save_data(sql_query, db_record):

    try:
        print('Start DB connection')
        connection = pymysql.connect(host=DB[HOSTNAME], user=DB[USERNAME], password=DB[PASSWORD], database=DB[DATABASE],
                                     port=3306)
        cursor = connection.cursor()

        cursor.execute(sql_query, db_record)
        connection.commit()
        connection.close()

        return 'Success'
    except Exception as e:
        print('Exception -> ', e)
        return 'Failed'


def get_fk(table_name, col_name, field_value):
    sql_query = "select id from " + table_name + " where " + col_name + " = '" + field_value + "'"
    fk_id = connect_db_fetch_data(sql_query)
    return fk_id


def save_member(db_record):
    sql_query = "insert into member (`member_name`,`ssn`,`campus_address`,`home_address`,`phone_no`," \
                "`card_issue_date`,`card_expiry_date`,`borrowed_count`,`member_type_id`,`member_status_id`) " \
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    return connect_db_save_data(sql_query, db_record)


if __name__ == '__main__':
    get_member_status_fk('active')