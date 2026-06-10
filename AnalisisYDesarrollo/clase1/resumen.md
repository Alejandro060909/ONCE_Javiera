# Análisis y Diseño de Software

## Ciclo de Vida de un Proyecto de Software

* **Análisis de requerimientos:** Se escribe qué se debe y qué no se debe hacer.
* **Diseño:** Se define cómo se estructurará el proyecto.
* **Implementación:** Se comienza a programar lo que se estableció en el diseño.
* **Pruebas:** Se comprueba que sí funcione el proyecto.
* **Despliegue:** Se lanza la aplicación.
* **Mantenimiento:** Se solucionan los errores que ocurrieron después de probarlo con usuarios reales.

---

## Metodologías Estructuradas

* **Cascada:** Utiliza el mismo ciclo de vida que el de un proyecto, pero este no admite devolverse en ningún paso (es estrictamente secuencial).
* **Modelo V:** Cada paso del ciclo de vida tiene una fase de revisión. Si no pasa este filtro, no se continúa.
* **Modelo Espiral:** Es una ramificación del método en cascada, pero en este, cada vez que se llega al último paso, se vuelve a comenzar un nuevo ciclo.

---

## Metodologías Ágiles


### 1. Scrum (Gestión por Ritmo)
Se basa en bloques de tiempo fijos (*Sprints*) y roles muy definidos para mantener el enfoque.

* **Daily Standup:** Sincronización diaria de 15 minutos centrada en el progreso y los impedimentos.
* **Roles Clave:**
    * **Product Owner:** Maximiza el valor del producto (el "Qué").
    * **Scrum Master:** Facilita el proceso y elimina bloqueos (el "Cómo").
    * **Equipo de Desarrollo:** Profesionales autónomos que construyen el incremento.

### 2. Kanban (Gestión por Flujo)
Inspirado en el sistema de producción de Toyota, utiliza tarjetas visuales en un tablero y se enfoca en la continuidad del trabajo.

### 3. XP - Extreme Programming (Excelencia Técnica)
Se centra en la calidad del código y en las buenas prácticas de ingeniería de software.

* **Programación en Pares:** El *Conductor* escribe el código mientras el *Navegador* revisa la estrategia y detecta errores en tiempo real.
* **TDD (Desarrollo Guiado por Pruebas):** Sigue el ciclo *Red-Green-Refactor*:
    1. Escribir una prueba que falle.
    2. Escribir el código mínimo necesario para que pase.
    3. Limpiar y optimizar el código (Refactorización).