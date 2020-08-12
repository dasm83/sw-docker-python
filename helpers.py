import requests

def getCharacterPlanetInfo(name):
  r = requests.get('https://swapi.dev/api/people/?search='+name)
  if(r.json()['count'] == 0):
    return {'error':'notFound'}

  result = []

  for c in r.json()['results']:
    planetUrl = c['homeworld']

    r = requests.get(planetUrl)
    json = r.json()
    planet = json['name']
    population = json['population']
    climate = json['climate']

    result.append({'character':c['name'],'planetName':planet,'planetPopulation':population,'planetClimate':climate})

  return result
