-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 11 fév. 2021 à 18:17
-- Version du serveur :  10.4.17-MariaDB
-- Version de PHP : 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `flask_blog`
--

-- Détection si une autre base de donnée du même nom existe
DROP DATABASE IF EXISTS flask_blog;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS flask_blog;

-- Utilisation de cette base de donnée

USE flask_blog;

-- --------------------------------------------------------

--
-- Structure de la table `t_countries`
--

CREATE TABLE `t_countries` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `t_countries`
--

INSERT INTO `t_countries` (`id`, `name`) VALUES
(1, 'Afghanistan'),
(2, 'Åland Islands'),
(3, 'Albania'),
(4, 'Algeria'),
(5, 'American Samoa'),
(6, 'Andorra'),
(7, 'Angola'),
(8, 'Anguilla'),
(9, 'Antarctica'),
(10, 'Antigua and Barbuda'),
(11, 'Argentina'),
(12, 'Armenia'),
(13, 'Aruba'),
(14, 'Australia'),
(15, 'Austria'),
(16, 'Azerbaijan'),
(17, 'Bahamas'),
(18, 'Bahrain'),
(19, 'Bangladesh'),
(20, 'Barbados'),
(21, 'Belarus'),
(22, 'Belgium'),
(23, 'Belize'),
(24, 'Benin'),
(25, 'Bermuda'),
(26, 'Bhutan'),
(27, 'Bosnia and Herzegovina'),
(28, 'Botswana'),
(29, 'Bouvet Island'),
(30, 'Brazil'),
(31, 'British Indian Ocean Territory'),
(32, 'Brunei Darussalam'),
(33, 'Bulgaria'),
(34, 'Burkina Faso'),
(35, 'Burundi'),
(36, 'Cambodia'),
(37, 'Cameroon'),
(38, 'Canada'),
(39, 'Cape Verde'),
(40, 'Cayman Islands'),
(41, 'Central African Republic'),
(42, 'Chad'),
(43, 'Chile'),
(44, 'China'),
(45, 'Christmas Island'),
(46, 'Cocos (Keeling) Islands'),
(47, 'Colombia'),
(48, 'Comoros'),
(49, 'Congo'),
(50, 'Cook Islands'),
(51, 'Costa Rica'),
(52, 'Croatia'),
(53, 'Cuba'),
(54, 'CuraÃ§ao'),
(55, 'Cyprus'),
(56, 'Czech Republic'),
(57, 'Denmark'),
(58, 'Djibouti'),
(59, 'Dominica'),
(60, 'Dominican Republic'),
(61, 'Ecuador'),
(62, 'Egypt'),
(63, 'El Salvador'),
(64, 'Equatorial Guinea'),
(65, 'Eritrea'),
(66, 'Estonia'),
(67, 'Ethiopia'),
(68, 'Falkland Islands (Malvinas)'),
(69, 'Faroe Islands'),
(70, 'Fiji'),
(71, 'Finland'),
(72, 'France'),
(73, 'French Guiana'),
(74, 'French Polynesia'),
(75, 'French Southern Territories'),
(76, 'Gabon'),
(77, 'Gambia'),
(78, 'Georgia'),
(79, 'Germany'),
(80, 'Ghana'),
(81, 'Gibraltar'),
(82, 'Greece'),
(83, 'Greenland'),
(84, 'Grenada'),
(85, 'Guadeloupe'),
(86, 'Guam'),
(87, 'Guatemala'),
(88, 'Guernsey'),
(89, 'Guinea'),
(90, 'Guinea-Bissau'),
(91, 'Guyana'),
(92, 'Haiti'),
(93, 'Heard Island and McDonald Islands'),
(94, 'Holy See (Vatican City State)'),
(95, 'Honduras'),
(96, 'Hong Kong'),
(97, 'Hungary'),
(98, 'Iceland'),
(99, 'India'),
(100, 'Indonesia'),
(101, 'Iraq'),
(102, 'Ireland'),
(103, 'Isle of Man'),
(104, 'Israel'),
(105, 'Italy'),
(106, 'Jamaica'),
(107, 'Japan'),
(108, 'Jersey'),
(109, 'Jordan'),
(110, 'Kazakhstan'),
(111, 'Kenya'),
(112, 'Kiribati'),
(113, 'Kuwait'),
(114, 'Kyrgyzstan'),
(115, 'Latvia'),
(116, 'Lebanon'),
(117, 'Lesotho'),
(118, 'Liberia'),
(119, 'Libya'),
(120, 'Liechtenstein'),
(121, 'Lithuania'),
(122, 'Luxembourg'),
(123, 'Macao'),
(124, 'Madagascar'),
(125, 'Malawi'),
(126, 'Malaysia'),
(127, 'Maldives'),
(128, 'Mali'),
(129, 'Malta'),
(130, 'Marshall Islands'),
(131, 'Martinique'),
(132, 'Mauritania'),
(133, 'Mauritius'),
(134, 'Mayotte'),
(135, 'Mexico'),
(136, 'Monaco'),
(137, 'Mongolia'),
(138, 'Montenegro'),
(139, 'Montserrat'),
(140, 'Morocco'),
(141, 'Mozambique'),
(142, 'Myanmar'),
(143, 'Namibia'),
(144, 'Nauru'),
(145, 'Nepal'),
(146, 'Netherlands'),
(147, 'New Caledonia'),
(148, 'New Zealand'),
(149, 'Nicaragua'),
(150, 'Niger'),
(151, 'Nigeria'),
(152, 'Niue'),
(153, 'Norfolk Island'),
(154, 'Northern Mariana Islands'),
(155, 'Norway'),
(156, 'Oman'),
(157, 'Pakistan'),
(158, 'Palau'),
(159, 'Panama'),
(160, 'Papua New Guinea'),
(161, 'Paraguay'),
(162, 'Peru'),
(163, 'Philippines'),
(164, 'Pitcairn'),
(165, 'Poland'),
(166, 'Portugal'),
(167, 'Puerto Rico'),
(168, 'Qatar'),
(169, 'RÃ©union'),
(170, 'Romania'),
(171, 'Russian Federation'),
(172, 'Rwanda'),
(173, 'Saint BarthÃ©lemy'),
(174, 'Saint Kitts and Nevis'),
(175, 'Saint Lucia'),
(176, 'Saint Martin (French part)'),
(177, 'Saint Pierre and Miquelon'),
(178, 'Saint Vincent and the Grenadines'),
(179, 'Samoa'),
(180, 'San Marino'),
(181, 'Sao Tome and Principe'),
(182, 'Saudi Arabia'),
(183, 'Senegal'),
(184, 'Serbia'),
(185, 'Seychelles'),
(186, 'Sierra Leone'),
(187, 'Singapore'),
(188, 'Sint Maarten (Dutch part)'),
(189, 'Slovakia'),
(190, 'Slovenia'),
(191, 'Solomon Islands'),
(192, 'Somalia'),
(193, 'South Africa'),
(194, 'South Georgia and the South Sandwich Islands'),
(195, 'South Sudan'),
(196, 'Spain'),
(197, 'Sri Lanka'),
(198, 'Sudan'),
(199, 'Suriname'),
(200, 'Svalbard and Jan Mayen'),
(201, 'Swaziland'),
(202, 'Sweden'),
(203, 'Switzerland'),
(204, 'Syrian Arab Republic'),
(205, 'Tajikistan'),
(206, 'Thailand'),
(207, 'Timor-Leste'),
(208, 'Togo'),
(209, 'Tokelau'),
(210, 'Tonga'),
(211, 'Trinidad and Tobago'),
(212, 'Tunisia'),
(213, 'Turkey'),
(214, 'Turkmenistan'),
(215, 'Turks and Caicos Islands'),
(216, 'Tuvalu'),
(217, 'Uganda'),
(218, 'Ukraine'),
(219, 'United Arab Emirates'),
(220, 'United Kingdom'),
(221, 'United States'),
(222, 'United States Minor Outlying Islands'),
(223, 'Uruguay'),
(224, 'Uzbekistan'),
(225, 'Vanuatu'),
(226, 'Viet Nam'),
(227, 'Wallis and Futuna'),
(228, 'Western Sahara'),
(229, 'Yemen'),
(230, 'Zambia'),
(231, 'Zimbabwe');

