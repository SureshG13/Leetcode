# Link: https://leetcode.com/problems/second-highest-salary/
# Suresh G --> MYSQL

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)
