"""Routes for weather section of the API."""
import flask
import requests
from flask_jwt_extended import jwt_required
from . import weather_bp
from config import Config


@weather_bp.route("/<city>", methods=["GET"])
@jwt_required
def get_weather_data(city):
    """Retrieves weather data from the open weather API."""
    url = (f"https://api.openweathermap.org/data/2.5/weather" +
           f"?q={city}&units=imperial&appid={Config.OW_API_KEY}")

    response = requests.get(url)
    
    return response.json()
