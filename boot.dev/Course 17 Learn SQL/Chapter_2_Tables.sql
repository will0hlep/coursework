-- lesson 1
CREATE TABLE people (id INTEGER, tag TEXT, name TEXT, age INTEGER, balance INTEGER, is_admin BOOLEAN);

-- lesson 2
CREATE TABLE transactions (id INTEGER, recipient_id INTEGER, sender_id INTEGER, note TEXT, amount INTEGER);

-- lesson 3
ALTER TABLE people
RENAME TO users;

ALTER TABLE users
RENAME COLUMN tag TO username;

ALTER TABLE users
ADD COLUMN password TEXT;

-- lesson 5
ALTER TABLE transactions
ADD COLUMN was_successful BOOLEAN;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT;

-- lesson 6
ALTER TABLE transactions
DROP COLUMN was_successful;

ALTER TABLE transactions
DROP COLUMN transaction_type;

-- lesson 12
CREATE TABLE posts (id INTEGER, image_url TEXT, description TEXT, author_id INTEGER, is_sponsored BOOLEAN);

-- lesson 13
ALTER TABLE posts
RENAME COLUMN author_id TO poster_id;

ALTER TABLE posts
ADD COLUMN is_edited BOOLEAN;

ALTER TABLE posts
DROP COLUMN is_sponsored;