import pymysql
import csv


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


def preprocess_confirmed_cases_data(data, cursor, connection):
    print("Loading CC's---------------------------------------------------------")
    state_row, county_row = data[0], data[1]

    for state_county_idx in range(1, len(state_row)):
        state = state_row[state_county_idx]
        county = county_row[state_county_idx]

        county_clean = county.replace("'", "''")

        present = check_state_county(state, county_clean, cursor)

        if present == 1:
            # up to down
            print('State = ', state, ' County = ', county)

            for i in range(2, len(data)):

                date_raw = data[i][0]
                date_parts = date_raw.split('/')
                date = date_parts[2] + '-' + date_parts[0] + '-' + date_parts[1]

                count = data[i][state_county_idx]
                db_record = [state, county, date, count]
                confirmed_cases_query = 'insert into confirmed_cases values(%s, %s, %s, %s)'
                cursor.execute(confirmed_cases_query, db_record)

            connection.commit()

    return 'Done---------'


def preprocess_deaths_data(data, cursor, connection):
    print("Loading D's---------------------------------------------------------")
    state_row, county_row = data[0], data[1]

    for state_county_idx in range(1, len(state_row)):
        state = state_row[state_county_idx]
        county = county_row[state_county_idx]

        county_clean = county.replace("'", "''")

        present = check_state_county(state, county_clean, cursor)

        if present == 1:
            # up to down
            print('State = ', state, ' County = ', county, ' state_county_idx =', state_county_idx)

            for i in range(2, len(data)):
                date_raw = data[i][0]
                date_parts = date_raw.split('/')
                date = date_parts[2] + '-' + date_parts[0] + '-' + date_parts[1]

                d_count = data[i][state_county_idx]
                db_record = [state, county, date, d_count]
                d_query = 'insert into deaths values(%s, %s, %s, %s)'
                cursor.execute(d_query, db_record)

            connection.commit()

    return 'Done---------'


def check_state_county(state, county, cursor):
    sql_query = "select count(*) from county where county = '" + county + "' and state = '" + state + "'"
    cursor.execute(sql_query)
    is_present = cursor.fetchone()
    return is_present[0]


def check_state(state, cursor):
    sql_query = "select count(*) from state where state = '" + state + "'"
    cursor.execute(sql_query)
    is_present = cursor.fetchone()
    return is_present[0]


def insert_state(data, cursor):
    for i in range(1, len(data)):
        record = data[i]
        state_insert_query = 'insert into state values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(state_insert_query, record)


def insert_county(data, cursor):
    for i in range(1, len(data)):
        record = data[i]
        state_name = record[0]

        present = check_state(state_name, cursor)

        if present == 1:
            state_insert_query = 'insert into county values(%s, %s, %s, %s, %s)'
            cursor.execute(state_insert_query, record)


def insert_vaccination(data, cursor):
    for i in range(1, len(data)):
        record = data[i]
        state_name = record[0]

        present = check_state(state_name, cursor)

        if present == 1:
            state_insert_query = 'insert into vaccinations values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(state_insert_query, record)


def db_omega():

    # Omega DB connection
    hostname = '10.208.63.68'
    database = 'axa5861'
    username = 'axa5861'
    password = 'ArlingtonTexas'

    # # local DB connection
    # hostname = 'localhost'
    # username = 'root'
    # password = ''
    # database = 'us_covid_19_db'

    state_csv = 'dataset/005_Project1_Data/US_state.csv'
    state_data = preprocess_state_data(load_csv_data(state_csv))

    county_csv = 'dataset/005_Project1_Data/Us_County.csv'
    # county_data = preprocess_county_data(load_csv_data(county_csv))
    county_data = load_csv_data(county_csv)

    vaccination_csv = 'dataset/005_Project1_Data/US_Vaccination.csv'
    vaccination_data = load_csv_data(vaccination_csv)

    confirmed_cases_csv = 'dataset/005_Project1_Data/Us_confirmed_cases.csv'
    # confirmed_cases_data = preprocess_confirmed_cases_data(load_csv_data(confirmed_cases_csv))

    d_csv = 'dataset/005_Project1_Data/Us_deaths.csv'

    print('checkpoint')

    try:
        print('Start DB connection')
        connection = pymysql.connect(host=hostname, user=username, password=password, database=database, port=3306)
        cursor = connection.cursor()

        insert_state(state_data, cursor)
        connection.commit()
        print('State data inserted')

        print('County data started')
        insert_county(county_data, cursor)
        connection.commit()
        print('County data inserted')

        print('Vaccination data started')
        insert_vaccination(vaccination_data, cursor)
        connection.commit()
        print('Vaccination data inserted')

        print('D data started')
        dc = preprocess_deaths_data(load_csv_data(d_csv), cursor, connection)
        print(dc)
        print('D data inserted')

        print('Confirmed Cases data started')
        cc = preprocess_confirmed_cases_data(load_csv_data(confirmed_cases_csv), cursor, connection)
        print(cc)
        print('Confirmed Cases data inserted')

        connection.close()
    except Exception as e:
        print('Exception -> ', e)
    print('END')


def main():
    db_omega()


if __name__ == '__main__':
    main()
