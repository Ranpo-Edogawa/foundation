CREATE DATABASE data;
USE data;
CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    phone_number VARCHAR(50),
    hire_date DATE,
    job_id VARCHAR(50),
    salary DOUBLE,
    commission_pct DOUBLE,
    manager_id INT,
    department_id INT
    );

INSERT INTO (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id)
VALUES (100, 'John', 'Doe', 'XXXXXXXXXXXXXXXXXXXX', '000000000000', '2022-01-01', 'IT_PROG', 50000, NULL, NULL, 10);

SELECT first_name, salary, department_id from employee WHERE department_id = 40;
