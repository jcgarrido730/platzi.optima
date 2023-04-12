-- Escribe aquí tu código SQL 👇
SELECT name FROM courses;
SELECT name teachers;

SELECT courses.id AS id,
       courses.name AS name,
       courses.teacher_id AS teacher_id,
       teachers.name AS teacher_name
FROM courses 
LEFT JOIN teachers 
ON teachers.course_id = courses.id
WHERE courses.teacher_id IS NOT NULL;