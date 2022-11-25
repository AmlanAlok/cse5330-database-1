


-- 5.1

USE `axa5861`$$
CREATE DEFINER = CURRENT_USER TRIGGER `axa5861`.`book_member_insert_overdue`
AFTER INSERT ON `book_member`
FOR EACH ROW

BEGIN
	if (select count(*)
		from book_member
        where member_id = new.member_id
        and (select CURDATE()) > last_date_to_return
        and date_of_return is null) > 0 then
		insert into `axa5861`.`notification` (`type`, `member_id`, `datetime`)
		values ('overdue', new.member_id, (select NOW()));
    end if;
END$$


-- 5.2

USE `axa5861`;

DELIMITER $$
USE `axa5861`$$
CREATE DEFINER = CURRENT_USER TRIGGER `axa5861`.`member_update_renewal`
AFTER UPDATE ON `member`
FOR EACH ROW
BEGIN
	if new.renewed = 1 and new.card_issue_date = (select CURDATE()) then
		insert into `axa5861`.`notification` (`type`, `member_id`, `datetime`) values ('renewal', new.id, (select NOW()));
    end if;
END$$

