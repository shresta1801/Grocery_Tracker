-- Grocery Expiry Tracker — MySQL schema (matches Flask-SQLAlchemy models in app.py)
-- Charset: utf8mb4 for full Unicode support

CREATE DATABASE IF NOT EXISTS grocery_tracker
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE grocery_tracker;

CREATE TABLE IF NOT EXISTS `user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(80) NOT NULL,
  `email` VARCHAR(120) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `dark_mode` TINYINT(1) DEFAULT 0,
  `notification_days` INT DEFAULT 3,
  `notification_method` VARCHAR(20) DEFAULT 'email',
  `remember_me` TINYINT(1) DEFAULT 1,
  `notification_frequency` VARCHAR(20) DEFAULT 'daily',
  `custom_notification_times` VARCHAR(200) DEFAULT '',
  `ai_notifications` TINYINT(1) DEFAULT 1,
  `browser_notifications` TINYINT(1) DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_user_username` (`username`),
  UNIQUE KEY `uq_user_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `grocery_item` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `category` VARCHAR(50) DEFAULT 'Other',
  `quantity` VARCHAR(50) NOT NULL,
  `expiry_date` DATE NOT NULL,
  `added_date` DATE DEFAULT (CURRENT_DATE),
  `status` VARCHAR(20) DEFAULT 'active',
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_grocery_item_user_id` (`user_id`),
  CONSTRAINT `fk_grocery_item_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
