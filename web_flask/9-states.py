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
@app.route('/states/<id>', strict_slashes=False)
def display_states_and_cities(id=None):
    """ Display states and cities """
    states = storage.all(State)

    if not id:
        state_names = {state.id: state.name for state in states.values()}
        return render_template('7-states_list.html', Table="States",
                               items=state_names)

    state_key = "State." + id
    if state_key in states:
        state = states[state_key]
        return render_template('9-states.html', Table=f"State: {state.name}",
                               items=state)

    return render_template('9-states.html', items=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
