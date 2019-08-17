  drop table if exists measurement;
  create table measurement(
         id SERIAL PRIMARY KEY,
         station VARCHAR,
         date DATE,
         precip DECIMAL,
         temp_obs DECIMAL);
       
  drop table if exists station;
  create table station(
         station VARCHAR PRIMARY KEY,
         name VARCHAR,
         latitude DECIMAL,
         longitude DECIMAL,
         elevation DECIMAL);

