from repository import *
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

    renewed_flag_new_member = 0

    db_record = [member_name, ssn, campus_address, home_address, phone_number,
                 card_issue_date, card_expiry_date, INIT_BORROWED_COUNT,
                 member_type_id, member_status_id, renewed_flag_new_member]

    return save_member(db_record)


def renew_member(member_id):
    member_record = str(get_record(table_name=MEMBER_DICT[TABLE_NAME], col_name=MEMBER_DICT[COL_NAME],
                                   field_value=member_id))

    if member_record:

        date_today = datetime.date.today()
        card_issue_date = date_today.strftime('%Y-%m-%d')
        card_expiry_date = date_today.replace(year=date_today.year + MEMBERSHIP_LENGTH).strftime('%Y-%m-%d')

        renewed_flag = str(1)
        member_status_id = str(get_fk(table_name=MEMBER_STATUS_DICT[TABLE_NAME],
                                      col_name=MEMBER_STATUS_DICT[COL_NAME],
                                      field_value=ACTIVE))

        return update_member_renewal(member_id, str(card_issue_date), str(card_expiry_date), renewed_flag,
                                     member_status_id)

    else:
        return 'Member with this member_id not present in DB'
