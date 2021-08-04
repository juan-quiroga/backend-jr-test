# Backend JR Test

La presente prueba tiene como objetivo ver como te desempeñas a la hora de resolver un problema. La evaluación no posee un tiempo límite de resolución. Para resolverla vas a necesitar leer sobre los siguientes temas:
 * Github
 * Bash
 * MySQL
 * Conexión a MySQL desde python
 * MySQL locking
 * Testing de unidad
 * APIs REST
 * Testing de integración

El test consiste de una aplicación sencilla que se encarga de manejar un stock de productos. Se deben crear APIs REST para manejar la creación, el listado, la obtención y la actualización del stock de un producto. Cada API debe interactuar con MySQL para persistir la información que corresponda. 

## Antes de empezar

### Github

Una vez que termines subirás tu código a github con lo cual tenés que bajarte el repositorio y crear una rama cuyo nombre sea tu nombre y apellido. La rama a crear debe salir de `main`. El repositorio es: `https://github.com/Optiwe/backend-jr-test`

### Virtual env

Para poder correr el proyecto se necesitan instalar las dependencias descritas en el archivo `requirements.txt`. Para poder hacerlo de manera aislada primero es necesario crear un virtual environment. 

 1. Instalar venv con: `pip install virtualenv`
 2. Crear el venv con: `virtualenv venv`

Nota: El proyecto corre sobre python 3.6 o superior. Si no estás seguro de que versión de python utiliza el venv creado, activalo con `source venv/bin/activate` y luego correr el comando `python --version`. Si la version de python es inferior a 3.6, instala python 3.6 y luego crear la venv especificando la version de python a utilizar usar, por ejemplo en linux usar `virtualenv --python=/usr/bin/python3.7 venv`

Una vez creado el venv, activarlo con `source venv/bin/activate` y utilizar el siguiente comando para instalar las dependencias: `pip install -r requirements.txt`

### Docker

El proyecto necesita un servidor MySQL corriendo localmente. Una manera sencilla de instalar un servidor MySQL es utilizar docker. Por otro lado necesitaremos un servidor HTTP. Para poder contar con ambos servicios de manera simple utilizaremos docker-compose. Ver el archivo `docker-compose.yml` para más detalles.

Luego de haber instalado docker y docker-compose utilizar el siguiente comando para levantar el servidor HTTP y el servidor MySQL: `docker-compose up`

Para verificar el correcto funcionamiento de los servidores correr `pytest -s -v test_api.py::ApiTestCase::test_status`. 

En el caso de que esté funcionando bien vas a ver la siguiente salida `test_api.py::ApiTestCase::test_status PASSED`. En caso de no ser asi, alguno de los dos servidores es probable que contenga algún error. Revisa la salida del comando `docker-compose up`

### Archivos del proyecto

La siguiente sección explica el contenido de cada archivo del proyecto:
 * api.py: Contiene las APIs HTTP disponibles
 * db.py: Contiene la clase DB la cual se encarga de manejar las conexiones a MySQL
 * docker-compose.yml: Contiene la definición de como levantar el servidor MySQL y el servidor HTTP
 * item.py: Contiene la clase ItemDAO, la cual se encarga de ejecutar las queries SQL
 * itemservice.py: Contiene la lógica de negocio que se encarga de manejar los items
 * lib.py: Contiene algunas clases y métodos utilitarios
 * main.py: Contiene el comando que permite inicializar la base de datos.
 * migration.py: Contiene las queries necesarias para inicializar MySQL
 * requirements.txt: Contiene el listado de librerias que necesita el proyecto para funcionar.
 * test_api.py: Contiene los test de integración que se encargan de verificar el correcto funcionamiento de las APIs REST
 * test_itemservice.py: Contiene algunos tests de unidad que se encargan de verificar el correcto funcionamiento de las queries.
 * uwsgi.ini: Contiene la configuración del servidor HTTP.

## Desarrollo

El desarrollo consiste en hacer que tanto los tests definidos en `test_itemservice.py` como en `test_api.py` pasen correctamente. Para correr los tests utilizar el siguiente comando `pytest -s -v`

### Tests de unidad

Lo primero que debes hacer es escribir el código necesario para que pasen los test definidos en `test_itemservice.py`. Para ello debes escribir el código faltante en el archivo `item.py`. El código faltante se debe encargar de ejecutar las queries a MySQL para llevar a cabo el objetivo de la función en cuestión. Para poder obtener una conexión a la db desde `item.py` usar: `self.db.get_connection()`

### Tests de integración

Una vez que los tests de unidad te estén pasando correctamente, tenés que escribir el código faltante en el archivo `api.py` para que pasen los tests definidos en `test_api.py`. Dicho código se debe encargar de leer el body, los query params y los url params según corresponda en cada caso y ejecutar los métodos correspondientes en la clase `ItemService` 


## Para terminar

Una vez que tanto los tests de unidad como los de integración te estén pasando, subí tu código al repositorio `https://github.com/Optiwe/backend-jr-test` y crea un PR contra la rama `main`