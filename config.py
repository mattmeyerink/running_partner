"""Contains configuration settings for the running app."""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, ".env"))

class Config:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")

    SECRET_KEY = os.getenv("SECRET_KEY")

    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    DB_ENDPOINT = os.getenv("DB_ENDPOINT")
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@" +
                              f"{DB_ENDPOINT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
