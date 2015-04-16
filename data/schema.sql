DROP DATABASE IF EXISTS test_app;
CREATE DATABASE test_app;

USE test_app;


CREATE TABLE `users` (
    `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `email` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `date_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `date_updated` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
