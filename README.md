# CollectionCatalogue
The term project for COMP 4721 (Software Design):  A collection catalogue web application built using the Django framework.

In order to run the server, Django must be installed using pip.  In addition, the data base needs to be set up using the following steps:

1. Delete db.sqlite3 in the root directory
2. Delete 0001_initial.py in the migrations folder
3. Run the following commands from the root directory:

python manage.py makemigrations
python manage.py sqlmigrate Catalogue 0001 
python manage.py migrate

The server can then be run with the command:

python manage.py runserver

It can then be accessed from localhost:8000 in any web-browser.
