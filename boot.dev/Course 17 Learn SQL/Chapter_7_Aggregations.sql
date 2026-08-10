-- Lesson 1
SELECT COUNT(*) FROM transactions
WHERE user_id = 6 AND was_successful;

-- Lesson 2
SELECT SUM(amount)
FROM transactions
WHERE user_id = 9 and was_successful;

-- Lesson 3
SELECT MAX(age) as age
FROM users
WHERE is_admin;

-- Lesson 4
SELECT MIN(age) as age
FROM users
WHERE country_code = 'US';

-- Lesson 5
SELECT user_id, SUM(amount) as balance
FROM transactions
WHERE was_successful
GROUP BY user_id;

-- Lesson 6
SELECT AVG(age)
FROM users
WHERE country_code = 'US';

-- Lesson 7
SELECT sender_id, SUM(amount) as balance
FROM transactions
WHERE sender_id IS NOT NULL AND was_successful AND note LIKE '%lunch%'
GROUP BY sender_id
HAVING balance > 20
ORDER BY balance;

-- Lesson 10
SELECT ROUND(AVG(age)) as round_age
FROM users
WHERE country_code = 'US';

-- Lesson 11
SELECT country_code, ROUND(AVG(age)) as average_age
FROM users
GROUP BY country_code;