-- Tu código aquí 👇
SELECT * FROM usuarios;
SELECT * FROM categorias;
SELECT * FROM etiquetas limit 3;
SELECT * FROM posts limit 3;
SELECT * FROM posts_etiquetas limit 3;

create table comentarios(
  id integer not null,
  cuerpo_comentario VARCHAR(255) null,
  usuario_id integer null,
  post_id integer null,
  primary key (id),
  foreign key (usuario_id) references usuarios(id),
  foreign key (post_id) references posts(id)
);

insert into comentarios(id, cuerpo_comentario, usuario_id, post_id)
values (1, 'texto del comentario 1', 1, 43);

insert into comentarios(id, cuerpo_comentario, usuario_id, post_id)
values (2, 'texto del comentario 2', 1, 44);

insert into comentarios(id, cuerpo_comentario, usuario_id, post_id)
values (3, 'texto del comentario 3', 5, 45);

insert into comentarios(id, cuerpo_comentario, usuario_id, post_id)
values (4, 'texto del comentario 4', 3, 4);

insert into comentarios(id, cuerpo_comentario, usuario_id, post_id)
values (5, 'texto del comentario 5', 2, 5);

SELECT id, cuerpo_comentario, usuario_id, post_id
FROM comentarios;

/*
SELECT c.*
FROM comentarios as c 
INNER JOIN posts p 
ON c.post_id = p.id
WHERE c.usuario_id = 1;
*/

SELECT c.cuerpo_comentario AS comentario,
       u.login AS usuario,
       p.titulo AS post
FROM comentarios AS c INNER JOIN 
     posts AS p ON c.post_id = p.id INNER JOIN 
     usuarios AS u ON c.usuario_id = u.id
WHERE c.usuario_id = 1;
