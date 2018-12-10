-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 13, 2018 at 11:04 AM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `sia`
--

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE IF NOT EXISTS `staff` (
  `UserId` varchar(3) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `PhoneNo` int(12) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Depart` varchar(30) NOT NULL,
  `Qualifi` varchar(50) NOT NULL,
  PRIMARY KEY (`UserId`),
  KEY `UserId` (`UserId`),
  KEY `UserId_2` (`UserId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`UserId`, `Name`, `Email`, `PhoneNo`, `Gender`, `Depart`, `Qualifi`) VALUES
('1A', 'gowtham', 'nandha@gmail.com', 69851412, 'MALE', 'IT', 'M.E'),
('102', 'PANDI', 'miya@gmail.com', 2147483647, 'Male', 'mca', 'b.sc'),
('103', 'ranjith', 'ranjith@gmail.com', 52856458, 'Male', 'ece', 'be'),
('104', 'nivi', 'nivi@gmai.com', 25445125, 'Female', 'mca', 'b.sc'),
('105', 'gow', 'fed', 68797, 'Female', 'mca', 'b.sc'),
('106', 'arun', 'arun@gmeil.com', 56248926, 'Male', 'eee', 'be'),
('108', 'nivi', 'nivi@gmai.com', 25445125, 'Female', 'ece', 'be');
