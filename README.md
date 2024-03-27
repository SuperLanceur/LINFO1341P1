# Ce fichier reprend le contenu de chaque trace

idle : Pas d'interaction avec le logiciel pendant un moment. Ces communications sont périodiques.

startup/new_startup : Démarrage de l'application de bureau, en étant connecté au préalable

open_tray/tray_clean : Ouverture de l'application minimisée (tray)

relogin : Reconnexion partielle au serveur depuis l'application de bureau (déconnexion/reconnexion)

relogin_full (todo) : Reconnexion complète au serveur (suppression des données locales)

shutdown : Fermeture brutale de l'application

single_sync/triple_sync : Appui unique/triple sur le bouton de synchronisation (le contenu sur le serveur n'a pas changé)

# Filtres 
Le fichier filter.txt contient les différents filtres utilisés. Pour le moment, seul des filtres TCP sont appliqués, en fonction des ports utilisés par l'application, obtenus via la commande `netstat -a -b`

Ces filtres ont été appliqués sur les traces originales, et le résultat obtenu peut être consulté dans le dossier `stripped`