Django Inventory written by Jamie Hamilton

A backup of the databse is in dbackups, and you can use dbrestore to restore it. The database used in restores and backups is dependent on the settings inventorysystem/settings.py. 
Do no attempt to run the emergency/clearmigrations script/command unless the migrations are screwed up. In which case you should consider restoring your backup instead. To initialize an empty database so Django can use it and start fresh migrations:

./manage.py makemigrations
./manage.py migrate -run-syncdb
./manage.py 0.0.0.0:8000   - or whatever port.

From there you can restore the latest prod copy of the database (or dev copy, whichever is known to match your tree) so you can have data to work with.


