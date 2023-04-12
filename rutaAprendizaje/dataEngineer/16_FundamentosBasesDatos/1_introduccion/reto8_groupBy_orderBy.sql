-- Escribe tu código aquí 👇
SELECT *
FROM courses;

SELECT *
FROM teachers; 

SELECT teachers.name AS teacher,
       SUM(n_reviews) AS total_reviews 
FROM courses 
INNER JOIN teachers 
ON courses.teacher_id = teachers.id
GROUP BY teachers.name
ORDER BY total_reviews DESC;
