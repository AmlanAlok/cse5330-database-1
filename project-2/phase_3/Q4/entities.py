import pymysql

HOSTNAME = 'hostname'
USERNAME = 'username'
PASSWORD = 'password'
DATABASE = 'database'

LOCAL_DB = {
    HOSTNAME: 'localhost',
    USERNAME: 'root',
    PASSWORD: '',
    DATABASE: 'axa5861'
}

OMEGA_DB = {
    HOSTNAME: '10.208.63.68',
    USERNAME: 'axa5861',
    PASSWORD: 'ArlingtonTexas',
    DATABASE: 'axa5861'
}

DB = LOCAL_DB


def connect_db_fetch_data(sql_query):

    # hostname = '10.208.63.68'
    # database = 'axa5861'
    # username = 'axa5861'
    # password = 'ArlingtonTexas'

    hostname = 'localhost'
    username = 'root'
    password = ''
    database = 'axa5861'


    try:
        print('Start DB connection')
        # connection = pymysql.connect(host=hostname, user=username, password=password, database=database, port=3306)
        connection = pymysql.connect(host=DB[HOSTNAME], user=DB[USERNAME], password=DB[PASSWORD], database=DB[DATABASE], port=3306)
        cursor = connection.cursor()

        cursor.execute(sql_query)
        output = cursor.fetchone()

        connection.close()

        return output[0]
    except Exception as e:
        print('Exception -> ', e)


def connect_db_save_data(sql_query, db_record):

    # hostname = '10.208.63.68'
    # database = 'axa5861'
    # username = 'axa5861'
    # password = 'ArlingtonTexas'

    hostname = 'localhost'
    username = 'root'
    password = ''
    database = 'axa5861'

    try:
        print('Start DB connection')
        connection = pymysql.connect(host=hostname, user=username, password=password, database=database, port=3306)
        cursor = connection.cursor()

        cursor.execute(sql_query, db_record)
        connection.commit()
        connection.close()

        return 'Success'
    except Exception as e:
        print('Exception -> ', e)


def get_member_status_fk(member_status):
    sql_query = "select id from member_status where member_status = '" + member_status + "'"
    fk_id = connect_db_fetch_data(sql_query)
    print(fk_id)


def get_fk(table_name, col_name, field_value):
    # sql_query = "select id from '" + table_name + "' where '" + col_name + "' = '" + field_value + "'"
    sql_query = "select id from " + table_name + " where " + col_name + " = '" + field_value + "'"
    fk_id = connect_db_fetch_data(sql_query)
    return fk_id


def save_member():
    sql_query = "insert into member (`member_name`,`ssn`,`campus_address`,`home_address`,`phone_no`) values " \
                "(%s, %s, %s, %s, %s)"
    # cursor.execute(d_query, db_record)

if __name__ == '__main__':
    get_member_status_fk('active')