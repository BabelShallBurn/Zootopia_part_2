import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    res = requests.get(url=URL, params={'name': animal_name}, headers={'X-API-Key': API_KEY})
    data = res.json()
    return data