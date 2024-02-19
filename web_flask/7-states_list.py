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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display states list """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
