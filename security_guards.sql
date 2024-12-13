-- -----------------------------------------------------
-- Schema security_guards
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `security_guards` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `security_guards` ;

-- Table: clients
CREATE TABLE IF NOT EXISTS `clients` (
  `client_id` INT NOT NULL,
  `client_details` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE = InnoDB;

-- Table: employee_category
CREATE TABLE IF NOT EXISTS `employee_category` (
  `category_code` VARCHAR(10) NOT NULL,
  `category_description` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`category_code`)
) ENGINE = InnoDB;

-- Table: employees
CREATE TABLE IF NOT EXISTS `employees` (
  `employee_id` INT NOT NULL,
  `category_code` VARCHAR(10) DEFAULT NULL,
  `employee_details` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  INDEX `category_code` (`category_code`),
  CONSTRAINT `fk_employee_category`
    FOREIGN KEY (`category_code`)
    REFERENCES `employee_category` (`category_code`)
    ON DELETE SET NULL
) ENGINE = InnoDB;

-- Table: employee_assignments
CREATE TABLE IF NOT EXISTS `employee_assignments` (
  `employee_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE DEFAULT NULL,
  PRIMARY KEY (`employee_id`, `client_id`, `start_date`),
  CONSTRAINT `fk_assignment_employee`
    FOREIGN KEY (`employee_id`)
    REFERENCES `employees` (`employee_id`),
  CONSTRAINT `fk_assignment_client`
    FOREIGN KEY (`client_id`)
    REFERENCES `clients` (`client_id`)
) ENGINE = InnoDB;

-- Table: training_courses
CREATE TABLE IF NOT EXISTS `training_courses` (
  `course_id` INT NOT NULL,
  `course_details` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE = InnoDB;

-- Table: employee_training
CREATE TABLE IF NOT EXISTS `employee_training` (
  `employee_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE DEFAULT NULL,
  PRIMARY KEY (`employee_id`, `course_id`, `start_date`),
  CONSTRAINT `fk_training_employee`
    FOREIGN KEY (`employee_id`)
    REFERENCES `employees` (`employee_id`),
  CONSTRAINT `fk_training_course`
    FOREIGN KEY (`course_id`)
    REFERENCES `training_courses` (`course_id`)
) ENGINE = InnoDB;

-- Table: qualifications
CREATE TABLE IF NOT EXISTS `qualifications` (
  `qualification_id` INT NOT NULL,
  `qualification_details` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`qualification_id`)
) ENGINE = InnoDB;

-- Table: employees_qualifications
CREATE TABLE IF NOT EXISTS `employees_qualifications` (
  `employee_id` INT NOT NULL,
  `qualification_id` INT NOT NULL,
  `date_qualified` DATE DEFAULT NULL,
  `qualification_level` VARCHAR(50) DEFAULT NULL,
  `other_details` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`employee_id`, `qualification_id`),
  CONSTRAINT `fk_qualification_employee`
    FOREIGN KEY (`employee_id`)
    REFERENCES `employees` (`employee_id`),
  CONSTRAINT `fk_qualification_details`
    FOREIGN KEY (`qualification_id`)
    REFERENCES `qualifications` (`qualification_id`)
) ENGINE = InnoDB;

