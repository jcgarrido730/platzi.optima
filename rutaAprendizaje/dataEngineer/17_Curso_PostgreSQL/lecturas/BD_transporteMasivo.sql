postgres=# CREATE DATABASE transporte_masivo;

postgres=# \c transporte_masivo

transporte_masivo=# CREATE TABLE viajero (
  id_viajero SERIAL,
  nombre VARCHAR,
  fecha_registro DATE,
  CONSTRAINT pk_pasajero PRIMARY KEY (id_viajero)
);

transporte_masivo=# CREATE INDEX idx_pasajero_fechacreacion ON viajero (fecha_registro);
