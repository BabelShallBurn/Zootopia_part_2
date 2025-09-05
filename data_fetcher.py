import json
import requests


API_KEY = 'bsz8YhmcmFN8e0bBIGJKng==URW0m2WuWuMvmgEs'
URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary.
  """
  res = requests.get(url=URL, params={'name': 'Fox'}, headers={'X-API-Key': API_KEY})
    data = res.json()
    return data