
-- Drop database and create an empty one

DROP DATABASE IF EXISTS employee_db;
CREATE DATABASE employee_db;

-- Have the psql client connect to the newly created database
--   (password stored in PGPASSWORD enviornment variable)

\connect employee_db postgres localhost;

-- Create the departments table and
--    copy the contents of the provided csv files into the table
 

CREATE TABLE departments
(
       dept_no VARCHAR(5) PRIMARY KEY,
       dept_name VARCHAR
);

-- Note: the following is using psql's client-side version of COPY because
--           the postgresql server complains when using the server-side version

\COPY departments FROM './data/departments.csv' DELIMITER ',' QUOTE '"' CSV HEADER;

-- Create the department employees table and
--    copy the contents of the provided csv files into the table

CREATE TABLE dept_employees
(
       emp_no INT,
       dept_no VARCHAR(5),
       from_date DATE,
       to_date DATE
);

\COPY dept_employees FROM './data/dept_emp.csv' DELIMITER ',' QUOTE '"' CSV HEADER;

-- Create department managers table and
--    copy the contents of the provided csv files into the table

CREATE TABLE dept_managers
(
       dept_no VARCHAR(5),
       emp_no INT,
       from_date DATE,
       to_date DATE
);

\COPY dept_managers FROM './data/dept_manager.csv' DELIMITER ',' QUOTE '"' CSV HEADER;

-- Create employee table and
--    copy the contents of the provided csv files into the table

CREATE TABLE employees
(
       emp_no INT PRIMARY KEY,
       birth_date DATE,
       first_name VARCHAR,
       last_name VARCHAR,
       gender VARCHAR(1),
       hire_date DATE
);

\COPY employees FROM './data/employees.csv' DELIMITER ',' QUOTE '"' CSV HEADER;

-- Create salaries table and
--    copy the contents of the provided csv files into the table

CREATE TABLE salaries
(
      emp_no INT,
      salary DECIMAL,
      from_date DATE,
      to_date DATE
);

\COPY salaries FROM './data/salaries.csv' DELIMITER ',' QUOTE '"' CSV HEADER;

-- Create titles table and
--    copy the contents of the provided csv files into the table

CREATE TABLE titles
(
       emp_no INT,
       title VARCHAR,
       from_date DATE,
       to_date DATE
);

\COPY titles FROM './data/titles.csv' DELIMITER ',' QUOTE '"' CSV HEADER;


-- Output from `head -n2 data/*.csv` 
-- ==> data/departments.csv <==
-- "dept_no","dept_name"
-- "d001","Marketing"
-- 
-- ==> data/dept_emp.csv <==
-- "emp_no","dept_no","from_date","to_date"
-- 10001,"d005","1986-06-26","9999-01-01"
-- 
-- ==> data/dept_manager.csv <==
-- "dept_no","emp_no","from_date","to_date"
-- "d001",110022,"1985-01-01","1991-10-01"
-- 
-- ==> data/employees.csv <==
-- "emp_no","birth_date","first_name","last_name","gender","hire_date"
-- 10001,"1953-09-02","Georgi","Facello","M","1986-06-26"
-- 
-- ==> data/salaries.csv <==
-- emp_no,salary,from_date,to_date
-- 10001,60117,1986-06-26,1987-06-26
-- 
-- ==> data/titles.csv <=
-- "emp_no","title","from_date","to_date"
-- 10001,"Senior Engineer","1986-06-26","9999-01-01"
-- 
