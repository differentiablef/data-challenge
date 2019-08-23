# ##############################################################################

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

# ##############################################################################

app = FlaskAPI(__name__)

# setup engine for postgresql 
engine = create_engine("postgresql://postgres@localhost/hawaii")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
conn = engine.connect()

# ##############################################################################

@app.route("/", methods=['GET'])
def notes_list():
    """
    List routes.
    """
    return {'end-points':['/api/v1.0/precipitation',
                          '/api/v1.0/stations',
                          '/api/v1.0/tobs',
                          '/api/v1.0/<start-date>',
                          '/api/v1.0/<start-date>/<end-date>']}

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

# ##############################################################################

if __name__ == "__main__":
    app.run(debug=True)
    pass
