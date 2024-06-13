### run ```pipenv install``` and then ```pipenv shell``` to enter into the virtual env.
### install click```pip install click``` and ```pip install SQLAlchemy```
#### To initialise the database you have to run ```python initialize_db.py```
#### To interact with the CLI you have to run ```python lib/cli.py``` to get the commands
- Adding a hymn you run ```python lib/cli.py create-hymn <number> <title> <lyrics> <author> <key>```
- Updating a hymn run ```python lib/cli.py update-hymn <num> --title <title> --lyrics <lyrics> ```
- Deleting a hymn ```python lib/cli.py delete-hymn <id>```
- Read all the hymns in the database ```python lib/cli.py list-hymns```
# Backend_Test
