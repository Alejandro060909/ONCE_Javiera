# Resumen: Introducción al Diseño de Software

Este documento resume los fundamentos, principios arquitectónicos y las fases iniciales para transformar requerimientos en especificaciones técnicas de diseño según el curso interactivo.

---

## 1. ¿Qué es el Diseño de Software?
* **Definición:** Es el proceso técnico mediante el cual los requerimientos de software se traducen en una representación interna del sistema (planos técnicos, estructuras y modelos) antes de comenzar la codificación.
* **El cambio de enfoque:** * **Análisis de Requerimientos:** Se enfoca en el **¿Qué?** (el problema y las necesidades del cliente).
  * **Diseño de Software:** Se enfoca en el **¿Cómo?** (la solución técnica, componentes e infraestructura).

---

## 2. Niveles del Diseño de Software
El diseño se aborda desde diferentes perspectivas para controlar la complejidad:
1. **Diseño Arquitectónico:** Define la estructura global del sistema, sus componentes principales (módulos, subsistemas) y cómo se comunican entre sí.
2. **Diseño de Interfaz:** Modela la interacción entre el software y los usuarios humanos, así como las conexiones con otros sistemas externos (APIs).
3. **Diseño de Componentes (Detallado):** Define la lógica interna, algoritmos, estructuras de datos y clases que darán vida a cada módulo individual.
4. **Diseño de Datos:** Estructura las bases de datos, esquemas y modelos de almacenamiento necesarios para soportar la información.

---

## 3. Principios Fundamentales del Diseño
Para garantizar un software de calidad, mantenible y escalable, se deben seguir estos criterios:
* **Abstracción:** Permitir enfocarse en lo importante de un componente ocultando los detalles de implementación complejos.
* **Modularidad:** Dividir el sistema en partes independientes (módulos) que se encarguen de tareas específicas.
* **Ocultamiento de Información (Encapsulamiento):** Asegurar que los detalles internos de un módulo no sean accesibles para otros que no lo necesiten.
* **Cohesión:** Medida de qué tan enfocada está una sección de código en hacer una sola cosa bien (Se busca **Alta Cohesión**).
* **Acoplamiento:** El nivel de dependencia entre diferentes módulos. Si un módulo cambia, no debería romper los demás (Se busca **Bajo Acoplamiento**).

---

## 4. Conceptos de Arquitectura de Software
* **Estilos Arquitectónicos Comunes:**
  * **Arquitectura en Capas:** Divide el sistema en niveles de responsabilidad (Presentación, Lógica de Negocio, Datos).
  * **Cliente-Servidor:** Distribuye las tareas entre proveedores de recursos (servidores) y demandantes (clientes).
  * **Microservicios:** Descompone la aplicación en un conjunto de servicios autónomos, pequeños y desplegables de manera independiente.
* **Importancia:** Una mala elección arquitectónica desde el inicio puede hacer que el software sea imposible de escalar o extremadamente costoso de mantener.

---

## 5. Evaluación del Módulo (Quizzes)
Las capturas muestran secciones prácticas para evaluar que el estudiante comprenda:
* La diferencia exacta entre el rol de un analista de requerimientos y el de un diseñador/arquitecto de software.
* La aplicación de los conceptos de cohesión y acoplamiento en casos prácticos.
* La identificación de fallos de diseño cuando los módulos dependen demasiado entre sí (alto acoplamiento).