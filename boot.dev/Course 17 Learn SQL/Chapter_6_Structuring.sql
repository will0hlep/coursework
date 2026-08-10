-- Lesson 1
SELECT * FROM transactions
    WHERE note LIKE '%lunch%'
    LIMIT 5;

-- Lesson 4
SELECT * FROM transactions
WHERE amount BETWEEN 10 AND 80
ORDER BY amount DESC;

-- Lesson 7
SELECT * FROM transactions
WHERE amount BETWEEN 10 AND 80
ORDER BY amount DESC
LIMIT 4;

-- Lesson 8
SELECT name, username FROM users
WHERE password in ('backendDev', 'welovebootdev', 'SQLrocks')
ORDER BY name;