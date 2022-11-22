
-- 4.1
select * from member;

-- 4.2
-- Add books to lend
select * from book;
select * from book_for_lending;

-- Add books interested to acquire
select * from book;
select * from interested_to_acquire;
select * from reason;

-- Add books not to be lent
select * from book where book_category_id = (select id from book_category where book_category = 'do not lend');