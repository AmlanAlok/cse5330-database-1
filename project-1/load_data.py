import pymysql
import csv


def db_omega():
    print('Start DB connection Omega')

    # hostname = 'academicmysql.mysql.database.azure.com' # did not work
    # hostname = 'acadmysqldb001p'  # did not work
    hostname = '10.208.63.68'
    database = 'axa5861'
    username = 'axa5861'
    password = 'ArlingtonTexas'

    state_csv = 'dataset/005_Project1_Data/US_state.csv'

    load_csv_data(state_csv)

    try:
        connection = pymysql.connect(host=hostname, user=username, password=password, database=database, port=3306)
        cursor = connection.cursor()

        data = load_csv_data(state_csv)
        for i in range(1, len(data)):
            row = data[i]
            state_insert_query = 'insert into state values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(state_insert_query, row)
            # print(row)
        # sql_query = 'select version()'
        # cursor.execute(sql_query)
        # data = cursor.fetchone()
        # print('Version = ', data)

        connection.close()
    except Exception as e:
        print('Exception -> ', e)

    print('END')


def load_csv_data(filepath):
    with open(filepath) as file:
        data = list(csv.reader(file))
    return data


def preprocess_state_data(data):
    for x in data:
        x[7] = 0 if x[7] == 'No' else 1
        x[8] = 0 if x[8] == '' else x[8].replace(',', '')
        x[9] = 0 if x[9] == '' else x[9].replace(',', '')
    return data


def preprocess_county_data(data):
    c = 1
    for x in data:
        if x[1] == 'Unassigned':
            x[1] += str(c)
            c+=1
    return data


def insert_state(data, cursor):
    for i in range(1, len(data)):
        record = data[i]
        state_insert_query = 'insert into state values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(state_insert_query, record)


def insert_county(data, cursor):
    for i in range(1, len(data)):
        record = data[i]
        state_insert_query = 'insert into county values(%s, %s, %s, %s, %s)'
        cursor.execute(state_insert_query, record)


def insert_vaccination(data, cursor):
    for i in range(1, len(data)):
        record = data[i]
        state_insert_query = 'insert into vaccinations values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(state_insert_query, record)


def db_1():
    print('Start DB connection')

    hostname = 'localhost'
    username = 'root'
    password = ''
    database = 'us_covid_19_db'

    # connection = pymysql.connect(host=hostname, user=username, password=password, database=database)
    # cursor = connection.cursor()

    # sql_query = 'select version()'
    #
    # try:
    #     cursor.execute(sql_query)
    #     data = cursor.fetchone()
    #     print('Version = ', data)

    state_csv = 'dataset/005_Project1_Data/US_state.csv'
    state_data = preprocess_state_data(load_csv_data(state_csv))

    county_csv = 'dataset/005_Project1_Data/Us_County.csv'
    # county_data = preprocess_county_data(load_csv_data(county_csv))
    county_data = load_csv_data(county_csv)

    vaccination_csv = 'dataset/005_Project1_Data/US_Vaccination.csv'
    vaccination_data = load_csv_data(vaccination_csv)

    try:
        connection = pymysql.connect(host=hostname, user=username, password=password, database=database, port=3306)
        cursor = connection.cursor()

        insert_state(state_data, cursor)
        insert_county(county_data, cursor)
        insert_vaccination(vaccination_data, cursor)

        connection.commit()
        connection.close()
    except Exception as e:
        print('Exception -> ', e)
    print('END')


def main():
    # db_omega()
    db_1()


if __name__ == '__main__':
    main()
