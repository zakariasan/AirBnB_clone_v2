#!/usr/bin/python3
""" Flask WebApp """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """ Close storage """
    storage.close()


@app.route('/states/', strict_slashes=False)
def display_states():
    """ Display states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def display_cities(state_id):
    """ Display cities of a state """
    states = storage.all(State)
    if state_id in states:
        state = states[state_id]
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
