-- List the following details of each employee:
--         employee number, last name, first name, gender, and salary.

SELECT
    employees.emp_no,
    salaries.salary,
    employees.first_name,
    employees.last_name,
    employees.gender
FROM employees
JOIN salaries
ON salaries.emp_no = employees.emp_no;

-- List employees who were hired in 1986.

SELECT *
FROM employees
WHERE (YEAR FROM hire_date) = 1986;

-- List the manager of each department with the following information:
--      department number, department name, the manager's employee number,
--        last name, first name, and start and end employment dates.



-- List the department of each employee with the following information:
--      employee number, last name, first name, and department name.


-- List all employees whose first name is "Hercules"
--      and last names begin with "B."


-- List all employees in the Sales department,
--      including their employee number, last name,
--        first name, and department name.

-- In descending order, list the frequency count of employee
--      last names, i.e., how many employees share each last name.
