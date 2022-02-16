drop database if exists staff_details;

create database if not exists staff_details;

use staff_details;

CREATE TABLE IF NOT EXISTS `staff_login` (
`employee_id` int(5) NOT NULL,
`name` varchar(30) NOT NULL,
`password` varchar(30) NOT NULL,
`email` varchar(30) NOT NULL,
`phone` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into staff_login values (01353, "Zheng Jie", "password123", "zjong.2019@smu.edu.sg", 88138399);
insert into staff_login values (01354, "Jay Sian", "password234", "cheejs.2019@smu.edu.sg", 88138399);