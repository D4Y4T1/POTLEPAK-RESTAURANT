-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jan 15, 2024 at 07:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `potlepak restaurant`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Cus_Name` varchar(30) NOT NULL,
  `Cus_Phone` int(13) NOT NULL,
  `Cus_ID` int(10) NOT NULL,
  `Birth_Day` int(2) NOT NULL,
  `Birth_Month` int(2) NOT NULL,
  `Birth_Year` int(4) NOT NULL,
  `Cus_Age` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) NOT NULL,
  `Age` int(3) NOT NULL,
  `Number_Phone` int(13) NOT NULL,
  `Gender` varchar(7) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `ID` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`First_Name`, `Last_Name`, `Age`, `Number_Phone`, `Gender`, `Email`, `ID`) VALUES
('hidayati', 'jakaria', 21, 123456789, '', '12345678', 0);

-- --------------------------------------------------------

--
-- Table structure for table `table reservation`
--

CREATE TABLE `table reservation` (
  `Table_Number` int(2) NOT NULL,
  `Number_of_Customer` int(2) NOT NULL,
  `Day` int(2) NOT NULL,
  `Month` int(2) NOT NULL,
  `Year` int(4) NOT NULL,
  `Deposit` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `table reservation`
--

INSERT INTO `table reservation` (`Table_Number`, `Number_of_Customer`, `Day`, `Month`, `Year`, `Deposit`) VALUES
(4, 10, 12, 2, 2023, 50);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
