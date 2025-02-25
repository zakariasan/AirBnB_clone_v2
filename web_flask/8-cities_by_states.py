#!/usr/bin/python3
""" Flask WebApp """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """ Close storage """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display cities by states """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
