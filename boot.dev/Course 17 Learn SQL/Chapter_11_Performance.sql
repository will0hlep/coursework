-- Lesson 1
CREATE INDEX email_idx ON users (email);

-- Lesson 5
CREATE INDEX user_id_recipient_id_idx
ON transactions (user_id, recipient_id);