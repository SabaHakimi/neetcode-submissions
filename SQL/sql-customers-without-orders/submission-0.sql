-- Write your query below
-- Write a query to find all customers who have never placed an order. 
-- Return the customer names. 
-- The result can be returned in any order.

SELECT customers.name
FROM customers
WHERE customers.id NOT IN (
    SELECT customers.id
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
);


-- get customers who HAVE placed an order
-- get all customers from customers not in this table