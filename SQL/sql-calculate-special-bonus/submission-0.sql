-- Write your query below
-- Write a query to calculate the bonus for each employee. 
-- An employee receives a bonus equal to 100% of their salary if:
    -- Their employee_id is an odd number, AND
    -- Their name does not start with the letter 'M'
-- Otherwise, the bonus is 0.
-- Return the employee_id and bonus for each employee, ordered by employee_id.

-- returning employee id and bonus
-- calc employee bonus is main issue
-- select all employee salary (* 2) where id and name match criteria

SELECT 
    employee_id,
    CASE
        WHEN employee_id % 2 = 1
        AND name NOT LIKE 'M%'
        THEN salary
        ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id ASC;
