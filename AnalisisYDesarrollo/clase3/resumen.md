# Resumen: Elicitación de Requerimientos de Software

Este documento resume las técnicas, buenas prácticas, errores comunes y el análisis de viabilidad explicados en el módulo de elicitación del curso interactivo.

---

## 1. El Arte de Elicitar
* **Definición:** Es el proceso de descubrir, entender, recolectar y priorizar las necesidades reales de los usuarios y partes interesadas (*stakeholders*) para un sistema de software. No es solo "preguntar", es investigar a fondo.
* **El Problema del Iceberg:** El cliente suele verbalizar solo una pequeña parte de lo que realmente necesita (la punta del iceberg). Los requerimientos implícitos, las reglas de negocio complejas y las necesidades reales están ocultas bajo la superficie.
* **Las 3 Grandes Técnicas Base:**
  1. **Entrevistas:** Diálogo directo con los interesados.
  2. **Encuestas:** Cuestionarios estructurados para recolectar datos a gran escala.
  3. **Observación:** Analizar cómo trabajan los usuarios en su entorno real.

---

## 2. Técnica 1: Entrevistas
* **Tipos de estructura:**
  * **Estructurada:** Sigue un guión rígido de preguntas predefinidas.
  * **No estructurada:** Es una conversación libre y abierta.
  * **Semi-estructurada:** Combina un guión base con la flexibilidad de profundizar según las respuestas (la más recomendada).
* **Tipos de preguntas:**
  * **Abiertas:** Permiten al usuario explayarse y explicar su flujo de trabajo (ej. *"¿Cómo realiza este proceso actualmente?"*).
  * **Cerradas:** Buscan respuestas específicas, de tipo Sí/No o selecciones puntuales.
* **Errores comunes al entrevistar:** Asumir respuestas, guiar al usuario hacia la solución que el desarrollador quiere, no escuchar activamente o perder el enfoque del problema de negocio.

---

## 3. Técnica 2: Encuestas y Cuestionarios
* **¿Cuándo usarlas?:** Ideales cuando se necesita obtener información, preferencias o datos estadísticos de un volumen masivo de usuarios en poco tiempo.
* **Buenas prácticas de diseño:**
  * Mantenerlas cortas, claras y fáciles de responder.
  * Combinar escalas de valoración (ej. Escala de Likert del 1 al 5) con opciones de selección múltiple.
  * Incluir una introducción que explique el propósito de la encuesta.
  * Probar el cuestionario con un grupo pequeño antes de enviarlo masivamente.

---

## 4. Técnica 3: Observación (Shadowing)
* **¿Qué es?:** Consiste en convertirse en la "sombra" del usuario mientras realiza sus tareas cotidianas para entender sus dolores y procesos reales sin sesgos verbales.
* **Variantes de observación:**
  * **Pasiva:** El analista mira y toma notas sin intervenir ni interrumpir el flujo de trabajo.
  * **Activa:** El analista interrumpe puntualmente al usuario para hacer preguntas sobre por qué realiza una acción específica.
* **Qué registrar:** Tiempos de ejecución, cuellos de botella, herramientas auxiliares que usan (como hojas de cálculo o notas adhesivas) y excepciones en el proceso.

---

## 5. Análisis de Viabilidad de Requerimientos
Una vez recolectados los requerimientos, se debe evaluar si es realista implementarlos mediante las **5 Dimensiones de la Viabilidad**:

1. **Técnica