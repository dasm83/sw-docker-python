from flask import Flask,jsonify
import helpers

app = Flask(__name__)

@app.route('/character/<name>/', methods=['GET', 'POST'])
def getCharacterPlanet(name):
  info = helpers.getCharacterPlanetInfo(name)
  return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
