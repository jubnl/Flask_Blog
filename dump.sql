-- MariaDB dump 10.17  Distrib 10.4.14-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: flask_blog
-- ------------------------------------------------------
-- Server version	10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `flask_blog`
--

/*!40000 DROP DATABASE IF EXISTS `flask_blog`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `flask_blog` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `flask_blog`;

--
-- Table structure for table `t_countries`
--

DROP TABLE IF EXISTS `t_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_countries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=232 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_countries`
--

LOCK TABLES `t_countries` WRITE;
/*!40000 ALTER TABLE `t_countries` DISABLE KEYS */;
INSERT INTO `t_countries` (`id`, `name`) VALUES (1,'Afghanistan'),(2,'Åland Islands'),(3,'Albania'),(4,'Algeria'),(5,'American Samoa'),(6,'Andorra'),(7,'Angola'),(8,'Anguilla'),(9,'Antarctica'),(10,'Antigua and Barbuda'),(11,'Argentina'),(12,'Armenia'),(13,'Aruba'),(14,'Australia'),(15,'Austria'),(16,'Azerbaijan'),(17,'Bahamas'),(18,'Bahrain'),(19,'Bangladesh'),(20,'Barbados'),(21,'Belarus'),(22,'Belgium'),(23,'Belize'),(24,'Benin'),(25,'Bermuda'),(26,'Bhutan'),(27,'Bosnia and Herzegovina'),(28,'Botswana'),(29,'Bouvet Island'),(30,'Brazil'),(31,'British Indian Ocean Territory'),(32,'Brunei Darussalam'),(33,'Bulgaria'),(34,'Burkina Faso'),(35,'Burundi'),(36,'Cambodia'),(37,'Cameroon'),(38,'Canada'),(39,'Cape Verde'),(40,'Cayman Islands'),(41,'Central African Republic'),(42,'Chad'),(43,'Chile'),(44,'China'),(45,'Christmas Island'),(46,'Cocos (Keeling) Islands'),(47,'Colombia'),(48,'Comoros'),(49,'Congo'),(50,'Cook Islands'),(51,'Costa Rica'),(52,'Croatia'),(53,'Cuba'),(54,'CuraÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ao'),(55,'Cyprus'),(56,'Czech Republic'),(57,'Denmark'),(58,'Djibouti'),(59,'Dominica'),(60,'Dominican Republic'),(61,'Ecuador'),(62,'Egypt'),(63,'El Salvador'),(64,'Equatorial Guinea'),(65,'Eritrea'),(66,'Estonia'),(67,'Ethiopia'),(68,'Falkland Islands (Malvinas)'),(69,'Faroe Islands'),(70,'Fiji'),(71,'Finland'),(72,'France'),(73,'French Guiana'),(74,'French Polynesia'),(75,'French Southern Territories'),(76,'Gabon'),(77,'Gambia'),(78,'Georgia'),(79,'Germany'),(80,'Ghana'),(81,'Gibraltar'),(82,'Greece'),(83,'Greenland'),(84,'Grenada'),(85,'Guadeloupe'),(86,'Guam'),(87,'Guatemala'),(88,'Guernsey'),(89,'Guinea'),(90,'Guinea-Bissau'),(91,'Guyana'),(92,'Haiti'),(93,'Heard Island and McDonald Islands'),(94,'Holy See (Vatican City State)'),(95,'Honduras'),(96,'Hong Kong'),(97,'Hungary'),(98,'Iceland'),(99,'India'),(100,'Indonesia'),(101,'Iraq'),(102,'Ireland'),(103,'Isle of Man'),(104,'Israel'),(105,'Italy'),(106,'Jamaica'),(107,'Japan'),(108,'Jersey'),(109,'Jordan'),(110,'Kazakhstan'),(111,'Kenya'),(112,'Kiribati'),(113,'Kuwait'),(114,'Kyrgyzstan'),(115,'Latvia'),(116,'Lebanon'),(117,'Lesotho'),(118,'Liberia'),(119,'Libya'),(120,'Liechtenstein'),(121,'Lithuania'),(122,'Luxembourg'),(123,'Macao'),(124,'Madagascar'),(125,'Malawi'),(126,'Malaysia'),(127,'Maldives'),(128,'Mali'),(129,'Malta'),(130,'Marshall Islands'),(131,'Martinique'),(132,'Mauritania'),(133,'Mauritius'),(134,'Mayotte'),(135,'Mexico'),(136,'Monaco'),(137,'Mongolia'),(138,'Montenegro'),(139,'Montserrat'),(140,'Morocco'),(141,'Mozambique'),(142,'Myanmar'),(143,'Namibia'),(144,'Nauru'),(145,'Nepal'),(146,'Netherlands'),(147,'New Caledonia'),(148,'New Zealand'),(149,'Nicaragua'),(150,'Niger'),(151,'Nigeria'),(152,'Niue'),(153,'Norfolk Island'),(154,'Northern Mariana Islands'),(155,'Norway'),(156,'Oman'),(157,'Pakistan'),(158,'Palau'),(159,'Panama'),(160,'Papua New Guinea'),(161,'Paraguay'),(162,'Peru'),(163,'Philippines'),(164,'Pitcairn'),(165,'Poland'),(166,'Portugal'),(167,'Puerto Rico'),(168,'Qatar'),(169,'RÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©union'),(170,'Romania'),(171,'Russian Federation'),(172,'Rwanda'),(173,'Saint BarthÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©lemy'),(174,'Saint Kitts and Nevis'),(175,'Saint Lucia'),(176,'Saint Martin (French part)'),(177,'Saint Pierre and Miquelon'),(178,'Saint Vincent and the Grenadines'),(179,'Samoa'),(180,'San Marino'),(181,'Sao Tome and Principe'),(182,'Saudi Arabia'),(183,'Senegal'),(184,'Serbia'),(185,'Seychelles'),(186,'Sierra Leone'),(187,'Singapore'),(188,'Sint Maarten (Dutch part)'),(189,'Slovakia'),(190,'Slovenia'),(191,'Solomon Islands'),(192,'Somalia'),(193,'South Africa'),(194,'South Georgia and the South Sandwich Islands'),(195,'South Sudan'),(196,'Spain'),(197,'Sri Lanka'),(198,'Sudan'),(199,'Suriname'),(200,'Svalbard and Jan Mayen'),(201,'Swaziland'),(202,'Sweden'),(203,'Switzerland'),(204,'Syrian Arab Republic'),(205,'Tajikistan'),(206,'Thailand'),(207,'Timor-Leste'),(208,'Togo'),(209,'Tokelau'),(210,'Tonga'),(211,'Trinidad and Tobago'),(212,'Tunisia'),(213,'Turkey'),(214,'Turkmenistan'),(215,'Turks and Caicos Islands'),(216,'Tuvalu'),(217,'Uganda'),(218,'Ukraine'),(219,'United Arab Emirates'),(220,'United Kingdom'),(221,'United States'),(222,'United States Minor Outlying Islands'),(223,'Uruguay'),(224,'Uzbekistan'),(225,'Vanuatu'),(226,'Viet Nam'),(227,'Wallis and Futuna'),(228,'Western Sahara'),(229,'Yemen'),(230,'Zambia'),(231,'Zimbabwe');
/*!40000 ALTER TABLE `t_countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_genders`
--

DROP TABLE IF EXISTS `t_genders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_genders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_genders`
--

LOCK TABLES `t_genders` WRITE;
/*!40000 ALTER TABLE `t_genders` DISABLE KEYS */;
INSERT INTO `t_genders` (`id`, `gender`) VALUES (1,'Homme'),(2,'Femme'),(3,'Hélicopter'),(5,'Bouteille'),(6,'Manche à couille');
/*!40000 ALTER TABLE `t_genders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_log_types`
--

DROP TABLE IF EXISTS `t_log_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_log_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `log_type` varchar(50) NOT NULL,
  `designation` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_log_types`
--

LOCK TABLES `t_log_types` WRITE;
/*!40000 ALTER TABLE `t_log_types` DISABLE KEYS */;
INSERT INTO `t_log_types` (`id`, `log_type`, `designation`) VALUES (1,'add_country','Add a country'),(2,'delete_country','Delete a country'),(3,'update_coutry','Update a country'),(4,'add_gender','Add a gender'),(5,'delete_gender','Delete a gender'),(6,'update_gender','Update a gender'),(7,'add_permission','Add a permission'),(8,'delete_permission','Delete a permission'),(9,'update_permission','Update a permission'),(10,'add_user','Add a user'),(11,'delete_user','Delete a user'),(12,'update_user_permission','Update a user\'s permission'),(13,'update_user_fname','Update a user\'s first name'),(14,'update_user_lname','Update a user\'s last name'),(15,'update_user_email','Update a user\'s email'),(16,'update_user_gender','Update a user\'s gender'),(17,'update_user_country','Update a user\'s country'),(18,'update_user_username','Update a user\'s username'),(19,'update_user_password','Update a user\'s password'),(20,'update_user_reset_password_permission','Update a user\'s reset permission'),(21,'update_user_reset_password_random','Update a user\'s key to reset his password'),(22,'update_user_files','Update a user\'s profile picture'),(23,'add_post','Add a post'),(24,'delete_post','Delete a post'),(25,'update_post','Update a post');
/*!40000 ALTER TABLE `t_log_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_logs`
--

DROP TABLE IF EXISTS `t_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `log_type_id` int(11) NOT NULL,
  `sql_executed` text NOT NULL,
  `value_before` varchar(255) DEFAULT NULL,
  `value_after` varchar(255) DEFAULT NULL,
  `success` tinyint(1) NOT NULL,
  `error_message` varchar(255) DEFAULT NULL,
  `deleted_data` text DEFAULT NULL,
  `log_date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `log_type_id` (`log_type_id`),
  CONSTRAINT `fk_log_type_id` FOREIGN KEY (`log_type_id`) REFERENCES `t_log_types` (`id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_logs`
--

LOCK TABLES `t_logs` WRITE;
/*!40000 ALTER TABLE `t_logs` DISABLE KEYS */;
INSERT INTO `t_logs` (`id`, `user_id`, `log_type_id`, `sql_executed`, `value_before`, `value_after`, `success`, `error_message`, `deleted_data`, `log_date`) VALUES (1,NULL,14,'INSERT INTO t_users (`permission`, `first_name`, `last_name`, `email`, `country`, `username`, `password`, `reset_password_permission`, `files`, `gender`, `reset_password_random`) VALUES (1, \'asdf\', \'asdf\', \'a@a.com\', 1, \'Jack\', \'$5$rounds=535000$kkQXTD5OouRxuyvH$AYMK5mB9SlD8TVTMgjrx7FC5zrjVu85cMZBKH7f3S78\', \'no_reset\', \'admin.png\', 1, \'Default_value\')',NULL,NULL,0,'(1062, Duplicate entry \'Jack\' for key \'username unique\')',NULL,'2021-02-11 17:09:25'),(2,NULL,14,'INSERT INTO t_users (`permission`, `first_name`, `last_name`, `email`, `country`, `username`, `password`, `reset_password_permission`, `files`, `gender`, `reset_password_random`) VALUES (1, \'ad\', \'sadd\', \'a@a.com\', 1, \'Jack\', \'$5$rounds=535000$H3DfQPnQfe6KovyR$ym/OeOim11dbzh0yeyrPl1/rELsHSivA9LSHwq4bVm2\', \'no_reset\', \'admin.png\', 1, \'Default_value\')',NULL,NULL,0,'(1062, \"Duplicate entry \'Jack\' for key \'username unique\'\")',NULL,'2021-02-11 17:34:26');
/*!40000 ALTER TABLE `t_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_permissions`
--

DROP TABLE IF EXISTS `t_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_permissions`
--

LOCK TABLES `t_permissions` WRITE;
/*!40000 ALTER TABLE `t_permissions` DISABLE KEYS */;
INSERT INTO `t_permissions` (`id`, `permission`) VALUES (1,'user'),(2,'modo'),(3,'admin');
/*!40000 ALTER TABLE `t_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_posts`
--

DROP TABLE IF EXISTS `t_posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `content` text NOT NULL,
  `date_posted` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author` (`author`),
  CONSTRAINT `fk_post_author` FOREIGN KEY (`author`) REFERENCES `t_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_posts`
--

LOCK TABLES `t_posts` WRITE;
/*!40000 ALTER TABLE `t_posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_users`
--

DROP TABLE IF EXISTS `t_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission` int(11) NOT NULL COMMENT 'les permissions de l''utilisateur',
  `first_name` varchar(100) NOT NULL COMMENT 'le Prenom',
  `last_name` varchar(100) NOT NULL COMMENT 'Le nom',
  `email` varchar(100) NOT NULL COMMENT 'l''email du client',
  `gender` int(11) NOT NULL COMMENT 'fk du sexe du client',
  `country` int(11) NOT NULL COMMENT 'fk du pays ou vie le client',
  `username` varchar(100) NOT NULL COMMENT 'le pseudo du client',
  `password` varchar(100) NOT NULL COMMENT 'le mot de passe du client',
  `reset_password_permission` varchar(12) NOT NULL,
  `reset_password_random` varchar(255) NOT NULL,
  `files` text NOT NULL COMMENT 'photo du client',
  `register_date` timestamp NULL DEFAULT current_timestamp() COMMENT 'la date de creation du client',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email unique` (`email`),
  UNIQUE KEY `username unique` (`username`),
  KEY `fk_permission` (`permission`),
  KEY `fk_country` (`country`),
  KEY `fk_gender` (`gender`) USING BTREE,
  CONSTRAINT `fk_country` FOREIGN KEY (`country`) REFERENCES `t_countries` (`id`),
  CONSTRAINT `fk_gender` FOREIGN KEY (`gender`) REFERENCES `t_genders` (`id`),
  CONSTRAINT `fk_permissions` FOREIGN KEY (`permission`) REFERENCES `t_permissions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='utilisateurs';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_users`
--

LOCK TABLES `t_users` WRITE;
/*!40000 ALTER TABLE `t_users` DISABLE KEYS */;
INSERT INTO `t_users` (`id`, `permission`, `first_name`, `last_name`, `email`, `gender`, `country`, `username`, `password`, `reset_password_permission`, `reset_password_random`, `files`, `register_date`) VALUES (1,3,'Jack','OWheel','exemple@exemple.com',3,98,'Jack','$5$rounds=535000$MQt8BJ0dVoLMHmGU$QmEmV5ywx.bAXHvwSv6j/3XgK7nPSLhLiAbx7JhThq4','no_reset','Default_value','admin.png','2021-02-11 09:41:59');
/*!40000 ALTER TABLE `t_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-08 11:37:00
