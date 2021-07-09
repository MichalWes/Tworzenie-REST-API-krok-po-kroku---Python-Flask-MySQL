from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

authors_bp = Flask(__name__)
authors_bp.config.from_object(Config)

db = SQLAlchemy(authors_bp)
migrate = Migrate(authors_bp, db)

from book_library_app import authors
from book_library_app import models
from book_library_app import db_manage_commands
from book_library_app import errors