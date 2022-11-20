from entities import *

TABLE_NAME = 'table_name'
COL_NAME = 'col_name'

ACTIVE = 'active'
INACTIVE = 'inactive'


MEMBER_STATUS = 'member_status'
MEMBER_STATUS_DICT = {
    TABLE_NAME: 'member_status',
    COL_NAME: 'member_status'
}


def get_member_status_active():
    # print(get_member_status_fk(ACTIVE))
    print(get_fk(table_name=MEMBER_STATUS_DICT[TABLE_NAME], col_name=MEMBER_STATUS_DICT[COL_NAME], field_value=ACTIVE))
    print(get_fk(table_name=MEMBER_STATUS_DICT[TABLE_NAME], col_name=MEMBER_STATUS_DICT[COL_NAME], field_value=INACTIVE))


# def add_member():

if __name__ == '__main__':
    get_member_status_active()




