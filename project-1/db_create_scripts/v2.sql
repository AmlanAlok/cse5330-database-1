-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema us_covid_19_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema us_covid_19_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `us_covid_19_db` DEFAULT CHARACTER SET utf8 ;
USE `us_covid_19_db` ;

-- -----------------------------------------------------
-- Table `us_covid_19_db`.`state`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `us_covid_19_db`.`state` (
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
  PRIMARY KEY (`state`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `us_covid_19_db`.`county`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `us_covid_19_db`.`county` (
  `state` VARCHAR(50) NOT NULL,
  `county` VARCHAR(45) NOT NULL,
  `population` INT NULL,
  `latitude` DECIMAL(10,8) NULL,
  `longitude` DECIMAL(11,8) NULL,
  PRIMARY KEY (`county`,`state`),
  INDEX `county_state_fk_idx` (`state` ASC),
  CONSTRAINT `county_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `us_covid_19_db`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `us_covid_19_db`.`confirmed_cases`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `us_covid_19_db`.`confirmed_cases` (
  `state` VARCHAR(50) NOT NULL,
  `county` VARCHAR(50) NOT NULL,
  `test_date` DATE NULL,
  `positive_count` INT NULL,
  PRIMARY KEY (`state`, `county`),
  INDEX `confirmed_cases_county_fk_idx` (`county` ASC),
  CONSTRAINT `confirmed_cases_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `us_covid_19_db`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `confirmed_cases_county_fk`
    FOREIGN KEY (`county`)
    REFERENCES `us_covid_19_db`.`county` (`county`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `us_covid_19_db`.`deaths`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `us_covid_19_db`.`deaths` (
  `state` VARCHAR(50) NOT NULL,
  `county` VARCHAR(50) NOT NULL,
  `report_date` DATE NULL,
  `death_count` INT NULL,
  PRIMARY KEY (`state`, `county`),
  INDEX `deaths_county_fk_idx` (`county` ASC),
  CONSTRAINT `deaths_state_fk`
    FOREIGN KEY (`state`)
    REFERENCES `us_covid_19_db`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `deaths_county_fk`
    FOREIGN KEY (`county`)
    REFERENCES `us_covid_19_db`.`county` (`county`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `us_covid_19_db`.`vaccinations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `us_covid_19_db`.`vaccinations` (
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
    REFERENCES `us_covid_19_db`.`state` (`state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
