
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";




CREATE TABLE `tbl_user` (
  `user_id` int(11) NOT NULL,
  `user_firstname` varchar(15) NOT NULL,
  `user_lastname` varchar(15) NOT NULL,
  `user_address` varchar(100) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `user_password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`user_id`);


ALTER TABLE `tbl_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

