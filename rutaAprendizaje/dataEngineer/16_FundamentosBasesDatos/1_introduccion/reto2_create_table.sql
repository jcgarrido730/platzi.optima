-- Inserta tu sentencia aqui-- Inserta tu sentencia aqui
create table people(
  person_id INTEGER AUTOINCREMENT not null, 
  last_name VARCHAR(255) null, 
  first_name VARCHAR(255) null, 
  address VARCHAR(255) null, 
  city VARCHAR(255) null,
  primary key (person_id));
  