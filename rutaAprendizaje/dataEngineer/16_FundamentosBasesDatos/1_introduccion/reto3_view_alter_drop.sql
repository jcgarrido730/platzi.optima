CREATE OR REPLACE VIEW people AS
SELECT * FROM people;

ALTER TABLE people
ADD COLUMN date_of_birth DATE NULL;

ALTER TABLE people
ADD COLUMN date_of_birth DATE NULL AFTER city;

ALTER TABLE people 
DROP COLUMN date_of_birth;

ALTER TABLE people
DROP COLUMN address;

DROP TABLE people;
DROP DATABASE nombre_baseDatos;

-- Escribe aquí tu código SQL 👇
CREATE VIEW v_madrid_customers AS
SELECT person_id, last_name, first_name
FROM people 
WHERE city='Madrid';

SELECT * FROM v_madrid_customers;

ALTER TABLE people
ADD COLUMN date_of_birth DATE NULL;

ALTER TABLE people
DROP COLUMN address;