# Blog avec Flask !
## J'utilise mon [CRUD](https://github.com/jubnl/python_CRUD).

## Configuration :
Ouvrez [databaseStructure+dataDump.sql](databaseStructure+dataDump.sql) et copiez l'intégralité du fichier.

Ouvrez Xampp ou Wamp ou Uwamp (enfin vous avez compris) et lancez votre serveur SQL et votre serveur Apache. Rendez vous sur PhpMyAdmin et collez le fichier précédemment copié de manière à executer le SQL.

Ouvrez [db_config.json](config/db_config.json) et assurez vous des paramètres de connexion à la base de donnée.

Assurez vous d'avoir installé python 3.6+ et executez [launch.bat](launch.bat). Les librairies nécessaires s'installeront.

Une fois que le serveur pour le site est en place puis rendez-vous à l'adresse suivante : http://localhost:5000

Enjoy !

Veuillez ouvrir une issue en cas de problème !

Il y a un compte admin existant de base :
email : exemple@exemple.com
password : Exemple123$

## Petite précision

Pour le moment il n'y a que la partie création de compte, login et logout, compte et update de compte qui sont fonctionnels. Des nouvelles fonctionnalités seront disponible d'ici peu.
