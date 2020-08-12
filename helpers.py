import requests

def getCharacterPlanetInfo(name):
  characterResponse = requests.get('https://swapi.dev/api/people/?search='+name).json()
  if(characterResponse['count'] == 0):
    return {'error':'notFound'}

  result = []

  for character in characterResponse['results']:
    planetUrl = character['homeworld']

    planetInfo = getPlanetInfoOnUrl(planetUrl)

    result.append({'character':character['name'],'planetName':planetInfo['name'],'planetPopulation':planetInfo['population'],'planetClimate':planetInfo['climate']})

  return result

def getPlanetInfoOnUrl(url):
  planetResponse = requests.get(url).json()

  planet = planetResponse['name']
  population = planetResponse['population']
  climate = planetResponse['climate']

  return {'name':planet,'population':population,'climate':climate}
