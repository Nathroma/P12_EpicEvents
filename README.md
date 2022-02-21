
#  EpicEvents

L'application permet de gérer les clients potentiels d'une entreprise ainsi que les contrats et évènements lié à ceux-ci

Se référer à la documentation Postman du projet disponible [en cliquant ici](https://documenter.getpostman.com/view/17390561/UVkmQGnt).

## Installation

- Télécharger l'application via GitHub
```bash
git clone 
```

- Créer un environnement virtuel et l'activer :
```cmd
python -m venv env
env\Scripts\activate
```
(Sous windows)

- Une fois dans l'environnment virtuel faites :
```cmd
pip install -r requirements.txt
```
pour installer les modules

- Puis faites les migrations :
```cmd
softdesk\manage.py makemigrations
softdesk\manage.py migrate
```

### Pour lancer le serveur Django:
```cmd
softdesk\manage.py runserver
```
en cas de problème se referer à la documentation [Django](https://www.djangoproject.com/)

### L'accès Admin
- Pour accéder à l'interface administrateur rendez-vous à l'adresse suivante: http://localhost:8000/admin/
- Les administrateurs ont tous les accès sur l'API

### L'accès utilisateur
Pour avoir accès au points de terminaison en tant qu'utilisateur
vous devez vous connectez avec un compte utilisateur précedemment crée via l'interface admin

Pour utiliser les points de terminaisons, utilisez [Postman](https://www.postman.com/).