
-- Q3 report query
select sa.subject_area,a.author_name,b.isbn, b.title, bm.date_of_borrowing,  date(now()) - bm.date_of_borrowing as `Days Since Borrowed`, mt.borrowing_period_limit as `Number of Days Loaned`,
bfl.loan_count as 'Number of Copies'
from book_member as bm
join book as b on b.isbn = bm.book_isbn
join author as a on a.id = b.author_id
join subject_area as sa on sa.id = b.subject_area_id
join member as m on m.id = bm.member_id
join member_type as mt on mt.id = m.member_type_id
join book_for_lending as bfl on bfl.book_isbn=b.isbn
where bm.date_of_borrowing >= (select Date(now()-interval 7 day))
order by sa.subject_area, a.author_name,bfl.loan_count,date(now()) - bm.date_of_borrowing;

