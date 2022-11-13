
use library;

select * from book_type;
select * from book_category;
select * from author;
select * from subject_area;
select * from staff_position;
select * from member_status;
select * from member_type;

-- display all books
select b.isbn, b.title, bc.book_category, a.author_name, sa.subject_area, bnd.bind_type, l.language_name
from book as b
join book_category as bc on bc.id = b.book_category_id
join author as a on a.id = b.author_id
join subject_area as sa on sa.id = b.subject_area_id
join binding as bnd on bnd.id = b.binding_id
join lang as l on l.id = b.lang_id;



-- display books interested to acquire
select b.isbn, b.title, bc.book_category, a.author_name, sa.subject_area, bnd.bind_type, l.language_name
from book as b
join interested_to_acquire as ia on b.isbn = ia.book_isbn
join book_category as bc on bc.id = b.book_category_id
join author as a on a.id = b.author_id
join subject_area as sa on sa.id = b.subject_area_id
join binding as bnd on bnd.id = b.binding_id
join lang as l on l.id = b.lang_id
join reason as r on r.id = ia.reason_id;
