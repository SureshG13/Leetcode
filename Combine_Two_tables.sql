# link: https://leetcode.com/problems/combine-two-tables/
# Suresh G --> MYSQL

# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId;
