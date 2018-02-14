from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import application, db

migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('migrate', MigrateCommand)

if __name__ == '__main__':
    manager.run()
