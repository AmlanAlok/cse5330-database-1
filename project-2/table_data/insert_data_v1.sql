
-- Base Data to be inserted before any other tables
insert into book_type (`name`) values ('lent');
insert into book_type (`name`) values ('cannot be lent');
insert into book_type (`name`) values ('interested to acquire');

insert into book_category (`name`) values ('rare');
insert into book_category (`name`) values ('out of print');
insert into book_category (`name`) values ('lost');
insert into book_category (`name`) values ('destroyed');

insert into subject_area (`name`) values ('Physics');
insert into subject_area (`name`) values ('Chemistry');
insert into subject_area (`name`) values ('Mathematics');

insert into staff_position (`name`) values ('Chief Librarian');
insert into staff_position (`name`) values ('Departmental Associate Librarian');
insert into staff_position (`name`) values ('Reference Librarian');
insert into staff_position (`name`) values ('Check-Out Staff');
insert into staff_position (`name`) values ('Library Assistants');

insert into member_status (`name`) values ('active');
insert into member_status (`name`) values ('inactive');

insert into member_type (`name`,`borrowing_period_limit`,`grace_period`,`book_limit`)
values ('standard',3,1,5);
insert into member_type (`name`,`borrowing_period_limit`,`grace_period`,`book_limit`)
values ('professor',12,2,50);

-- Other tables

insert into author (`name`) values ('Richard Feynman');
insert into author (`name`) values ('Alan Heeger');
insert into author (`name`) values ('Eddie Woo');

insert into book (`title`,`description`,`language`,`cover`,`book_type_id`,`author_id`,`subject_area_id`)
values ('Introduction to Physics','Learn physics','English','')

















