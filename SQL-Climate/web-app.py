
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def notes_list():
    """
    List routes.
    """
    return []

@app.route('/api/v1.0/precipitation', methods=['GET'])
def precipitation():
    return []

@app.route('/api/v1.0/stations', methods=['GET'])
def stations():
    return []

@app.route('/api/v1.0/tobs', methods=['GET'])
def tempurature():
    return []

@app.route('/api/v1.0/<start>', methods=['GET'], strict_slashes=False)
@app.route('/api/v1.0/<start>/<end>', methods=['GET'], strict_slashes=False)
def range_summary(start, end=None):
    return []


if __name__ == "__main__":
    app.run(debug=True)
