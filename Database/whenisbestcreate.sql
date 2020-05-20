-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema whenisbest
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema whenisbest
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `whenisbest` DEFAULT CHARACTER SET utf8 ;
USE `whenisbest` ;

-- -----------------------------------------------------
-- Table `whenisbest`.`Users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `whenisbest`.`Users` ;

CREATE TABLE IF NOT EXISTS `whenisbest`.`Users` (
  `userID` VARCHAR(320) NOT NULL,
  `FName` VARCHAR(60) NULL,
  `LName` VARCHAR(60) NULL,
  `Pass` CHAR(128) NULL,
  PRIMARY KEY (`userID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whenisbest`.`Event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `whenisbest`.`Event` ;

CREATE TABLE IF NOT EXISTS `whenisbest`.`Event` (
  `eventID` CHAR(32) NOT NULL,
  `eventName` VARCHAR(50) NOT NULL,
  `eventDuration` INT NULL,
  `eventRecurs` TINYINT NOT NULL DEFAULT 0,
  `eventShared` TINYINT NOT NULL,
  `eventCreator` VARCHAR(320) NULL,
  `eventFrequency` INT NULL DEFAULT 0,
  PRIMARY KEY (`eventID`),
  UNIQUE INDEX `EventID_UNIQUE` (`eventID` ASC),
  INDEX `creator_idx` (`eventCreator` ASC),
  CONSTRAINT `creator`
    FOREIGN KEY (`eventCreator`)
    REFERENCES `whenisbest`.`Users` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whenisbest`.`UserEvent`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `whenisbest`.`UserEvent` ;

CREATE TABLE IF NOT EXISTS `whenisbest`.`UserEvent` (
  `userID` VARCHAR(320) NOT NULL,
  `eventID` CHAR(32) NOT NULL,
  PRIMARY KEY (`userID`, `eventID`),
  INDEX `eventLinkage_idx` (`eventID` ASC),
  CONSTRAINT `userLinkage`
    FOREIGN KEY (`userID`)
    REFERENCES `whenisbest`.`Users` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `eventLinkage`
    FOREIGN KEY (`eventID`)
    REFERENCES `whenisbest`.`Event` (`eventID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whenisbest`.`Responses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `whenisbest`.`Responses` ;

CREATE TABLE IF NOT EXISTS `whenisbest`.`Responses` (
  `eventID` CHAR(32) NOT NULL,
  `userEmail` VARCHAR(320) NOT NULL,
  `userName` VARCHAR(60) NULL,
  `timeSlot` DATETIME NOT NULL,
  `comments` VARCHAR(500) NULL,
  PRIMARY KEY (`eventID`, `userEmail`, `timeSlot`),
  CONSTRAINT `eventID`
    FOREIGN KEY (`eventID`)
    REFERENCES `whenisbest`.`Event` (`eventID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whenisbest`.`Recurring`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `whenisbest`.`Recurring` ;

CREATE TABLE IF NOT EXISTS `whenisbest`.`Recurring` (
  `eventID` CHAR(32) NOT NULL,
  `day` INT NOT NULL,
  `timeSlot` TIME NOT NULL,
  PRIMARY KEY (`eventID`),
  CONSTRAINT `recurringEventID`
    FOREIGN KEY (`eventID`)
    REFERENCES `whenisbest`.`Event` (`eventID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whenisbest`.`OneTime`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `whenisbest`.`OneTime` ;

CREATE TABLE IF NOT EXISTS `whenisbest`.`OneTime` (
  `eventID` CHAR(32) NOT NULL,
  `date` DATE NOT NULL,
  `timeSlot` TIME NOT NULL,
  PRIMARY KEY (`eventID`),
  CONSTRAINT `singleEventID`
    FOREIGN KEY (`eventID`)
    REFERENCES `whenisbest`.`Event` (`eventID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
