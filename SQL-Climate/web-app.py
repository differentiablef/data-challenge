
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def notes_list():
    """
    List routes.
    """
    return ['node-list']

@app.route('/api/v1.0/precipitation', methods=['GET'])
def precipitation():
    return ['precip']

@app.route('/api/v1.0/stations', methods=['GET'])
def stations():
    return ['stations']

@app.route('/api/v1.0/tobs', methods=['GET'])
def tempurature():
    return ['temp_obs']

@app.route('/api/v1.0/<start>', methods=['GET'], strict_slashes=False)
@app.route('/api/v1.0/<start>/<end>', methods=['GET'], strict_slashes=False)
def range_summary(start, end=None):
    return ['range_summary']

if __name__ == "__main__":
    app.run(debug=True)
    pass
