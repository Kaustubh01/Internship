-- MySQL dump 10.13  Distrib 5.7.43, for Win64 (x86_64)
--
-- Host: localhost    Database: internship
-- ------------------------------------------------------
-- Server version	5.7.43-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `question_1` int(1) DEFAULT NULL,
  `question_2` int(1) DEFAULT NULL,
  `question_3` int(1) DEFAULT NULL,
  `question_4` int(1) DEFAULT NULL,
  `question_5` int(1) DEFAULT NULL,
  `question_6` int(1) DEFAULT NULL,
  `question_7` int(1) DEFAULT NULL,
  `question_8` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,5,5,5,5,5,5,5,5),(2,5,5,5,5,5,5,5,5);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `internship`
--

DROP TABLE IF EXISTS `internship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `internship` (
  `internship_id` int(11) NOT NULL AUTO_INCREMENT,
  `prn` bigint(20) DEFAULT NULL,
  `year` varchar(255) DEFAULT NULL,
  `organization` varchar(255) DEFAULT NULL,
  `duration` varchar(255) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `work_time` varchar(255) DEFAULT NULL,
  `days` varchar(255) DEFAULT NULL,
  `std_class` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `feedback` varchar(30) DEFAULT NULL,
  `report` varchar(30) DEFAULT NULL,
  `offer_letter` varchar(15) DEFAULT NULL,
  `certificate` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`internship_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internship`
--

LOCK TABLES `internship` WRITE;
/*!40000 ALTER TABLE `internship` DISABLE KEYS */;
INSERT INTO `internship` VALUES (1,2021016402129591,'2023-2024','Google','2','2023-10-03','2023-10-03','5 pm to 6 pm','Monday, Tuesday','FE','Approved','submitted','submitted',NULL,NULL),(2,2021016402127696,'2023-2024','Google','2','2023-10-03','2023-10-03','5 pm to 6 pm','Monday','FE','Approved','submitted','submitted',NULL,NULL);
/*!40000 ALTER TABLE `internship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `report` (
  `id` int(11) NOT NULL,
  `std_mobile` bigint(10) DEFAULT NULL,
  `std_email` varchar(30) DEFAULT NULL,
  `roll_as_intern` varchar(30) DEFAULT NULL,
  `emp_email` varchar(30) DEFAULT NULL,
  `supervisor_name` varchar(50) DEFAULT NULL,
  `supervisor_email` varchar(30) DEFAULT NULL,
  `supervisor_phone` bigint(10) DEFAULT NULL,
  `project_title` varchar(150) DEFAULT NULL,
  `project_desc` varchar(255) DEFAULT NULL,
  `resources` varchar(150) DEFAULT NULL,
  `learnings` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES (1,8657423246,'kaustubhmayekar02@gmail.com','Intern','skillhivedumy@gmail.com','harry','harrythegamer54@gmail.com',7878787878,'area','brief','flask','learning'),(2,8657423246,'kaustubhmayekar02@gmail.com','Intern','skillhivedumy@gmail.com','harry','harrythegamer54@gmail.com',7878787878,'area','work','flask','internship');
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `name` varchar(255) DEFAULT NULL,
  `prn` bigint(20) NOT NULL,
  `password` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`prn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('BIRWADKAR HARSH SANTOSH (SNEHAL)',2021016400314527,NULL),('KATKAR PRATHMESH NARAYAN (SHEETAL)',2021016400926373,NULL),('GUPTA NISHA SANTOSH (SARITA)',2021016401240117,NULL),('JEDHE SAMARTH VIJAY (ASHWINI)',2021016402117887,NULL),('KANSE HRITIK MANGESH (MANSI)',2021016402117895,NULL),('JAIN VIVEK DINESHKUMAR (RAJUDEVI)',2021016402117906,NULL),('AGIVALE YASHASHREE KALURAM (KALPANA)',2021016402117914,NULL),('SABQUAT JAREER (AZRA NAHEED)',2021016402117937,NULL),('CHAVAN MAHESH NILU (MANUBAI)',2021016402120963,NULL),('CHAVAN SANKET KRISHNATH (CHHAYA)',2021016402120971,NULL),('CHIKHALE ATHARVA SACHIN (VAISHALI)',2021016402125361,NULL),('RUTURAJ BHIVSANE (VIDYA)',2021016402125376,NULL),('DIVYANSH DOSHI (RUCHI)',2021016402127673,NULL),('BALSANIA MOHSINALI BAKARALI (HAMIDAB)',2021016402127681,NULL),('LANDE OMKAR RAMDAS (SANGITA)',2021016402127696,'password'),('ILKE ATHARVA SATAPPA (VAISHALI)',2021016402127707,NULL),('GOWDA RUCHITHA SWAMY (GEETHA)',2021016402129432,NULL),('BHAMRA AVNEET KAUR BALWINDER SINGH (JASWINDER KAUR)',2021016402129494,NULL),('HIMANSHU DINESH MAHAJAN (MADHUREE)',2021016402129583,NULL),('MAYEKAR KAUSTUBH SANJAY (SAPANA)',2021016402129591,'password'),('BARBHAYA SIDDH JATIN (KAMINI)',2021016402129617,NULL),('MALKAR PRANAV KRISHNA (PALLAVI)',2021016402129625,NULL),('JOSHI PIYUSH PRAKASH (PRANITA)',2021016402129633,NULL),('JADHAV DEVANSH SUNIL (NIRMALA)',2021016402129641,NULL),('SHAIKH RAHIL AHMED MUKHTAR AHMED (RASHIDA)',2021016402129761,NULL),('HARAD SANIKA HEMANT (SUVARNA)',2021016402130853,NULL),('HRITIK ATRE (SUJATA)',2021016402130884,NULL),('CHAVAN RUCHA PRABHAKAR (SNEHAL)',2021016402130892,NULL),('DESAI AAMIL SAJID (SABIHA)',2021016402130903,NULL),('KAMBLI RAUNAK NARAYAN (LAXMI)',2021016402130926,NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-03 20:08:59
