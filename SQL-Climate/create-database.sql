
drop database if exists hawaii;
create database hawaii;

-- connect to newly initialized database
\connect hawaii postgres 

-- create tables
drop table if exists measurement;
create table measurement(
         id SERIAL PRIMARY KEY,
         station VARCHAR,
         date DATE,
         precip real,
         temp_obs real);
       
drop table if exists station;
create table station(
         station VARCHAR PRIMARY KEY,
         name VARCHAR,
         latitude real,
         longitude real,
         elevation real);

-- copy the contents of the provided csv files into the tables
\copy station from './Resources/hawaii_stations.csv' delimiter ',' csv header;
\copy measurement(station, date, precip, temp_obs) from './Resources/hawaii_measurements.csv' delimiter ',' csv header;


