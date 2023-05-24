CREATE DATABASE  IF NOT EXISTS `nba` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nba`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: nba
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `game_ID` int NOT NULL,
  `gameDATE` date DEFAULT NULL,
  `homeTeam` varchar(30) DEFAULT NULL,
  `visitorTeam` varchar(30) DEFAULT NULL,
  `victory` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`game_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'2022-12-04','Spurs','Suns',0),(2,'2022-11-30','Trail Blazers','Lakers',1),(3,'2022-12-15','Jazz','Pelicans',1),(4,'2022-11-22','Grizzlies','Kings',0),(5,'2022-11-23','Warriors','Clippers',1),(6,'2022-12-12','Mavericks','Thunder',1),(7,'2022-11-05','Timberwolves','Rockets',1),(8,'2022-10-26','Nuggest','Lakers',1),(9,'2022-11-28','Kings','Suns',0);
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games_details`
--

DROP TABLE IF EXISTS `games_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games_details` (
  `detail_ID` int NOT NULL,
  `game_ID` int NOT NULL,
  `team_ID` int NOT NULL,
  `playerID` int NOT NULL,
  `minPlayed` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `rebounds` int DEFAULT NULL,
  `assists` int DEFAULT NULL,
  `fieldGoal` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`detail_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games_details`
--

LOCK TABLES `games_details` WRITE;
/*!40000 ALTER TABLE `games_details` DISABLE KEYS */;
INSERT INTO `games_details` VALUES (1,1,1,1,28,20,0,8,0.44),(2,1,1,3,25,25,10,3,0.71),(3,1,1,4,6,2,2,0,0.50),(4,1,1,5,26,20,4,3,0.63),(5,1,1,9,14,12,4,0,0.60),(6,1,1,10,24,5,5,2,0.40),(7,1,1,11,26,9,11,6,0.50),(8,1,1,12,25,5,2,6,0.25),(9,1,1,13,21,17,3,2,0.75),(10,1,1,14,14,10,1,3,0.38),(11,1,1,15,28,8,1,4,1.00),(12,1,1,16,3,0,2,1,0.00),(13,1,2,21,17,4,6,5,0.14),(14,1,2,19,31,12,3,0,0.83),(15,1,2,24,33,27,5,2,0.48),(16,1,2,25,29,10,2,3,0.45),(17,1,2,31,31,14,5,4,0.42),(18,1,2,30,18,2,3,1,0.16),(19,1,2,23,15,5,4,0,0.40),(20,1,2,22,13,5,4,1,0.40),(21,1,2,18,20,5,7,1,1.00),(22,1,2,26,8,3,0,0,1.00),(23,1,2,20,25,8,1,2,0.30),(24,2,12,38,29,27,12,1,0.53),(25,2,12,49,33,31,7,8,0.60),(26,2,12,34,22,5,4,0,0.29),(27,2,12,44,35,22,5,3,0.70),(28,2,12,39,11,6,4,0,1.00),(29,2,12,47,2,0,1,1,0.00),(30,2,12,41,2,0,1,0,0.00),(31,2,12,36,20,14,6,3,0.60),(32,2,12,49,23,10,5,4,0.29),(33,2,12,42,14,4,1,2,0.30),(34,2,12,37,19,3,1,1,0.16),(35,2,8,65,36,21,5,4,0.41),(36,2,8,64,31,10,10,1,0.60),(37,2,8,54,35,27,4,5,0.43),(38,2,8,59,32,8,4,5,0.25),(39,2,8,62,39,22,4,8,0.41),(40,2,8,53,14,3,3,2,0.00),(41,2,8,51,8,0,1,0,0.00),(42,2,8,63,14,2,5,0,0.25),(43,2,8,52,2,0,0,0,0.00),(44,2,8,61,28,16,3,0,0.58),(45,3,9,79,35,14,7,3,0.27),(46,3,9,78,42,31,5,3,0.53),(47,3,9,82,21,3,6,3,0.00),(48,3,9,72,32,4,2,6,0.13),(49,3,9,71,39,39,8,2,0.58),(50,3,9,74,18,2,3,2,0.30),(51,3,9,68,3,4,1,0,1.00),(52,3,9,77,28,11,8,1,1.00),(53,3,9,69,26,17,3,1,0.40),(54,3,9,67,21,7,1,3,0.50),(55,3,3,99,42,31,8,8,0.50),(56,3,3,89,21,12,4,4,0.50),(57,3,3,98,26,6,9,1,0.50),(58,3,3,93,42,28,6,4,0.48),(59,3,3,94,33,12,5,0,0.50),(60,3,3,95,29,13,9,1,0.60),(61,3,3,92,33,13,2,2,0.36),(62,3,3,85,20,8,3,3,0.40),(63,3,3,84,19,6,3,1,0.40),(64,4,5,116,37,9,13,8,0.38),(65,4,5,100,33,26,4,0,0.54),(66,4,5,113,24,2,3,2,0.13),(67,4,5,104,35,32,8,6,0.52),(68,4,5,106,33,18,6,1,0.60),(69,4,5,108,15,0,3,0,0.00),(70,4,5,109,11,10,3,0,0.71),(71,4,5,110,19,2,2,4,0.20),(72,4,5,101,9,0,1,2,0.00),(73,4,5,112,23,14,2,4,0.38),(74,4,4,124,27,22,3,1,0.57),(75,4,4,120,32,14,5,5,0.38),(76,4,4,117,30,5,16,0,0.40),(77,4,4,129,34,34,7,6,0.57),(78,4,4,126,31,10,9,2,0.38),(79,4,4,122,18,6,2,2,0.60),(80,4,4,118,16,7,2,2,0.30),(81,4,4,127,10,0,0,2,0.00),(82,4,4,130,15,3,2,0,0.30),(83,4,4,125,27,8,3,6,0.30),(84,5,7,161,28,19,5,0,0.40),(85,5,7,165,26,8,4,1,0.80),(86,5,7,157,22,11,1,6,0.40),(87,5,7,160,33,17,3,2,0.63),(88,5,7,153,36,13,2,7,0.71),(89,5,7,150,11,0,2,0,0.00),(90,5,7,154,21,3,6,1,0.14),(91,5,7,162,29,17,6,2,0.43),(92,5,7,152,12,10,3,0,0.57),(93,5,7,164,21,9,4,3,0.25),(94,5,6,137,33,9,7,12,1.00),(95,5,6,148,32,31,3,2,0.60),(96,5,6,143,17,9,3,2,1.00),(97,5,6,135,32,22,5,9,0.45),(98,5,6,147,27,18,0,0,0.45),(99,5,6,141,14,6,4,2,0.50),(100,5,6,138,12,5,6,0,0.43),(101,5,6,142,21,7,7,2,0.40),(102,5,6,134,4,3,1,0,0.75),(103,5,6,136,17,6,5,1,0.30),(104,5,6,145,22,8,1,5,0.20),(105,5,6,144,5,0,0,0,0.00),(106,5,6,146,5,0,1,1,0.00),(107,6,10,171,23,9,5,3,0.30),(108,6,10,173,19,20,6,0,0.38),(109,6,10,179,15,0,3,0,0.00),(110,6,10,168,35,20,7,10,0.44),(111,6,10,169,37,38,11,8,0.48),(112,6,10,175,31,8,7,0,0.50),(113,6,10,181,20,8,5,1,0.30),(114,6,10,167,32,12,5,0,0.65),(115,6,10,177,18,6,1,2,0.25),(116,6,13,197,38,17,2,4,0.62),(117,6,13,193,22,0,9,2,0.00),(118,6,13,187,38,42,2,3,0.61),(119,6,13,186,31,14,5,4,0.46),(120,6,13,185,34,12,7,3,0.27),(121,6,13,183,19,4,4,2,0.29),(122,6,13,194,14,6,2,1,0.60),(123,6,13,192,13,2,2,1,0.30),(124,6,13,190,10,5,2,0,0.40),(125,6,13,189,21,12,7,1,0.57),(126,7,11,206,35,13,5,3,0.60),(127,7,11,200,31,16,3,6,0.86),(128,7,11,216,30,25,9,6,0.64),(129,7,11,214,27,13,6,4,0.50),(130,7,11,201,33,19,2,3,0.54),(131,7,11,211,32,16,6,2,0.50),(132,7,11,205,2,3,0,0,1.00),(133,7,11,212,13,11,3,0,0.57),(134,7,11,207,22,6,2,11,0.60),(135,7,11,210,16,7,0,3,0.60),(136,7,14,226,31,17,3,1,0.75),(137,7,14,230,20,17,7,5,0.80),(138,7,14,222,27,11,1,4,0.40),(139,7,14,229,29,13,5,2,0.25),(140,7,14,223,29,21,2,4,0.38),(141,7,14,221,25,7,3,1,0.50),(142,7,14,219,24,17,6,2,0.75),(143,7,14,225,3,1,1,0,0.00),(144,7,14,227,18,9,1,1,0.43),(145,7,14,217,15,4,2,1,0.30),(146,7,14,228,19,0,2,6,0.00),(147,8,15,239,29,6,9,5,0.25),(148,8,15,235,33,18,5,4,0.58),(149,8,15,242,35,31,13,9,0.71),(150,8,15,244,28,13,4,6,0.40),(151,8,15,236,25,13,4,1,0.57),(152,8,15,240,22,10,4,3,0.38),(153,8,15,245,3,0,0,0,0.00),(154,8,15,250,3,0,0,0,0.00),(155,8,15,249,3,2,0,0,0.50),(156,8,15,237,3,0,0,0,0.00),(157,8,15,243,10,2,5,0,1.00),(158,8,15,248,3,0,1,1,0.00),(159,8,15,241,17,6,3,5,0.16),(160,8,15,247,3,0,1,0,0.00),(161,8,15,234,25,9,5,0,0.60),(162,8,12,38,36,22,14,5,0.58),(163,8,12,40,35,19,7,9,0.38),(164,8,12,34,29,6,4,3,0.25),(165,8,12,44,26,8,2,1,0.60),(166,8,12,48,30,15,2,1,0.43),(167,8,12,39,3,0,0,0,0.00),(168,8,12,35,28,6,5,4,0.34),(169,8,12,47,10,2,3,0,0.50),(170,8,12,41,12,4,4,0,0.50),(171,8,12,42,19,9,4,1,0.30),(172,8,12,37,3,2,1,1,0.00),(173,9,5,116,37,17,9,10,0.80),(174,9,5,100,28,6,2,2,0.25),(175,9,5,113,23,11,2,1,0.45),(176,9,5,104,29,11,5,5,0.30),(177,9,5,106,32,18,7,3,0.53),(178,9,5,109,11,4,0,0,0.50),(179,9,5,114,5,2,0,0,0.50),(180,9,5,110,25,7,3,2,0.29),(181,9,5,101,19,11,8,1,0.50),(182,9,5,112,30,30,1,8,0.71),(183,9,1,6,32,11,6,3,0.50),(184,9,1,5,40,13,8,7,0.43),(185,9,1,3,35,17,12,1,0.80),(186,9,1,12,24,5,2,7,0.20),(187,9,1,1,41,44,8,4,0.61),(188,9,1,15,3,0,0,0,0.00),(189,9,1,4,9,4,3,2,0.60),(190,9,1,9,4,2,0,1,0.00),(191,9,1,16,9,5,0,0,0.60),(192,9,1,10,25,15,4,1,0.54),(193,9,1,14,18,6,2,0,0.40);
/*!40000 ALTER TABLE `games_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `player_ID` int NOT NULL,
  `team_ID` int NOT NULL,
  `playerFirst` varchar(30) NOT NULL,
  `playerLast` varchar(30) NOT NULL,
  `playerAge` int DEFAULT NULL,
  `totalGames` int DEFAULT NULL,
  PRIMARY KEY (`player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,1,'Devin','Booker',26,2),(2,1,'Paul','Chris',36,0),(3,1,'Deandre','Ayton',24,2),(4,1,'Bismack','Biyombo',30,2),(5,1,'Mikal','Bridges',26,2),(6,1,'Torrey','Craig',31,1),(7,1,'Jae','Crowder',32,0),(8,1,'Cameron','Johnson',26,0),(9,1,'Jock','Landale',27,2),(10,1,'Damion','Lee',30,2),(11,1,'Josh','Okogie',24,1),(12,1,'Cameron','Payne',28,2),(13,1,'Dario','Saric',28,1),(14,1,'Landry','Shamet',25,2),(15,1,'Ish','Wainright',28,2),(16,1,'Duane','Washington Jr.',22,2),(17,2,'Dominick','Barlow',19,0),(18,2,'Charles','Bassey',22,1),(19,2,'Keita','Bates-Diop',26,1),(20,2,'Malaki','Branham',19,1),(21,2,'Zach','Collins',25,1),(22,2,'Gorgui','Dieng',32,1),(23,2,'Alize','Johnson',26,1),(24,2,'Keldon','Johnson',23,1),(25,2,'Tre','Jones',22,1),(26,2,'Romeo','Langford',23,1),(27,2,'Doug','McDermott',30,0),(28,2,'Jakob','Poeltl',27,0),(29,2,'Josh','Richardson',29,0),(30,2,'Isaiah','Roby',24,0),(31,2,'Devin','Vassell',22,1),(32,2,'Jeremy','Sochan',19,0),(33,2,'Blake','Wesley',19,0),(34,12,'Patrick','Beverley',34,2),(35,12,'Troy','Brown Jr.',23,2),(36,12,'Thomas','Bryant',25,1),(37,12,'Max','Christie',19,2),(38,12,'Anthony','Davis',29,2),(39,12,'Wenyen','Gabriel',25,2),(40,12,'Lebron','James',37,1),(41,12,'Damian','Jones',27,2),(42,12,'Kendrick','Nunn',27,2),(43,12,'Scotty','Pippen Jr.',22,0),(44,12,'Austin','Reaves',24,2),(45,12,'Dennis','Schroder',29,0),(46,12,'Cole','Swider',23,0),(47,12,'Juan','Toscano-Anderson',29,1),(48,12,'Lonnie','Walker IV',24,2),(49,12,'Russell','Westbrook',34,1),(50,8,'Ibou','Badji',20,0),(51,8,'Greg','Brown III',21,1),(52,8,'John','Butler Jr.',20,1),(53,8,'Drew','Eubanks',25,1),(54,8,'Jerami','Grant',28,1),(55,8,'Josh','Hart',27,0),(56,8,'Keon','Johnson',20,0),(57,8,'Damian','Lillard',32,0),(58,8,'Nassir','Little',22,0),(59,8,'Jusuf','Nurkic',28,1),(60,8,'Gary','Payton II',30,0),(61,8,'Shaedon','Sharpe',19,1),(62,8,'Anfernee','Simons',23,1),(63,8,'Jabari','Walker',20,1),(64,8,'Trendon','Watford',22,1),(65,8,'Justise','Winslow',26,1),(66,9,'Ochai','Agbaji',22,0),(67,9,'Nickeil','Alexander-Walker',24,1),(68,9,'Udoka','Azubuike',23,1),(69,9,'Malik','Beasley',26,1),(70,9,'Leandro','Bolmaro',22,0),(71,9,'Jordan','Clarkson',30,1),(72,9,'Mike','Conley',35,1),(73,9,'Simone','Fontecchio',27,0),(74,9,'Rudy','Gay',36,1),(75,9,'Talen','Horton-Tucker',22,0),(76,9,'Johnny','Juzang',21,0),(77,9,'Walker','Kessler',21,1),(78,9,'Lauri','Markkanen',25,1),(79,9,'Kelly','Olynyk',31,1),(80,9,'Micah','Potter',24,0),(81,9,'Collin','Sexton',23,0),(82,9,'Jarred','Vanderbilt',23,1),(83,3,'Jose','Alvarado',24,0),(84,3,'Dyson','Daniels',19,1),(85,3,'Devonte','Graham',27,1),(86,3,'Jaxson','Hayes',22,0),(87,3,'Willy','Hernangomez',28,0),(88,3,'Brandon','Ingram',25,0),(89,3,'Herbert','Jones',24,1),(90,3,'Kira','Lewis Jr.',21,0),(91,3,'E.J.','Liddell',21,0),(92,3,'Naji','Marshall',24,1),(93,3,'CJ','McCollum',31,1),(94,3,'Trey','Murphy III',22,1),(95,3,'Larry','Nance Jr.',29,1),(96,3,'Dereon','Seabron',22,0),(97,3,'Garrett','Temple',36,0),(98,3,'Jonas','Valanciunas',30,1),(99,3,'Zion','Williamson',22,1),(100,5,'Harrison','Barnes',30,2),(101,5,'Terence','Davis',25,1),(102,5,'Matthew','Dellavedova',32,0),(103,5,'Keon','Ellis',22,0),(104,5,'De\'Aaron','Fox',24,2),(105,5,'Richaun','Holmes',29,0),(106,5,'Kevin','Huerter',24,2),(107,5,'Alex','Len',29,0),(108,5,'Trey','Lyles',27,1),(109,5,'Chimezie','Metu',25,2),(110,5,'Davion','Mitchell',24,2),(111,5,'Chima','Moneke',26,0),(112,5,'Malik','Monk',24,2),(113,5,'Keegan','Murray',22,2),(114,5,'KZ','Okpala',23,1),(115,5,'Neemias','Queta',23,0),(116,5,'Domantas','Sabonis',26,2),(117,4,'Steven','Adams',29,0),(118,4,'Santi','Aldama',21,1),(119,4,'Desmond','Bane',24,0),(120,4,'Dillon','Brooks',26,1),(121,4,'Kennedy','Chandler',20,0),(122,4,'Brandon','Clarke',26,1),(123,4,'Danny','Green',35,0),(124,4,'Jaren','Jackson Jr.',23,1),(125,4,'Tyus','Jones',26,1),(126,4,'John','Konchar',26,1),(127,4,'Jake','LaRavia',21,1),(128,4,'Kenneth','Lofton Jr.',20,0),(129,4,'Ja','Morant',23,1),(130,4,'David','Roddy',21,1),(131,4,'Xavier','Tillman',23,0),(132,4,'Ziaire','Williams',21,0),(133,4,'Vince','Williams Jr.',22,0),(134,6,'Patrick','Baldwin Jr.',20,1),(135,6,'Stephen','Curry',34,1),(136,6,'Donte','DiVincenzo',25,1),(137,6,'Draymond','Green',32,1),(138,6,'JaMychal','Green',32,1),(139,6,'Andre','Iguodala',38,0),(140,6,'Ty','Jerome',25,0),(141,6,'Jonathan','Kuminga',20,1),(142,6,'Anthony','Lamb',24,1),(143,6,'Kevon','Looney',26,1),(144,6,'Moses','Moody',20,1),(145,6,'Jordan','Poole',23,1),(146,6,'Ryan','Rollins',20,1),(147,6,'Klay','Thompson',32,1),(148,6,'Andrew','Wiggins',27,1),(149,6,'James','Wiseman',21,0),(150,7,'Nicolas','Batum',34,1),(151,7,'Brandon','Boston Jr.',21,0),(152,7,'Moses','Brown',23,1),(153,7,'Amir','Coffey',25,1),(154,7,'Robert','Covington',32,1),(155,7,'Moussa','Diabate',20,0),(156,7,'Paul','George',32,0),(157,7,'Reggie','Jackson',32,1),(158,7,'Luke','Kennard',26,0),(159,7,'Kawhi','Leonard',31,0),(160,7,'Terance','Mann',26,1),(161,7,'Marcus','Morris Sr.',33,1),(162,7,'Norman','Powell',29,1),(163,7,'Jason','Preston',23,0),(164,7,'John','Wall',32,1),(165,7,'Ivica','Zubac',25,1),(166,10,'Davis','Bertans',30,0),(167,10,'Reggie','Bullock',31,1),(168,10,'Spencer','Dinwiddie',29,1),(169,10,'Luka','Doncic',23,1),(170,10,'Tyler','Dorsey',26,0),(171,10,'Dorain','Finney-Smith',29,1),(172,10,'Josh','Green',22,0),(173,10,'Tim','Hardaway Jr.',30,1),(174,10,'Jaden','Hardy',20,0),(175,10,'Maxi','Kleber',30,1),(176,10,'JaVale','McGee',34,0),(177,10,'Frank','Ntilikina',24,1),(178,10,'Theo','Pinson',27,0),(179,10,'Dwight','Powell',31,1),(180,10,'Kemba','Walker',32,0),(181,10,'Christian','Wood',27,1),(182,10,'McKinley','Wright IV',24,0),(183,13,'Darius','Bazley',22,1),(184,13,'Ousmane','Dieng',19,0),(185,13,'Luguentz','Dort',23,1),(186,13,'Josh','Giddey',20,1),(187,13,'Shai','Gilgeous-Alexander',24,1),(188,13,'Chet','Holmgren',20,0),(189,13,'Isaiah','Joe',23,1),(190,13,'Tre','Mann',21,1),(191,13,'Mike','Muscala',31,0),(192,13,'Eugene','Omoruyi',25,1),(193,13,'Aleksej','Pokusevski',20,1),(194,13,'Jeremiah','Robinson-Earl',22,1),(195,13,'Lindy','Water III',25,0),(196,13,'Aaron','Wiggins',23,0),(197,13,'Jalen','Williams',21,1),(198,13,'Jaylin','Williams',20,0),(199,13,'Kenrich','Williams',28,0),(200,11,'Kyle','Anderson',29,1),(201,11,'Anthony','Edwards',21,1),(202,11,'Bryn','Forbes',29,0),(203,11,'Luka','Garza',23,0),(204,11,'Rudy','Gobert',30,0),(205,11,'Nathan','Knight',25,1),(206,11,'Jaden','McDaniels',22,1),(207,11,'Jordan','McLaughlin',26,1),(208,11,'Josh','Minott',20,0),(209,11,'Wendell','Moore Jr.',21,0),(210,11,'Jaylen','Nowell',23,1),(211,11,'Taurean','Prince',28,1),(212,11,'Naz','Reid',23,1),(213,11,'Austin','Rivers',30,0),(214,11,'D\'Angelo','Russell',26,1),(215,11,'Matt','Ryan',25,0),(216,11,'Karl-Anthony','Towns',27,1),(217,14,'Josh','Christopher',21,1),(218,14,'Darius','Days',23,0),(219,14,'Tari','Eason',21,1),(220,14,'Bruno','Fernando',24,0),(221,14,'Usman','Garuba',20,1),(222,14,'Eric','Gordon',33,1),(223,14,'Jalen','Green',20,1),(224,14,'Trevor','Hudgins',23,0),(225,14,'Boban','Marjanovic',34,1),(226,14,'Kenyon','Martin Jr.',21,1),(227,14,'Garrison','Mathews',26,1),(228,14,'Daishen','Nix',20,1),(229,14,'Kevin','Porter Jr.',22,1),(230,14,'Alperen','Sengun',20,1),(231,14,'Jabari','Smith Jr.',19,0),(232,14,'Jae\'Sean','Tate',27,0),(233,14,'TyTy','Washinton Jr.',21,0),(234,15,'Christian','Braun',21,1),(235,15,'Bruce','Brown',26,1),(236,15,'Kentavious','Caldwell-Pope',29,1),(237,15,'Flatko','Cancar',25,0),(238,15,'Collin','Gillespie',23,0),(239,15,'Aaron','Gordon',27,1),(240,15,'Jeff','Green',36,1),(241,15,'Bones','Hyland',22,1),(242,15,'Nikola','Jokic',27,1),(243,15,'DeAndre','Jordan',34,1),(244,15,'Jamal','Murray',25,1),(245,15,'Zeke','Nnaji',21,1),(246,15,'Michael','Porter Jr.',24,0),(247,15,'Davon','Reed',27,1),(248,15,'Ish','Smith',34,1),(249,15,'Peyton','Watson',20,1),(250,15,'Jack','White',25,1);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ranking`
--

DROP TABLE IF EXISTS `ranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ranking` (
  `team_ID` int NOT NULL,
  `conference` varchar(30) DEFAULT NULL,
  `totalGames` int DEFAULT NULL,
  `wins` int DEFAULT NULL,
  `losses` int DEFAULT NULL,
  PRIMARY KEY (`team_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ranking`
--

LOCK TABLES `ranking` WRITE;
/*!40000 ALTER TABLE `ranking` DISABLE KEYS */;
INSERT INTO `ranking` VALUES (1,'West',2,2,0),(2,'West',1,0,1),(3,'West',1,0,1),(4,'West',1,0,1),(5,'West',1,1,0),(6,'West',2,1,1),(7,'West',1,0,1),(8,'West',1,0,1),(9,'West',1,1,0),(10,'West',1,1,0),(11,'West',1,1,0),(12,'West',2,1,1),(13,'West',1,0,1),(14,'West',1,0,1),(15,'West',1,1,0);
/*!40000 ALTER TABLE `ranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `team_ID` int NOT NULL,
  `teamName` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `arena` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`team_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'Suns','Phoenix','Footprint Center'),(2,'Spurs','San Antonio','AT&T Center'),(3,'Pelicans','New Orleans','Smoothie King Center'),(4,'Grizzlies','Memphis','FedExForum'),(5,'Kings','Sacramento','Golden 1 Center'),(6,'Warriors','San Francisco','Chase Center'),(7,'Clippers','Los Angeles','Staples Center'),(8,'Trail Blazers','Portland','Moda Center'),(9,'Jazz','Utah','Vivint Smart Home Arena'),(10,'Mavericks','Dallas','American Airlines Center'),(11,'Timberwolves','Minnesota','Target Center'),(12,'Lakers','Los Angeles','Staples Center'),(13,'Thunder','Oklahoma City','Chesapeake Energy Arena'),(14,'Rockets','Houston','Toyota Center'),(15,'Nuggets','Denver','Pepsi Center');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `with5`
--

DROP TABLE IF EXISTS `with5`;
/*!50001 DROP VIEW IF EXISTS `with5`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `with5` AS SELECT 
 1 AS `CONCAT(playerFirst, " ", playerLast)`,
 1 AS `points`,
 1 AS `rebounds`,
 1 AS `assists`,
 1 AS `gameDATE`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'nba'
--

--
-- Dumping routines for database 'nba'
--

--
-- Final view structure for view `with5`
--

/*!50001 DROP VIEW IF EXISTS `with5`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `with5` AS select concat(`p`.`playerFirst`,' ',`p`.`playerLast`) AS `CONCAT(playerFirst, " ", playerLast)`,`gd`.`points` AS `points`,`gd`.`rebounds` AS `rebounds`,`gd`.`assists` AS `assists`,`g`.`gameDATE` AS `gameDATE` from ((`players` `p` join `games_details` `gd` on((`p`.`player_ID` = `gd`.`playerID`))) join `games` `g` on((`gd`.`game_ID` = `g`.`game_ID`))) where ((`gd`.`points` >= 5) and (`gd`.`rebounds` >= 5) and (`gd`.`assists` >= 5)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-16 22:04:27
