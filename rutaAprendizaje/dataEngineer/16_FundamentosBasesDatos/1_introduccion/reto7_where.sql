-- Escribe tu código aquí 👇
SELECT *
FROM COURSES
WHERE n_reviews >= 1;

SELECT *
FROM COURSES
WHERE n_reviews BETWEEN 1 AND 100;

SELECT *
FROM COURSES
WHERE name LIKE '%SQL%';
