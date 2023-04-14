## Conectarse a docker (base de datos local)

```sh
docker-compose exec mongodb bash
```

## Conexion con mongosh
```sh
mongosh "mongodb://root:root123@localhost:27017/?authMechanism=DEFAULT&tls=false"
```
## consultar bases de datos y colecciones
```sh
show dbs
show collections
```

## consultar documentos
```sh
use tienda_platzi
db.productos.find()
```

```sh
use("platzi_store")
db.products.find()
exit
```

## Conectarse a Mongo Atlas
```sh
mongosh "mongodb+srv://jcgarrido:09Abril**2023@mongodb101.d7tc4zk.mongodb.net/test"
use sample_training
db.zips.find({state:'NY'})
db.zips.find({state:'NY'}).count()
exit 
```
