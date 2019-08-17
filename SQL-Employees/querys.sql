-- List the following details of each employee:
--         employee number, last name, first name, gender, and salary.

SELECT
    employees.emp_no,
    salaries.salary,
    employees.first_name,
    employees.last_name,
    employees.gender
FROM
    employees,
    salaries
WHERE
    salaries.emp_no = employees.emp_no;

-- List employees who were hired in 1986.

SELECT
    *
FROM
    employees
WHERE
    EXTRACT (YEAR FROM hire_date) = 1986;

-- List the manager of each department with the following information:
--      department number, department name, the manager's employee number,
--        last name, first name, and start and end employment dates.

SELECT
    departments.dept_no,
    departments.dept_name,
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    dept_managers.from_date,
    dept_managers.to_date
FROM
    dept_managers,
    employees,
    departments
WHERE
    dept_managers.emp_no  = employees.emp_no
AND dept_managers.dept_no = departments.dept_no 
-- Restrict to only active managers
AND dept_managers.to_date >= Now();

-- List the department of each employee with the following information:
--      employee number, last name, first name, and department name.

SELECT
    departments.dept_name,
    employees.emp_no,
    employees.last_name,
    employees.first_name
FROM
    dept_employees,
    employees,
    departments 
WHERE
    dept_employees.emp_no  = employees.emp_no
AND dept_employees.dept_no = departments.dept_no
-- Restrict to only active department employees
AND dept_employees.to_date >=  Now();

-- List all employees whose first name is "Hercules"
--      and last names begin with "B."

SELECT
    *
FROM
    employees
WHERE
    employees.first_name = 'Hercules'
AND employees.last_name LIKE 'B%';


-- List all employees in the Sales department,
--      including their employee number, last name,
--        first name, and department name.

SELECT
    departments.dept_name,
    employees.emp_no,
    employees.last_name,
    employees.first_name
FROM
    dept_employees,
    employees,
    departments 
WHERE
    dept_employees.emp_no  = employees.emp_no
AND dept_employees.dept_no = departments.dept_no
-- Restrict to only employees
AND dept_employees.to_date >=  Now()
-- Restrict to only 'Sales' department
AND departments.dept_name = 'Sales';

-- In descending order, list the frequency count of employee last names, 
--      i.e., how many employees share each last name.

SELECT
    employees.last_name,
    COUNT(employees.emp_no)
FROM
    employees
GROUP BY
      employees.last_name;
