# Distributed Systems Cache-RPC

## Descripción general

El código fuente de la aplicación se encuentra en la carpeta `src` y se encuentra programado en Python. Los modulos son los siguientes:

### Módulos programados

* **buscador.py:** Módulo que contiene la Api REST, recibe las request para buscar productos y son devueltos en formato JSON. Si el resultado de la busqueda se encuentra en el cache lo retorna inmediatamente, caso contrario se comunica via RPC con el modulo del inventario para obtener el resultado.
* **cache.py:** Módulo que contiene los metodos para acceder al cache.
* **inventario.py:** Módulo que contiene el servicio que busca en el inventario `inventory_list.json`, el cual es un JSON que contiene la lista de productos.

### Otros modulos

* **search.proto:** Módulo que contiene la estructura de los datos utilizados para la comunicación.
* **search_pb2_grpc.py y search_pb2.py:** Módulos generados a partir de la estructura de datos requerida para ser utilizadas en Python.
* **client.py y server.py:** Módulos de prueba proporcionados por el ayudante. 

## Configuración y ejecución

### Configuración de REDIS

La configuración utilizada en redis fue la siguiente:

* Política de desalojo: LRU, elimina del cache la que no se ha usado en mayor tiempo, configurada en el cliente de redis con el comando

```bat 
config set maxmemory-policy allkeys-lru
```

* Maxima memoria: 20MB, configurado en cliente de redis con el comando

```bat 
config set maxmemory 20M
```

### Dependencias

Las dependencias necesarias para que se pueda ejectuar el programa se encuentran en el archivo `requirements.txt`.

### Ejecución

Con las dependencias instaladas se deben ejecutar los archivos `buscador.py` e `inventario.py`.

 
## Redis install
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-es
