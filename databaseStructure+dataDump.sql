-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mar. 09 fév. 2021 à 16:47
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
  `name` varchar(100) NOT NULL,
  `code` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `t_countries`
--

INSERT INTO `t_countries` (`id`, `name`, `code`) VALUES
(1, 'Afghanistan', 'AF'),
(2, 'Åland Islands', 'AX'),
(3, 'Albania', 'AL'),
(4, 'Algeria', 'DZ'),
(5, 'American Samoa', 'AS'),
(6, 'Andorra', 'AD'),
(7, 'Angola', 'AO'),
(8, 'Anguilla', 'AI'),
(9, 'Antarctica', 'AQ'),
(10, 'Antigua and Barbuda', 'AG'),
(11, 'Argentina', 'AR'),
(12, 'Armenia', 'AM'),
(13, 'Aruba', 'AW'),
(14, 'Australia', 'AU'),
(15, 'Austria', 'AT'),
(16, 'Azerbaijan', 'AZ'),
(17, 'Bahamas', 'BS'),
(18, 'Bahrain', 'BH'),
(19, 'Bangladesh', 'BD'),
(20, 'Barbados', 'BB'),
(21, 'Belarus', 'BY'),
(22, 'Belgium', 'BE'),
(23, 'Belize', 'BZ'),
(24, 'Benin', 'BJ'),
(25, 'Bermuda', 'BM'),
(26, 'Bhutan', 'BT'),
(27, 'Bosnia and Herzegovina', 'BA'),
(28, 'Botswana', 'BW'),
(29, 'Bouvet Island', 'BV'),
(30, 'Brazil', 'BR'),
(31, 'British Indian Ocean Territory', 'IO'),
(32, 'Brunei Darussalam', 'BN'),
(33, 'Bulgaria', 'BG'),
(34, 'Burkina Faso', 'BF'),
(35, 'Burundi', 'BI'),
(36, 'Cambodia', 'KH'),
(37, 'Cameroon', 'CM'),
(38, 'Canada', 'CA'),
(39, 'Cape Verde', 'CV'),
(40, 'Cayman Islands', 'KY'),
(41, 'Central African Republic', 'CF'),
(42, 'Chad', 'TD'),
(43, 'Chile', 'CL'),
(44, 'China', 'CN'),
(45, 'Christmas Island', 'CX'),
(46, 'Cocos (Keeling) Islands', 'CC'),
(47, 'Colombia', 'CO'),
(48, 'Comoros', 'KM'),
(49, 'Congo', 'CG'),
(50, 'Cook Islands', 'CK'),
(51, 'Costa Rica', 'CR'),
(52, 'Croatia', 'HR'),
(53, 'Cuba', 'CU'),
(54, 'CuraÃ§ao', 'CW'),
(55, 'Cyprus', 'CY'),
(56, 'Czech Republic', 'CZ'),
(57, 'Denmark', 'DK'),
(58, 'Djibouti', 'DJ'),
(59, 'Dominica', 'DM'),
(60, 'Dominican Republic', 'DO'),
(61, 'Ecuador', 'EC'),
(62, 'Egypt', 'EG'),
(63, 'El Salvador', 'SV'),
(64, 'Equatorial Guinea', 'GQ'),
(65, 'Eritrea', 'ER'),
(66, 'Estonia', 'EE'),
(67, 'Ethiopia', 'ET'),
(68, 'Falkland Islands (Malvinas)', 'FK'),
(69, 'Faroe Islands', 'FO'),
(70, 'Fiji', 'FJ'),
(71, 'Finland', 'FI'),
(72, 'France', 'FR'),
(73, 'French Guiana', 'GF'),
(74, 'French Polynesia', 'PF'),
(75, 'French Southern Territories', 'TF'),
(76, 'Gabon', 'GA'),
(77, 'Gambia', 'GM'),
(78, 'Georgia', 'GE'),
(79, 'Germany', 'DE'),
(80, 'Ghana', 'GH'),
(81, 'Gibraltar', 'GI'),
(82, 'Greece', 'GR'),
(83, 'Greenland', 'GL'),
(84, 'Grenada', 'GD'),
(85, 'Guadeloupe', 'GP'),
(86, 'Guam', 'GU'),
(87, 'Guatemala', 'GT'),
(88, 'Guernsey', 'GG'),
(89, 'Guinea', 'GN'),
(90, 'Guinea-Bissau', 'GW'),
(91, 'Guyana', 'GY'),
(92, 'Haiti', 'HT'),
(93, 'Heard Island and McDonald Islands', 'HM'),
(94, 'Holy See (Vatican City State)', 'VA'),
(95, 'Honduras', 'HN'),
(96, 'Hong Kong', 'HK'),
(97, 'Hungary', 'HU'),
(98, 'Iceland', 'IS'),
(99, 'India', 'IN'),
(100, 'Indonesia', 'ID'),
(101, 'Iraq', 'IQ'),
(102, 'Ireland', 'IE'),
(103, 'Isle of Man', 'IM'),
(104, 'Israel', 'IL'),
(105, 'Italy', 'IT'),
(106, 'Jamaica', 'JM'),
(107, 'Japan', 'JP'),
(108, 'Jersey', 'JE'),
(109, 'Jordan', 'JO'),
(110, 'Kazakhstan', 'KZ'),
(111, 'Kenya', 'KE'),
(112, 'Kiribati', 'KI'),
(113, 'Kuwait', 'KW'),
(114, 'Kyrgyzstan', 'KG'),
(115, 'Latvia', 'LV'),
(116, 'Lebanon', 'LB'),
(117, 'Lesotho', 'LS'),
(118, 'Liberia', 'LR'),
(119, 'Libya', 'LY'),
(120, 'Liechtenstein', 'LI'),
(121, 'Lithuania', 'LT'),
(122, 'Luxembourg', 'LU'),
(123, 'Macao', 'MO'),
(124, 'Madagascar', 'MG'),
(125, 'Malawi', 'MW'),
(126, 'Malaysia', 'MY'),
(127, 'Maldives', 'MV'),
(128, 'Mali', 'ML'),
(129, 'Malta', 'MT'),
(130, 'Marshall Islands', 'MH'),
(131, 'Martinique', 'MQ'),
(132, 'Mauritania', 'MR'),
(133, 'Mauritius', 'MU'),
(134, 'Mayotte', 'YT'),
(135, 'Mexico', 'MX'),
(136, 'Monaco', 'MC'),
(137, 'Mongolia', 'MN'),
(138, 'Montenegro', 'ME'),
(139, 'Montserrat', 'MS'),
(140, 'Morocco', 'MA'),
(141, 'Mozambique', 'MZ'),
(142, 'Myanmar', 'MM'),
(143, 'Namibia', 'NA'),
(144, 'Nauru', 'NR'),
(145, 'Nepal', 'NP'),
(146, 'Netherlands', 'NL'),
(147, 'New Caledonia', 'NC'),
(148, 'New Zealand', 'NZ'),
(149, 'Nicaragua', 'NI'),
(150, 'Niger', 'NE'),
(151, 'Nigeria', 'NG'),
(152, 'Niue', 'NU'),
(153, 'Norfolk Island', 'NF'),
(154, 'Northern Mariana Islands', 'MP'),
(155, 'Norway', 'NO'),
(156, 'Oman', 'OM'),
(157, 'Pakistan', 'PK'),
(158, 'Palau', 'PW'),
(159, 'Panama', 'PA'),
(160, 'Papua New Guinea', 'PG'),
(161, 'Paraguay', 'PY'),
(162, 'Peru', 'PE'),
(163, 'Philippines', 'PH'),
(164, 'Pitcairn', 'PN'),
(165, 'Poland', 'PL'),
(166, 'Portugal', 'PT'),
(167, 'Puerto Rico', 'PR'),
(168, 'Qatar', 'QA'),
(169, 'RÃ©union', 'RE'),
(170, 'Romania', 'RO'),
(171, 'Russian Federation', 'RU'),
(172, 'Rwanda', 'RW'),
(173, 'Saint BarthÃ©lemy', 'BL'),
(174, 'Saint Kitts and Nevis', 'KN'),
(175, 'Saint Lucia', 'LC'),
(176, 'Saint Martin (French part)', 'MF'),
(177, 'Saint Pierre and Miquelon', 'PM'),
(178, 'Saint Vincent and the Grenadines', 'VC'),
(179, 'Samoa', 'WS'),
(180, 'San Marino', 'SM'),
(181, 'Sao Tome and Principe', 'ST'),
(182, 'Saudi Arabia', 'SA'),
(183, 'Senegal', 'SN'),
(184, 'Serbia', 'RS'),
(185, 'Seychelles', 'SC'),
(186, 'Sierra Leone', 'SL'),
(187, 'Singapore', 'SG'),
(188, 'Sint Maarten (Dutch part)', 'SX'),
(189, 'Slovakia', 'SK'),
(190, 'Slovenia', 'SI'),
(191, 'Solomon Islands', 'SB'),
(192, 'Somalia', 'SO'),
(193, 'South Africa', 'ZA'),
(194, 'South Georgia and the South Sandwich Islands', 'GS'),
(195, 'South Sudan', 'SS'),
(196, 'Spain', 'ES'),
(197, 'Sri Lanka', 'LK'),
(198, 'Sudan', 'SD'),
(199, 'Suriname', 'SR'),
(200, 'Svalbard and Jan Mayen', 'SJ'),
(201, 'Swaziland', 'SZ'),
(202, 'Sweden', 'SE'),
(203, 'Switzerland', 'CH'),
(204, 'Syrian Arab Republic', 'SY'),
(205, 'Tajikistan', 'TJ'),
(206, 'Thailand', 'TH'),
(207, 'Timor-Leste', 'TL'),
(208, 'Togo', 'TG'),
(209, 'Tokelau', 'TK'),
(210, 'Tonga', 'TO'),
(211, 'Trinidad and Tobago', 'TT'),
(212, 'Tunisia', 'TN'),
(213, 'Turkey', 'TR'),
(214, 'Turkmenistan', 'TM'),
(215, 'Turks and Caicos Islands', 'TC'),
(216, 'Tuvalu', 'TV'),
(217, 'Uganda', 'UG'),
(218, 'Ukraine', 'UA'),
(219, 'United Arab Emirates', 'AE'),
(220, 'United Kingdom', 'GB'),
(221, 'United States', 'US'),
(222, 'United States Minor Outlying Islands', 'UM'),
(223, 'Uruguay', 'UY'),
(224, 'Uzbekistan', 'UZ'),
(225, 'Vanuatu', 'VU'),
(226, 'Viet Nam', 'VN'),
(227, 'Wallis and Futuna', 'WF'),
(228, 'Western Sahara', 'EH'),
(229, 'Yemen', 'YE'),
(230, 'Zambia', 'ZM'),
(231, 'Zimbabwe', 'ZW');

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
-- Structure de la table `t_users`
--

