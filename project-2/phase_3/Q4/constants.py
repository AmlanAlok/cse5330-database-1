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

TABLE_NAME = 'table_name'
COL_NAME = 'col_name'
PK = 'pk'


ACTIVE = 'active'
INACTIVE = 'inactive'
MEMBER_STATUS = 'member_status'
MEMBER_STATUS_DICT = {
    TABLE_NAME: MEMBER_STATUS,
    COL_NAME: MEMBER_STATUS,
    PK: 'id'
}

STANDARD = 'standard'
PROFESSOR = 'professor'
MEMBER_TYPE = 'member_type'
MEMBER_TYPE_DICT = {
    TABLE_NAME: MEMBER_TYPE,
    COL_NAME: MEMBER_TYPE,
    PK: 'id'
}

MEMBERSHIP_LENGTH = 4
INIT_BORROWED_COUNT = 0

LANG = 'lang'
BINDING = 'binding'
SUBJECT_AREA = 'subject_area'
AUTHOR = 'author'
BOOK_CATEGORY = 'book_category'
REASON = 'reason'

BOOK_FOR_LENDING_DICT = {
    TABLE_NAME: 'book_for_lending',
    COL_NAME: 'book_isbn'
}

CARD_ISSUE_IDX = 'car_issue_idx'
CARD_EXPIRY_IDX = 'card_expiry_idx'
RENEWED_IDX = 'renewed_idx'

MEMBER_DICT = {
    TABLE_NAME: 'member',
    COL_NAME: 'id',
    CARD_ISSUE_IDX: 6,
    CARD_EXPIRY_IDX: 7,
    RENEWED_IDX: 11
}
