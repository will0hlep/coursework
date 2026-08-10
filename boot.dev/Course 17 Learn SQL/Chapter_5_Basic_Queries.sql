-- Lesson 1
SELECT amount, note AS birthday_message 
FROM transactions
WHERE sender_id = 10;

-- Lesson 2
ALTER TABLE transactions
ADD COLUMN audit TEXT;

UPDATE transactions
SET audit = IIF(was_successful, 'No action required', 'Perform an audit');

SELECT * FROM transactions;

-- Lesson 3
SELECT name, age
FROM users
WHERE age BETWEEN 18 AND 30;

-- Lesson 4
SELECT DISTINCT country_code
    FROM users;

-- Lesson 5
SELECT *
    FROM users
    WHERE country_code = 'CA'
    AND age < 18;

-- Lesson 6
SELECT COUNT(*) as junior_count
    FROM users
    WHERE age < 18
    AND (country_code = 'CA'
    OR country_code = 'US');

-- Lesson 7
SELECT name, age, country_code
FROM users
WHERE country_code IN ('US', 'CA', 'MX');

-- Lesson 8
SELECT * FROM users
WHERE name LIKE 'Al%';

-- Lesson 9
SELECT * FROM users
WHERE name LIKE 'Al___';

-- Lesson 12
SELECT *, IIF(age > 55 OR country_code = 'CA', 10, 0) AS discount_percent
FROM users;