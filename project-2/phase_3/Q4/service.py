from entities import *
from constants import *
import time
import datetime



def get_member_status_active():
    # print(get_member_status_fk(ACTIVE))
    print(get_fk(table_name=MEMBER_STATUS_DICT[TABLE_NAME], col_name=MEMBER_STATUS_DICT[COL_NAME], field_value=ACTIVE))
    print(get_fk(table_name=MEMBER_STATUS_DICT[TABLE_NAME], col_name=MEMBER_STATUS_DICT[COL_NAME], field_value=INACTIVE))


# def add_member():


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
                 card_issue_date, card_expiry_date, str(INIT_BORROWED_COUNT),
                 str(member_type_id), str(member_status_id)]

    return save_member(db_record)


if __name__ == '__main__':
    get_member_status_active()




