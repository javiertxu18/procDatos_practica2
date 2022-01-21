# procDatos_practica2
Esta es la práctica número 2 de la asignatura de procesamiento de datos del máster en big data.

*NOTA: Ejecutar sobre windows*

## Enunciado
La práctica consiste en descargar información de diversas tablas (INE, Twitter, scrapp), cargarlas en Python, limpiar esos datos para dejarlos de manera correcta y una vez limpios subirlos a una capa raw de una BBDD.

Una vez estén en esa capa raw hay que crear una capa operacional donde las tablas estén relacionadas mediante un modelo de datos que tenga sentido.

El número mínimo de tablas a crear son 5 en la capa raw.

Se puntuará complejidad tanto del modelo como de las descargas y transformaciones.

## Base de datos

Configurar archivo ./config.ini con la info de tu postgreSql

## Esquema de postgresql

Se ha entregado el esquema de la base de datos junto al resto de cosas de la práctica
, el fichero se llama "dbRaw.sql".

Para importarla, cree una base de datos nueva,
haga clic derecho sobre ella y seleccione restaurar.

En la opción de filename, seleccione el fichero dbRaw.sql

Y en la opcion de role name, seleccion e 'postgres'.

Una vez hecho esto, configure el fichero config.ini con la info de su server postgreSQL
y ejecute el programa.


