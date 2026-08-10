-- lesson 1
SELECT * FROM users;

-- lesson 2
SELECT age FROM users;

-- lesson 3
SELECT age, name, balance FROM users;

-- lesson 6
SELECT id, name, is_admin FROM users;

-- lesson 9
CREATE TABLE users (id INTEGER, name TEXT, age INTEGER);
INSERT into users (id, name, age) values (1, 'John Doe', 21);
INSERT into users (id, name, age) values (2, 1, 33);
SELECT * FROM users;
