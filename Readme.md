# Proyecto Portal Córdoba
Este proyecto se hizo con la finalidad de crear un portal turistico solicitado en la materia Programacion 2.

## Proposito del proyecto:
Para este proyecto elegimos a la provincia de Córdoba y algunas de sus principales ciudades turisticas, mostrando las distancias entre ellas. El principal objetivo es detallar los lugares turistos más importantes de cada ciudad y el camino más corto de una ciudad a otra. 

## Descripcion del Proyecto:
Sobre la base que nos dio el proyecto, nosotros implementamos:
- Atributos nuevos a la clase city.
- Creamos una nueva funcion "obtener_vecinos" en la clase city.
- Creamos una nueva clase "Lugar_Turistico" y le agregamos la funcionabilidad, tanto en views.py como en el admin.py, para que lo muestre en dichos archivos.
- Agregamos archivos de estilos al proyecto en si, generando una mejor vista al usuario.
- Desarrollamos la funcion Dijkstra para calcular la ruta más corta.
- Configuramos la carpeta static.
- Modificamos y agregamos contenido a los distintos archivos html, como por ejemplo se pueden crear distintas ciudades dinamicamente.
- Se comento la clase de "ArbolBinarioBusqueda"

## Analisis de Complejidad de algoritmos de Dijkstra:
El análisis de complejidad del algoritmo de Dijkstra es de O(V logV), donde "V" es el número de vértices ya que tenemos una cola de prioridad.

## ¿Que anda? 
Funciona todo lo requerido en la consigna del trabajo.

## ¿Que no anda? 
Creemos que funciona todo, pero deberiamos profundizar mucho más en los temas de grafo y Dijkstra.

## ¿Que se puede mejorar?
- Se podría implementar que los lugares turisticos se creen de manera dinamica ya que ahora solo podemos cargar solo 3 lugares turisticos por ciudad.
- Tambien se podria cambiar el diseño del nav, para que sea mas estetico.
- En el footer se tendrian que enlazar las redes sociales del portal.

