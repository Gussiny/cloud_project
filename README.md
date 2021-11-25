# Proyecto de Cloud

El proyecto consta de una aplicación hecha en Flask con Python en donde se busca ayudar a calcular el área y el volumen de diferentes figuras geometricas de tres dimensiones, en este caso serían: `cilindro`, `cubo`, `esfera`, `cono`, `prisma rectangular`. 

Una vez que son calculados se muestran dentro de la misma página de la app y a su vez los resultados son almacenados en tiempo real en una base de datos de Firestore donde se podrán consultar los mismos como si fuera un historial.

##### Link al Video:
https://drive.google.com/file/d/1qANCR8jGoJ3ysm_3q5jr3XIiuwPvqjhu/view?usp=sharing

----
# Instrucciones
## Dockerizar proyecto

#### Crear el build:
`docker build -t mpi-docker-proyecto .`

#### Poner tag al proyecto:
`docker tag mpi-docker-proyecto gcr.io/second-impact-327701/mpi-docker-proyecto`

#### Hacer push al repo:
`docker push gcr.io/second-impact-327701/mpi-docker-proyecto`

---
## Crear cluster
#### Crear el cluster a partir del *.yaml*:
`kubectl apply -f mipod.yaml`

> ##### Para poder eliminar el deploy actual usamos el comando:
> `kubectl delete deploy mpi-docker`

#### Dar permismos al archivo *.sh* para poder correrlo:
`chmod +x pod_copy.sh`

#### Ejecutar el *.sh* para obtener las direcciones de los pods:
`./pod_copy.sh`

#### Copiar el archivo *hosts* para tener las direcciones en todos los pods:

`for podname in $(kubectl get pods -o json| jq -r '.items[].metadata.name'); do kubectl cp hosts ${podname}:/mpi/; done`

---
## Ejecutar el servidor de Flask

#### Necesitamos obtener el pod donde ejecutaremos el servidor:
`kubectl get pods`

#### Sustituimos el `<pod>` con el *id* del que usaremos:
`kubectl exec <pod> -- mpiexec -f hosts -n 2 python3 project.py`

##### Ejemplo:
`kubectl exec mpi-docker-6cb58bc9f6-dbf5j -- mpiexec -f hosts -n 2 python3 project.py`

----
## Ejecutar python sin Flask:
#### Aplicamos el mismo proceso anterior pero con los parametros de las figuras:

`kubectl exec mpi-docker-77d7cb5ddb-rpc4h -- mpiexec -f hosts -n 2 python3 project.py 1 8 4`

| Figura | ID | Param1 | Param2 | Param3 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Cilindro | 1 |  Altura | Radio | -- |
| Cubo | 2 |  Altura | -- | -- |
| Esfera | 3 |  Radio | -- | -- |
| Cono | 4 |  Altura | Radio | -- |
| Prisma | 5 | Altura | Ancho | Largo |
