
"""
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
"""
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db


app.config.from_objects(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()