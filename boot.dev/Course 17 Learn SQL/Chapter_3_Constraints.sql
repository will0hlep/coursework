-- lesson 1
SELECT * FROM transactions;

-- lesson 2
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL,
country_code TEXT NOT NULL,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
is_admin BOOLEAN);

-- lesson 3
INSERT INTO users (
  id,
  name,
  age,
  username,
  password,
  is_admin
) VALUES (
  1,
  'Rudolf',
  33,
  'rudolf1234',
  'thisisnotsecure',
  false
);

INSERT INTO users (
  id,
  name,
  age,
  username,
  password,
  is_admin
) VALUES (
  2,
  'Jerry',
  25,
  'jerrysmith',
  'mypasswordis1234',
  true
);

-- lesson 4
INSERT INTO users (
  id,
  name,
  country_code
) VALUES (
  1,
  'Jerry',
  'US'
);

INSERT INTO users (
  id,
  name,
  country_code
) VALUES (
  2,
  'Amit',
  'IN'
);

--lesson 5
CREATE TABLE transactions (
id INTEGER PRIMARY KEY,
sender_id INTEGER,
recipient_id INTEGER,
memo TEXT NOT NULL,
amount INTEGER UNIQUE NOT NULL,
balance INTEGER NOT NULL);