-- Lesson 1
SELECT *
FROM users
INNER JOIN countries
ON users.country_code = countries.country_code;

-- Lesson 2
SELECT users.name, users.age, countries.name as country_name
FROM users
INNER JOIN countries
ON countries.country_code = users.country_code
ORDER BY country_name;

-- Lesson 3
SELECT users.name as name, SUM(transactions.amount) as sum, COUNT(transactions.amount) as count
FROM users
LEFT JOIN transactions
ON users.id = transactions.user_id
GROUP BY users.id
ORDER BY sum DESC;

-- Lesson 9
SELECT users.id, users.name, users.age, users.username, countries.name as country_name, sum(transactions.amount) as balance
FROM users
LEFT JOIN transactions
ON users.id = transactions.user_id
AND users.id = 6
AND transactions.was_successful
LEFT JOIN countries
ON countries.country_code = users.country_code;

-- Lesson 10
SELECT users.name, users.username, COUNT(*) as support_ticket_count
FROM users
INNER JOIN support_tickets
ON users.id = support_tickets.user_id
AND NOT issue_type LIKE "Account Access"
GROUP BY users.id
HAVING support_ticket_count > 1
ORDER BY support_ticket_count DESC;