LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Main','User','muser@email.com','12345','2024-01-18 10:15:03','willie1',1),
    (2,'Willie','Nelson','willie.nelson@email.com','12345','2024-01-18 21:40:15','willie1',2),
    (3,'James','Hetfield','jhetfield@email.com','12345','2024-01-25 05:12:45','willie1',3),
    (4,'Amelia','Earhart','aearhart@email.com','12345','2024-01-29 16:24:33','willie1',4),
    (5,'Peewee','Herman','pherman@email.com','12345','2024-01-25 05:12:45','willie1',5),
    (6,'Steve','Rogers','srogers@email.com','12345','2024-01-30 05:29:22','willie1',6),
    (7,'Jimmy','John','jjohn@email.com','12345','2024-01-25 05:12:45','willie1',7),
    (8,'Ronald','McDonald','rmcdonald@email.com','12345','2024-02-08 18:41:45','willie1',8),
    (9,'Mario','Jumpman','mjumpman@email.com','12345','2024-02-08 18:53:37','willie1',9),
    (10,'Abraham','Lincoln','alincoln@email.com','12345','2024-02-08 19:26:06','willie1',10),
    (11,'Jimmy','Dean','jdean@email.com','12345','2024-02-08 19:38:18','willie1',11),
    (12,'Sam','Adams','sadams@email.com','12345','2024-02-09 00:38:52','willie1',12),
    (13,'George','Washington','gwashington@eamil.com','12345','2024-02-09 00:40:21','willie1',13),
    (14,'Thomas','Edison','tedison@email.com','12345','2024-02-09 00:42:45','willie1',14),
    (15,'Albert','Einstein','aeinstein@email.com','12345','2024-02-09 00:44:42','willie1',15),
    (16,'Jack','Frost','jfrost@email.com','12345','2024-02-09 00:47:24','willie1',16),
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;