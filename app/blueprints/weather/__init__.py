"""Initilize the weather data blueprint"""
import flask


weather_bp = flask.Blueprint("weather", __name__, url_prefix="/weather")

from . import routes
