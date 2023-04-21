# Conceptos 

* Data WareHouse: Almacen de datos
* Data Mart: Áreas del Almacen (finanzas, ventas, recursos humanos)
* Dimensión: Análisis de una métrica o la información desde distintas perspectivas
* Hechos: Es la información cuantitativa de un proceso de negocio. Se denominan Medidas o Métricas
* Data Lake: Arquitecturas utilizadas para almacenar grandes cantidades de datos desestructurados y semiestructurados que se recopilan en los distintos sistemas, dispositivos y aplicaciones de la empresa
* Data LakeHouse: Arquitectura abierta de gestión de datos que combina las ventajas de flexibilidad y escalabilidad de un lago de datos con las estructuras y características de gestión de datos de un almacén de datos

---
## Tipos de analítica
* Analítica Descriptiva: Examina datos históricos para entender eventos pasados y su impacto en el negocio
* Analítica Diagnóstica: Investiga las causas de eventos específicos, identificando patrones y relaciones
* Analítica Predictiva: Utiliza modelos estadísticos y algoritmos para prever futuros eventos y tendencias
* Analítica Prescriptiva: Proporciona recomendaciones basadas en análisis previos para optimizar decisiones y acciones futuras

La Analítica Descriptiva y Diagnóstica se ajustan más a Business Intelligence, ya que se enfocan en el análisis de datos históricos y en comprender eventos y causas en el negocio.

---
## Jerarquía del conocimiento
### Pirámide D-I-K-W
### Datos-Información-Conocimiento-Sabiduría

- 4. Sabiduría: Evaluación e internalización del conocimiento
- 3. Conocimiento: Aplicación mental de los datos y la información
- 2. Información: Datos procesados para ser útiles 
- 1. Datos: Elementos discontinuos que representan hechos 

---
## Atributos 
### Jerárquicos
Permiten ir de lo general a lo particular.
Consolidar y desagregar. Por ej: país.

### Descriptivos
Información relevante. Netamente
descriptiva. Por ej: dirección, teléfono, talla,
clima.

### De control
Datos de auditoría. 
No pertenecen al conocimiento del negocio. Por ej: fecha de carga.

---
## OLTP
Procesamiento de Transacciones En Línea
Sistema transaccional / operacional

## OLAP
Procesamiento Analítico En Línea
Sistema de bodega de datos (DWH)

---
## Tipos de dimensiones
### Tipo 1
Sobreescribir el atributo actualizado.
Se tienen atributos de fecha_carga y fecha_actualizacion, (atributo opcional usuario)
### Tipo 2
Agrega un nuevo registro con el cambio.
Se crean 2 atributos fecha para indicar la vigencia del registo: fecha_inicio, fecha_final
### Tipo 3
Se tiene el atributo de fecha_carga
Se agrega un nuevo atributo "valor_anterior".

---
### Reglas de negocio
Lo que el negocio nos sugiere para realizar transformación de nuestros datos.
¿Qué es lo que espera el negocio? Que los datos cumplan para poder tomar decisiones?
  