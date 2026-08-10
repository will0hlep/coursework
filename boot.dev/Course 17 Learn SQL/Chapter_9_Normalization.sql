-- Lesson 3
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

CREATE TABLE countries (
  id INTEGER PRIMARY KEY,
  country_code TEXT,
  name TEXT,
  user_id INTEGER,
  CONSTRAINT fk_users
  FOREIGN KEY (user_id)
  REFERENCES users(id)
);

-- Lesson 10
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

CREATE TABLE countries (
  id INTEGER PRIMARY KEY,
  country_code TEXT,
  name TEXT
);

CREATE TABLE users_countries (
  user_id INTEGER,
  country_id INTEGER,
  UNIQUE(user_id, country_id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (country_id) REFERENCES countries (id)
);

-- Lesson 11
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);

CREATE TABLE companies (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  num_employees INTEGER NOT NULL,
  revenue INTEGER
);

CREATE TABLE users_companies (
  user_id INTEGER,
  company_id INTEGER,
  UNIQUE(user_id, company_id)
);

-- Lesson 12
CREATE TABLE companies (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  num_employees INTEGER NOT NULL
);

-- Don't touch between these comments --

INSERT INTO companies(name, num_employees)
  VALUES ('Pfizer', 10000);
INSERT INTO companies(name, num_employees)
  VALUES ('WorldBanc', 80);
INSERT INTO companies(name, num_employees)
  VALUES ('Fantasy Quest', 30);
INSERT INTO companies(name, num_employees)
  VALUES ('Walmart', 1000);

-- Don't touch between these comments --

SELECT *, IIF(100 < num_employees, 'large', 'small') AS size
  FROM companies;

-- Lesson 13
--CREATE TABLE users (
--  id INTEGER PRIMARY KEY,
--  name TEXT NOT NULL,
--  age INTEGER NOT NULL,
--  username TEXT UNIQUE NOT NULL,
--  password TEXT NOT NULL,
--  is_admin BOOLEAN
--);

CREATE TABLE banks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  routing_number INTEGER
);

CREATE TABLE users_banks (
  user_id INTEGER,
  bank_id INTEGER,
  UNIQUE(user_id, bank_id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (bank_id) REFERENCES banks (id)
);