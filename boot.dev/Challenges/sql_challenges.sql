--challenge 1
SELECT title AS post_title, author_username AS author, word_count
FROM posts
WHERE status = 'draft'
  AND word_count >= 200
  AND LENGTH(title) >= 12;

--challenge 2
SELECT books.title as book_title, authors.name as author_name, COUNT(reviews.id) as review_count
FROM books
LEFT JOIN authors
ON books.author_id = authors.id
LEFT JOIN reviews
ON books.id = reviews.book_id
GROUP BY books.id
ORDER BY review_count DESC, book_title