CREATE TABLE `t_users` (
  `id` int(11) NOT NULL,
  `permission` varchar(10) NOT NULL COMMENT 'les permissions de l''utilisateur',
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
(1, 'user', 'Jack', 'OWheel', 'a@a.com', 3, 203, 'Jack', '$5$rounds=535000$gLv.Lg.8yYKzaAO.$riI9GpNzVTU0hHYUNUhOiI4hsc8Ri8dlfBwssOQPHkA', 'no_reset', 'Default_value', 'da53c3ef06c08423.jpg', '2021-02-09 15:05:23'),
(2, 'admin', 'Jack', 'JAck', 'admin@admin.com', 3, 116, 'Jack2', '$5$rounds=535000$gZeC8FZPy7Q.n5Bu$A6PzPHapp3.5WJgRueYz.SPVGYTkKK5gC7qkOhxiND0', 'no_reset', 'Default_value', 'admin.png', '2021-02-09 16:43:56');

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
-- Index pour la table `t_users`
--
ALTER TABLE `t_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email unique` (`email`),
  ADD UNIQUE KEY `username unique` (`username`),
  ADD KEY `fk_country` (`country`),
  ADD KEY `fk_gender` (`gender`);

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
-- AUTO_INCREMENT pour la table `t_users`
--
ALTER TABLE `t_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `t_users`
--
ALTER TABLE `t_users`
  ADD CONSTRAINT `fk_country` FOREIGN KEY (`country`) REFERENCES `t_countries` (`id`),
  ADD CONSTRAINT `fk_gender` FOREIGN KEY (`gender`) REFERENCES `t_genders` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
