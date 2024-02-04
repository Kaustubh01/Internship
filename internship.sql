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
  `internship_type` varchar(20) DEFAULT NULL,
  `mode` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`internship_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internship`
--

LOCK TABLES `internship` WRITE;
/*!40000 ALTER TABLE `internship` DISABLE KEYS */;
INSERT INTO `internship` VALUES (1,2021016402117872,'2023-2024','Google','3','2023-12-26','2023-12-26','01:01 - 11:01','Monday, Tuesday','FE','Approved',NULL,NULL,NULL,NULL,'Out-house','offline'),(2,2021016402120506,'2023-2024','Google','3','2023-12-26','2023-12-26','00:20 - 00:22','Monday','FE','pending',NULL,NULL,NULL,NULL,'in-house','online'),(3,2021016402120506,'2023-2024','Google','4','2023-12-26','2023-12-26','03:00 - 11:00','Monday','FE','pending',NULL,NULL,NULL,NULL,'Out-house','offline'),(4,2021016402117872,'2023-2024','Google','4','2023-12-26','2023-12-26','00:44 - 00:44','Wednesday','FE','pending',NULL,NULL,NULL,NULL,'Out-house','offline'),(5,2021016402120506,'2022-2023','Microsoft','3','2023-12-28','2023-12-28','21:51 - 21:51','Thursday, Friday','FE','Approved',NULL,NULL,NULL,NULL,'in-house','online');
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
  `gender` varchar(10) DEFAULT NULL,
  `email` varchar(35) DEFAULT NULL,
  `username` varchar(35) DEFAULT NULL,
  `password` varchar(35) DEFAULT NULL,
  `department` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`prn`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('BIRWADKAR HARSH SANTOSH (SNEHAL)',2021016400314527,NULL,NULL,NULL,NULL,NULL),('KATKAR PRATHMESH NARAYAN (SHEETAL)',2021016400926373,NULL,NULL,NULL,NULL,NULL),('GUPTA NISHA SANTOSH (SARITA)',2021016401240117,NULL,NULL,NULL,NULL,NULL),('PAWAR HARSHAL PRADEEP (APARNA)',2021016402117872,'male','kaustubhmayekar02@gmail.com','harry','password','Information Technology'),('JEDHE SAMARTH VIJAY (ASHWINI)',2021016402117887,NULL,NULL,NULL,NULL,NULL),('KANSE HRITIK MANGESH (MANSI)',2021016402117895,NULL,NULL,NULL,NULL,NULL),('JAIN VIVEK DINESHKUMAR (RAJUDEVI)',2021016402117906,NULL,NULL,NULL,NULL,NULL),('AGIVALE YASHASHREE KALURAM (KALPANA)',2021016402117914,NULL,NULL,NULL,NULL,NULL),('BHAWESH SUNIL YEOLE (MANGALA)',2021016402117922,NULL,NULL,NULL,NULL,NULL),('SABQUAT JAREER (AZRA NAHEED)',2021016402117937,NULL,NULL,NULL,NULL,NULL),('NAGRE SHARAYU SUBHASH (SUMAN)',2021016402120506,NULL,NULL,'shera','password','Information Technology'),('PANHALEKAR HRISHIKESH RAJESH (RASHMI)',2021016402120955,NULL,NULL,NULL,NULL,NULL),('CHAVAN MAHESH NILU (MANUBAI)',2021016402120963,NULL,NULL,NULL,NULL,NULL),('CHAVAN SANKET KRISHNATH (CHHAYA)',2021016402120971,NULL,NULL,NULL,NULL,NULL),('PUROHIT SAGAR BHARAT (SANTOSHDEVI)',2021016402120986,NULL,NULL,NULL,NULL,NULL),('TODSAM VANSHITA TUSHAR (PRAGATI)',2021016402120994,NULL,NULL,NULL,NULL,NULL),('SHINDE MANTHAN ABHIJIT SULBHA (SULBHA)',2021016402121003,NULL,NULL,NULL,NULL,NULL),('SAWANT RIYA PRAVIN (PRANJALI)',2021016402125345,NULL,NULL,NULL,NULL,NULL),('MOHILE ADITYA SANDEEP (SUNITA)',2021016402125353,NULL,NULL,NULL,NULL,NULL),('CHIKHALE ATHARVA SACHIN (VAISHALI)',2021016402125361,NULL,NULL,NULL,NULL,NULL),('RUTURAJ BHIVSANE (VIDYA)',2021016402125376,NULL,NULL,NULL,NULL,NULL),('PADME SANIKA SHIVA (SAVITA)',2021016402127642,NULL,NULL,NULL,NULL,NULL),('PRATHAMESH RAJARAM PUKALE (ARCHANA)',2021016402127657,NULL,NULL,NULL,NULL,NULL),('QURESHI MOHAMMED TAMIR MOHAMMED WARIS NASIM BANU (NASIM BANO)',2021016402127665,NULL,NULL,NULL,NULL,NULL),('DIVYANSH DOSHI (RUCHI)',2021016402127673,NULL,NULL,NULL,NULL,NULL),('BALSANIA MOHSINALI BAKARALI (HAMIDAB)',2021016402127681,NULL,NULL,NULL,NULL,NULL),('LANDE OMKAR RAMDAS (SANGITA)',2021016402127696,NULL,NULL,NULL,NULL,NULL),('ILKE ATHARVA SATAPPA (VAISHALI)',2021016402127707,NULL,NULL,NULL,NULL,NULL),('RAJHANS ANKITA KIRAN JAYASHREE (JAYASHREE RAJHANS)',2021016402127715,NULL,NULL,NULL,NULL,NULL),('PEDHAMBKAR ATHARVA MAHADEV (MANALI)',2021016402127723,NULL,NULL,NULL,NULL,NULL),('SAHU KIRAN SIMANCHAL (SUSHMA)',2021016402127731,NULL,NULL,NULL,NULL,NULL),('GOWDA RUCHITHA SWAMY (GEETHA)',2021016402129432,NULL,NULL,NULL,NULL,NULL),('TAYADE VEDANT NILESH (RANJANA)',2021016402129447,NULL,NULL,NULL,NULL,NULL),('SHINDE JAYESH DILIP (YOGITA)',2021016402129455,NULL,NULL,NULL,NULL,NULL),('RAUT YATISH SHEKHAR (BHARATI)',2021016402129463,NULL,NULL,NULL,NULL,NULL),('MESHRAM PIYUSH AJAY (MADHULIKA)',2021016402129471,NULL,NULL,NULL,NULL,NULL),('WASEKAR SAKSHI SHAMSUNDAR (KAVITA)',2021016402129486,NULL,NULL,NULL,NULL,NULL),('BHAMRA AVNEET KAUR BALWINDER SINGH (JASWINDER KAUR)',2021016402129494,NULL,NULL,NULL,NULL,NULL),('HIMANSHU DINESH MAHAJAN (MADHUREE)',2021016402129583,NULL,NULL,NULL,NULL,NULL),('MAYEKAR KAUSTUBH SANJAY (SAPANA)',2021016402129591,NULL,NULL,NULL,NULL,NULL),('RASTOGI OM VIJAY (LAXMI)',2021016402129602,NULL,NULL,NULL,NULL,NULL),('BARBHAYA SIDDH JATIN (KAMINI)',2021016402129617,NULL,NULL,NULL,NULL,NULL),('MALKAR PRANAV KRISHNA (PALLAVI)',2021016402129625,NULL,NULL,NULL,NULL,NULL),('JOSHI PIYUSH PRAKASH (PRANITA)',2021016402129633,NULL,NULL,NULL,NULL,NULL),('JADHAV DEVANSH SUNIL (NIRMALA)',2021016402129641,NULL,NULL,NULL,NULL,NULL),('MISHRA AMEET SUNIL (SANGEETA)',2021016402129656,NULL,NULL,NULL,NULL,NULL),('SHAIKH RAHIL AHMED MUKHTAR AHMED (RASHIDA)',2021016402129761,NULL,NULL,NULL,NULL,NULL),('SAKSHI SINGH (SEEMA)',2021016402129776,NULL,NULL,NULL,NULL,NULL),('SAWANT ANIRUDDHA VIJAY (RAMA)',2021016402129784,NULL,NULL,NULL,NULL,NULL),('RAWAT KARAN SINGH SURENDER SINGH KANTI (KANTI)',2021016402129792,NULL,NULL,NULL,NULL,NULL),('VISHWAKARMA HARSH RAMPRASAD (SEETA)',2021016402129803,NULL,NULL,NULL,NULL,NULL),('NAIK VIVEK HANUMANTA (REKHA)',2021016402129811,NULL,NULL,NULL,NULL,NULL),('MHATRE PREET SANTOSH (NAMITA)',2021016402129826,NULL,NULL,NULL,NULL,NULL),('SINGH SOMESH SHRINIVAS (MAHARANI)',2021016402129834,NULL,NULL,NULL,NULL,NULL),('SHETTY SWASTIK VIDYADHAR (BABY)',2021016402129962,NULL,NULL,NULL,NULL,NULL),('NIKAM APOORVA RAJENDRA (SWAPNALI)',2021016402129977,NULL,NULL,NULL,NULL,NULL),('VAGDODA JILL ASHOK (SUNITA)',2021016402129985,NULL,NULL,NULL,NULL,NULL),('SAWANT TEJAS SUBHASH (SAMIKSHA)',2021016402129993,NULL,NULL,NULL,NULL,NULL),('YADAV CHHAGANRAM JAYKESH (BACHHI)',2021016402130002,NULL,NULL,NULL,NULL,NULL),('PAL PRADEEP KEDAR (SUNITA)',2021016402130017,NULL,NULL,NULL,NULL,NULL),('SHAH PALASH GIRISHKUMAR (ANJALI)',2021016402130025,NULL,NULL,NULL,NULL,NULL),('YADAV SANJANA SANJEEV KUMAR (ASHA)',2021016402130033,NULL,NULL,NULL,NULL,NULL),('HARAD SANIKA HEMANT (SUVARNA)',2021016402130853,NULL,NULL,NULL,NULL,NULL),('PADAVE SRUSHTI RAVJI (SUMAN)',2021016402130861,NULL,NULL,NULL,NULL,NULL),('WAYAL SIDDHESH PRAVIN (SHEETAL)',2021016402130876,NULL,NULL,NULL,NULL,NULL),('HRITIK ATRE (SUJATA)',2021016402130884,NULL,NULL,NULL,NULL,NULL),('CHAVAN RUCHA PRABHAKAR (SNEHAL)',2021016402130892,NULL,NULL,NULL,NULL,NULL),('DESAI AAMIL SAJID (SABIHA)',2021016402130903,NULL,NULL,NULL,NULL,NULL),('MUKHARI MONISH AJAY (JAYASHREE)',2021016402130911,NULL,NULL,NULL,NULL,NULL),('KAMBLI RAUNAK NARAYAN (LAXMI)',2021016402130926,NULL,NULL,NULL,NULL,NULL);
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

-- Dump completed on 2024-02-03 17:12:23
