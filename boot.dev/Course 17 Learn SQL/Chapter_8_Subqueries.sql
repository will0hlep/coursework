-- Lesson 1
SELECT *
FROM transactions
WHERE user_id IN (
    SELECT id
    FROM users
    WHERE name = 'David'
);

-- Lesson 4
SELECT * FROM users
WHERE id IN (
  SELECT sender_id FROM transactions
  WHERE NOT is_admin AND (note LIKE '%invoice%' OR note LIKE '%tax%')
)

-- Lesson 5
SELECT * FROM users
WHERE age_in_days > 40 * 365;