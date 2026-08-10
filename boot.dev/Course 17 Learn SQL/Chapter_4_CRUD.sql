-- Lesson 1
SELECT c,r,u,d FROM crud

-- Lesson 2
INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (2, 'Samantha', 29, 'BR', 'Sammy93', 'addingRecords!', false);

-- Lesson 5
INSERT INTO users(name, age, country_code, username, password, is_admin)
VALUES ('Lance', 20, 'US', 'LanChr', 'bootdevisbest', false);

INSERT INTO users(name, age, country_code, username, password, is_admin)
VALUES ('Tiffany', 28, 'US', 'Tifferoon', 'autoincrement', true);

-- Lesson 8
SELECT COUNT(*) FROM users;

-- Lesson 11
SELECT username FROM users WHERE is_admin;

-- Lesson 12
SELECT id, user_id, recipient_id, sender_id, amount FROM transactions WHERE sender_id IS NOT NULL;

-- Lesson 13
DELETE FROM users
    WHERE id = 2;

-- Lesson 16
UPDATE users
SET is_admin = TRUE
WHERE id = 9;

-- Lesson 20
SELECT COUNT(*) FROM users WHERE country_code = 'US';

-- Lesson 21
UPDATE users
SET country_code = 'US'
WHERE country_code = 'USA';