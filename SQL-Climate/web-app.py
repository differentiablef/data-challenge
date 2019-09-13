# ##############################################################################

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

import datetime as dt

# ##############################################################################

# setup flask app
app = FlaskAPI(__name__)

# setup engine for PostgreSQL 
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
    return {'end-points':
            ['/api/v1.0/precipitation',
             '/api/v1.0/stations',
             '/api/v1.0/tobs',
             '/api/v1.0/<start-date:MM-DD-YYYY>',
             '/api/v1.0/<start-date:MM-DD-YYYY>/<end-date:MM-DD-YYYY>']}

@app.route('/api/v1.0/precipitation', methods=['GET'])
def precipitation():
    end_date = session.query( Measurement.date).\
        order_by(desc(Measurement.date)).\
        limit(1).all()[0][0]
    begin_date = end_date - dt.timedelta(days=365)
    
    results = session.query( Measurement ).\
        filter( Measurement.date >= begin_date ).\
        filter( Measurement.date <= end_date ).\
        all()
    
    return dict([(entry.date, entry.precip) for entry in results])

@app.route('/api/v1.0/stations', methods=['GET'])
def stations():
    results = session.query( Station ).all()
    return  [ dict([ ( 'id', result.station ),
                     ( 'name', result.name ),
                     ( 'lat', result.latitude ),
                     ( 'lon', result.longitude ),
                     ( 'elev', result.elevation ) ]) \
                                  for result in results ]

@app.route('/api/v1.0/tobs', methods=['GET'])
def tempurature():
    end_date = session.query( Measurement.date).\
        order_by(desc(Measurement.date)).\
        limit(1).all()[0][0]
    begin_date = end_date - dt.timedelta(days=365)
    
    results = session.query( Measurement ).\
        filter( Measurement.date >= begin_date ).\
        filter( Measurement.date <= end_date ).\
        all()
    
    return dict([(entry.date, entry.precip) for entry in results])

@app.route('/api/v1.0/<start>', methods=['GET'], strict_slashes=False)
@app.route('/api/v1.0/<start>/<end>', methods=['GET'], strict_slashes=False)
def range_summary(start, end=None):

    try:
        begin_date = dt.datetime.strptime(start, "%m-%d-%Y")
    except:
        return "Invalid date format (start-date)"

    
    results = session.query(
        func.avg(Measurement.temp_obs),
        func.max(Measurement.temp_obs),
        func.min(Measurement.temp_obs)).\
        filter( begin_date <= Measurement.date )

    if end:
        try:
            end_date = dt.datetime.strptime(end, "%m-%d-%Y")
        except:
            return "Invalid date format (end-date)"
        
        results = results.filter( end_date >= Measurement.date )
        pass

    results = results.all()[0]
    
    return dict([
        ('mean', results[0]),
        ('max', results[1]),
        ('min', results[2])])

# ##############################################################################

if __name__ == "__main__":
    app.run(debug=True)
    pass
