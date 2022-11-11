/*
 Navicat Premium Data Transfer

 Source Server         : MySQL5.+
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : day29

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 11/11/2022 23:47:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `article_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `read_num` int(11) NULL DEFAULT 0,
  `comment_num` int(11) NULL DEFAULT 0,
  `up_num` int(11) NULL DEFAULT 0,
  `down_num` int(11) NULL DEFAULT 0,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_article_userinfo`(`user_id`) USING BTREE,
  CONSTRAINT `fk_article_userinfo` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES (1, '白衣胜雪', '执天问道何有期？尽诛邪魔无穷极。除却君身三重雪，天下谁人胜白衣。', '2022-11-11 20:37:39', 7, 2, 0, 0, 1);
INSERT INTO `article` VALUES (2, '江南曲', '嫁得瞿塘贾，朝朝误妾期。', '2022-11-11 20:40:34', 2, 1, 0, 0, 1);
INSERT INTO `article` VALUES (3, '送别', '山中相送罢，日暮掩柴扉。春草明年绿，王孙归不归？', '2022-11-11 20:55:19', 3, 0, 0, 0, 2);
INSERT INTO `article` VALUES (4, '春思', '燕草如碧丝，秦桑低绿枝。当君怀归日，是妾断肠时。春风不相识，何事入罗帏。', '2022-11-11 20:55:43', 0, 0, 0, 0, 2);
INSERT INTO `article` VALUES (5, '月夜', '更深月色半人家，北斗阑干南斗斜。今夜偏知春气暖，虫声新透绿窗纱。', '2022-11-11 22:01:12', 4, 2, 0, 0, 1);

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `comment_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_comment_userinfo`(`user_id`) USING BTREE,
  INDEX `fk_comment_article`(`article_id`) USING BTREE,
  CONSTRAINT `fk_comment_article` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_comment_userinfo` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES (1, 'hkw发表评论1', '2022-11-11 22:57:35', 1, 1);
INSERT INTO `comment` VALUES (2, 'jon_comment_1', '2022-11-11 23:28:41', 2, 1);
INSERT INTO `comment` VALUES (3, 'hkw_comment_2_article2', '2022-11-11 23:39:07', 1, 2);
INSERT INTO `comment` VALUES (4, 'hkw_comment_articl5', '2022-11-11 23:46:40', 1, 5);
INSERT INTO `comment` VALUES (5, '666', '2022-11-11 23:46:51', 1, 5);

-- ----------------------------
-- Table structure for up_and_down
-- ----------------------------
DROP TABLE IF EXISTS `up_and_down`;
CREATE TABLE `up_and_down`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `up_num` int(11) NULL DEFAULT 0,
  `down_num` int(11) NULL DEFAULT 0,
  `ctime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_updown_userinfo`(`user_id`) USING BTREE,
  INDEX `fk_updown_article`(`article_id`) USING BTREE,
  CONSTRAINT `fk_updown_article` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_updown_userinfo` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of up_and_down
-- ----------------------------
INSERT INTO `up_and_down` VALUES (1, 1, 0, '2022-11-11 23:28:44', 2, 1);
INSERT INTO `up_and_down` VALUES (2, 0, 1, '2022-11-11 23:28:49', 2, 1);
INSERT INTO `up_and_down` VALUES (3, 1, 0, '2022-11-11 23:39:10', 1, 2);
INSERT INTO `up_and_down` VALUES (4, 0, 1, '2022-11-11 23:39:12', 1, 2);
INSERT INTO `up_and_down` VALUES (5, 1, 0, '2022-11-11 23:40:33', 1, 3);
INSERT INTO `up_and_down` VALUES (6, 1, 0, '2022-11-11 23:46:52', 1, 5);

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nickname` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_username`(`username`) USING BTREE,
  UNIQUE INDEX `ix_phone`(`phone`) USING BTREE,
  UNIQUE INDEX `ix_email`(`email`) USING BTREE,
  INDEX `ix_user_pwd`(`username`, `password`) USING BTREE,
  INDEX `ix_nick_pwd`(`nickname`, `password`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES (1, 'hkw', 'hkwJsxl', 'ed7744e5e18166b037934e20f7ff0b91', '18533538210', 'hkwJsxl@gmail.com', '2022-11-11 17:43:34');
INSERT INTO `userinfo` VALUES (2, 'jon', 'jonhappy', '3775135450c579ce7ff7b30ec6c48581', '18533538211', 'jonhappy@gmail.com', '2022-11-11 17:46:13');

SET FOREIGN_KEY_CHECKS = 1;
