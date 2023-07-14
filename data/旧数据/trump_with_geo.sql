/*
 Navicat Premium Data Transfer

 Source Server         : MyMariaDB
 Source Server Type    : MariaDB
 Source Server Version : 100605 (10.6.5-MariaDB-1:10.6.5+maria~focal)
 Source Host           : localhost:3306
 Source Schema         : USSchedule

 Target Server Type    : MariaDB
 Target Server Version : 100605 (10.6.5-MariaDB-1:10.6.5+maria~focal)
 File Encoding         : 65001

 Date: 10/04/2023 23:33:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for trump_with_geo
-- ----------------------------
DROP TABLE IF EXISTS `trump_with_geo`;
CREATE TABLE `trump_with_geo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `date` date NULL DEFAULT NULL,
  `lastname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `text` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `links` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `count` int(11) NULL DEFAULT NULL,
  `rank` tinyint(4) NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `travel_places` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `travel_start_date` date NULL DEFAULT NULL,
  `travel_end_date` date NULL DEFAULT NULL,
  `topics` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `meet_countries` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `link_content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9021 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
