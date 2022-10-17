
USE `axa5861` ;

CREATE TABLE IF NOT EXISTS `axa5861`.`state` (
  `state_id` INT NULL,
  `state` VARCHAR(50) NOT NULL,
  `abbreviation` CHAR(2) NULL,
  `year_of_statehood` INT NULL,
  `capital` VARCHAR(50) NULL,
  `capital_since` INT NULL,
  `land_area` DECIMAL NULL,
  `is_populous_city` TINYINT NULL,
  `municipal_population` INT NULL,
  `metro_population` INT NULL,
  PRIMARY KEY (`state`));

CREATE TABLE IF NOT EXISTS `axa5861`.`county` (
  `state` VARCHAR(50) NOT NULL,
  `county` VARCHAR(45) NOT NULL,
  `population` INT NULL,
  `latitude` DECIMAL(10,8) NULL,
  `longitude` DECIMAL(11,8) NULL,
  PRIMARY KEY (`county`,`state`),
  INDEX `county_state_fk_idx` (`state` ASC),
  CONSTRAINT `county_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `axa5861`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `axa5861`.`confirmed_cases` (
  `state` VARCHAR(50) NOT NULL,
  `county` VARCHAR(50) NOT NULL,
  `test_date` DATE NOT NULL,
  `positive_count` INT NULL,
  PRIMARY KEY (`state`, `county`, `test_date`),
  INDEX `confirmed_cases_county_fk_idx` (`county` ASC),
  CONSTRAINT `confirmed_cases_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `axa5861`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `confirmed_cases_county_fk`
    FOREIGN KEY (`county`)
    REFERENCES `axa5861`.`county` (`county`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `axa5861`.`deaths` (
  `state` VARCHAR(50) NOT NULL,
  `county` VARCHAR(50) NOT NULL,
  `report_date` DATE NOT NULL,
  `death_count` INT NULL,
  PRIMARY KEY (`state`, `county`, `report_date`),
  INDEX `deaths_county_fk_idx` (`county` ASC),
  CONSTRAINT `deaths_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `axa5861`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `deaths_county_fk`
    FOREIGN KEY (`county`)
    REFERENCES `axa5861`.`county` (`county`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `axa5861`.`vaccinations` (
  `state` VARCHAR(50) NOT NULL,
  `total_distributed` INT NULL,
  `total_administered` INT NULL,
  `distributed_per_100k` INT NULL,
  `administered_per_100k` INT NULL,
  `people_with_one_plus_doses` INT NULL,
  `people_with_one_plus_doses_per_100k` INT NULL,
  `people_with_two_plus_doses` INT NULL,
  `people_with_two_plus_doses_per_100k` INT NULL,
  PRIMARY KEY (`state`),
  CONSTRAINT `vaccinations_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `axa5861`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
