first in ths folder create virtual envirement:
run in terminal: pipenv shell
if not working do (python -m pipenv shell)
to exit = exit

run:
pipenv install flask (remember to do it inside the shell)

ro install sfuff you need for flask run in you terminal:

pipenv install flask-sqlalchemy

pipenv install psycopg2 (if not working: pipenv install psycopg2-binary)

co create a DB in Your terminal:

python
from application import db
from  application.modules import FriendsCharacter
db.create_all()
after that you should be able to see your empty DB inside your Elephant SQL)