-- --------------------------------------------------------

--
-- Structure de la table `t_genders`
--

CREATE TABLE `t_genders` (
  `id` int(11) NOT NULL,
  `gender` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `t_genders`
--

INSERT INTO `t_genders` (`id`, `gender`) VALUES
(1, 'Homme'),
(2, 'Femme'),
(3, 'Hélicoptère'),
(5, 'Bouteille'),
(6, 'Manche à couille');

-- --------------------------------------------------------

--
-- Structure de la table `t_logs`
--

CREATE TABLE `t_logs` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `log_type_id` int(11) NOT NULL,
  `sql_executed` text NOT NULL,
  `value_before` varchar(255) DEFAULT NULL,
  `value_after` varchar(255) DEFAULT NULL,
  `success` tinyint(1) NOT NULL,
  `error_message` varchar(255) DEFAULT NULL,
  `deleted_data` text DEFAULT NULL,
  `log_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `t_logs`
--

INSERT INTO `t_logs` (`id`, `user_id`, `log_type_id`, `sql_executed`, `value_before`, `value_after`, `success`, `error_message`, `deleted_data`, `log_date`) VALUES
(1, NULL, 14, 'INSERT INTO t_users (`permission`, `first_name`, `last_name`, `email`, `country`, `username`, `password`, `reset_password_permission`, `files`, `gender`, `reset_password_random`) VALUES (1, \'asdf\', \'asdf\', \'a@a.com\', 1, \'Jack\', \'$5$rounds=535000$kkQXTD5OouRxuyvH$AYMK5mB9SlD8TVTMgjrx7FC5zrjVu85cMZBKH7f3S78\', \'no_reset\', \'admin.png\', 1, \'Default_value\')', NULL, NULL, 0, '(1062, Duplicate entry \'Jack\' for key \'username unique\')', NULL, '2021-02-11 17:09:25'),
(2, NULL, 14, 'INSERT INTO t_users (`permission`, `first_name`, `last_name`, `email`, `country`, `username`, `password`, `reset_password_permission`, `files`, `gender`, `reset_password_random`) VALUES (1, \'ad\', \'sadd\', \'a@a.com\', 1, \'Jack\', \'$5$rounds=535000$H3DfQPnQfe6KovyR$ym/OeOim11dbzh0yeyrPl1/rELsHSivA9LSHwq4bVm2\', \'no_reset\', \'admin.png\', 1, \'Default_value\')', NULL, NULL, 0, '(1062, \"Duplicate entry \'Jack\' for key \'username unique\'\")', NULL, '2021-02-11 17:34:26');

-- --------------------------------------------------------

--
-- Structure de la table `t_log_types`
--

CREATE TABLE `t_log_types` (
  `id` int(11) NOT NULL,
  `log_type` varchar(50) NOT NULL,
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `t_log_types`
--

INSERT INTO `t_log_types` (`id`, `log_type`, `designation`) VALUES
(1, 'add_country', 'Add a country'),
(2, 'delete_country', 'Delete a country'),
(3, 'update_coutry', 'Update a country'),
(4, 'add_gender', 'Add a gender'),
(5, 'delete_gender', 'Delete a gender'),
(6, 'update_gender', 'Update a gender'),
(7, 'add_permission', 'Add a permission'),
(8, 'delete_permission', 'Delete a permission'),
(9, 'update_permission', 'Update a permission'),
(10, 'add_user', 'Add a user'),
(11, 'delete_user', 'Delete a user'),
(12, 'update_user_permission', 'Update a user\'s permission'),
(13, 'update_user_fname', 'Update a user\'s first name'),
(14, 'update_user_lname', 'Update a user\'s last name'),
(15, 'update_user_email', 'Update a user\'s email'),
(16, 'update_user_gender', 'Update a user\'s gender'),
(17, 'update_user_country', 'Update a user\'s country'),
(18, 'update_user_username', 'Update a user\'s username'),
(19, 'update_user_password', 'Update a user\'s password'),
(20, 'update_user_reset_password_permission', 'Update a user\'s reset permission'),
(21, 'update_user_reset_password_random', 'Update a user\'s key to reset his password'),
(22, 'update_user_files', 'Update a user\'s profile picture'),
(23, 'add_post', 'Add a post'),
(24, 'delete_post', 'Delete a post'),
(25, 'update_post', 'Update a post');

-- --------------------------------------------------------

--
-- Structure de la table `t_permissions`
--

CREATE TABLE `t_permissions` (
  `id` int(11) NOT NULL,
  `permission` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `t_permissions`
--

INSERT INTO `t_permissions` (`id`, `permission`) VALUES
(1, 'user'),
(2, 'modo'),
(3, 'admin');

-- --------------------------------------------------------

--
-- Structure de la table `t_posts`
--

CREATE TABLE `t_posts` (
  `id` int(11) NOT NULL,
  `author` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `content` text NOT NULL,
  `date_posted` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `t_users`
--

CREATE TABLE `t_users` (
  `id` int(11) NOT NULL,
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
  `register_date` timestamp NULL DEFAULT current_timestamp() COMMENT 'la date de creation du client'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='utilisateurs';

--
-- Déchargement des données de la table `t_users`
--

INSERT INTO `t_users` (`id`, `permission`, `first_name`, `last_name`, `email`, `gender`, `country`, `username`, `password`, `reset_password_permission`, `reset_password_random`, `files`, `register_date`) VALUES
(1, 3, 'Jack', 'OWheel', 'exemple@exemple.com', 3, 98, 'Jack', '$5$rounds=535000$MQt8BJ0dVoLMHmGU$QmEmV5ywx.bAXHvwSv6j/3XgK7nPSLhLiAbx7JhThq4', 'no_reset', 'Default_value', 'admin.png', '2021-02-11 09:41:59');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `t_countries`
--
ALTER TABLE `t_countries`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `t_genders`
--
ALTER TABLE `t_genders`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `t_logs`
--
ALTER TABLE `t_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `log_type_id` (`log_type_id`);

--
-- Index pour la table `t_log_types`
--
ALTER TABLE `t_log_types`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `t_permissions`
--
ALTER TABLE `t_permissions`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `t_posts`
--
ALTER TABLE `t_posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author` (`author`);

--
-- Index pour la table `t_users`
--
ALTER TABLE `t_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email unique` (`email`),
  ADD UNIQUE KEY `username unique` (`username`),
  ADD KEY `fk_permission` (`permission`),
  ADD KEY `fk_country` (`country`),
  ADD KEY `fk_gender` (`gender`) USING BTREE;

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `t_countries`
--
ALTER TABLE `t_countries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=232;

--
-- AUTO_INCREMENT pour la table `t_genders`
--
ALTER TABLE `t_genders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `t_logs`
--
ALTER TABLE `t_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `t_log_types`
--
ALTER TABLE `t_log_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT pour la table `t_permissions`
--
ALTER TABLE `t_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `t_posts`
--
ALTER TABLE `t_posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_users`
--
ALTER TABLE `t_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `t_logs`
--
ALTER TABLE `t_logs`
  ADD CONSTRAINT `fk_log_type_id` FOREIGN KEY (`log_type_id`) REFERENCES `t_log_types` (`id`),
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_users` (`id`);

--
-- Contraintes pour la table `t_posts`
--
ALTER TABLE `t_posts`
  ADD CONSTRAINT `fk_post_author` FOREIGN KEY (`author`) REFERENCES `t_users` (`id`);

--
-- Contraintes pour la table `t_users`
--
ALTER TABLE `t_users`
  ADD CONSTRAINT `fk_country` FOREIGN KEY (`country`) REFERENCES `t_countries` (`id`),
  ADD CONSTRAINT `fk_gender` FOREIGN KEY (`gender`) REFERENCES `t_genders` (`id`),
  ADD CONSTRAINT `fk_permissions` FOREIGN KEY (`permission`) REFERENCES `t_permissions` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
