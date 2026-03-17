# Documentacion sobre el proyecto final de clase
en este documento veremos principalmente dos cosas, que se presentara  continuacion:

## porque escoji cada etiqueta en mi proyecto.

1. <header>- para el encabezado de mi trabajo. Para el titulo y la barra de navegacion.
2. <nav>- me sirve para poner la barra de navegacion de la pagina.
3. <main>- el cuerpo principal de mi pagina. Aca puse todo el contenido de mi pagina, puesto que mi pagina solo tiene un tema central.
4. <section>- para separar diferentes contenidos uno de otro, por ejemplo para separar los gustos de la metas.
5. <figure>- para poner una imagen, la imagen de mi avatar.
6. <figcaption>- para ponerle una decripcion al la imagen. Explicar el porque de la imagen.
7. <time>- para indicar que lo que hay dentro de cada <li> de la <ul> me esta conteniendo una fecha(y cual es la fecha).

## Estructura DOM de mi pagina.

html
├── head
│   ├── meta (charset="UTF-8")
│   ├── meta (name="viewport")
│   ├── meta (name="description")
│   └── title
│       └── "Tarjeta de presentacion personal"
│
└── body
    ├── header
    │   ├── div
    │   │   ├── h1
    │   │   │   └── "Alejandro Bolivar Echeverri"
    │   │   └── p
    │   │       └── "actualmente estudiante de la Javiera Londoño"
    │   │
    │   └── nav
    │       ├── a ("presentacion")
    │       ├── a ("gustos")
    │       ├── a ("disgustos")
    │       ├── a ("anecdotas graciosas")
    │       └── a ("metas")
    │
    └── main
        ├── section#presentacion
        │   ├── h2
        │   │   └── "quien soy yo?"
        │   ├── p
        │   │   └── (texto de presentación)
        │   └── figure
        │       ├── img
        │       └── figcaption
        │           └── "este es mi avatar"
        │
        ├── section#gustos
        │   ├── h2
        │   │   └── "Mis gustos"
        │   └── ul
        │       ├── li
        │       ├── li
        │       ├── li
        │       ├── li
        │       ├── li
        │       └── li
        │
        ├── section#disgustos
        │   ├── h2
        │   │   └── "mis disgustos"
        │   └── ul
        │       ├── li
        │       ├── li
        │       ├── li
        │       ├── li
        │       └── li
        │
        ├── section#anecdotas
        │   ├── h2
        │   │   └── "anecdotas graciosas"
        │   └── ul
        │       ├── li
        │       │   └── time
        │       ├── li
        │       │   └── time
        │       ├── li
        │       │   └── time
        │       ├── li
        │       │   └── time
        │       └── li
        │           └── time
        │
        └── section#metas
            ├── h2
            │   └── "metas"
            └── p
                └── (texto de metas)