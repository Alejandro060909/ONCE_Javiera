# Resumen: Curso de Requerimientos de Software

Este documento resume las 5 secciones clave identificadas en las capturas de pantalla del curso interactivo de Ingeniería de Requerimientos.

---

## 1. Profundización del Concepto de Requerimiento
* **Definición general:** Un requerimiento es una condición o capacidad que debe cumplir un software para resolver un problema, alcanzar un objetivo o satisfacer un contrato, norma o especificación formal.
* **Niveles de definición:**
  1. **Requerimientos del Negocio:** Objetivos de alto nivel de la organización.
  2. **Requerimientos del Usuario:** Lo que el usuario final necesita hacer con el sistema.
  3. **Requerimientos del Sistema:** Especificaciones técnicas detalladas para el desarrollo (funcionales y no funcionales).
* **Fuentes de requerimientos:** Usuarios finales, clientes/patrocinadores, leyes/normativas y sistemas existentes.
* **Características de un buen requerimiento:** Debe ser necesario, conciso, completo, consistente, rastreable y verificable.

---

## 2. Requerimientos Funcionales (RF)
* **¿Qué son?:** Son los que definen **qué debe hacer** el sistema. Describen los servicios, funciones, entradas, procesos y salidas que el software proporcionará al usuario.
* **Cómo identificarlos:** Se centran en las acciones del sistema. Suelen redactarse utilizando la estructura clásica de Historias de Usuario: *"Como [rol], quiero [acción] para [beneficio]"*.
* **Ejemplos comunes:**
  * **Iniciar sesión:** Permitir el ingreso mediante correo y contraseña.
  * **Crear Diario:** Opción para que el usuario registre sus notas o actividades diarias.
  * **Generar informes:** El sistema debe compilar datos y exportarlos en PDF.
  * **Búsqueda:** Filtrar contenidos o productos por categorías.

---

## 3. Requerimientos No Funcionales (RNF)
* **¿Qué son?:** Definen **cómo** debe funcionar el sistema. No describen características operativas directas, sino restricciones, propiedades emergentes o criterios de calidad que limitan el diseño o la infraestructura.
* **Categorías comunes:**
  * **Rendimiento y Almacenamiento:** Tiempos de respuesta, volumen de datos soportado.
  * **Seguridad:** Protección de datos, cifrado de contraseñas.
  * **Usabilidad:** Facilidad de aprendizaje y diseño intuitivo de la interfaz.
  * **Confiabilidad:** Disponibilidad del sistema (ej. 99.9% del tiempo online).
  * **Leyes y Regulaciones:** Cumplimiento de normativas de protección de datos (como GDPR).

---

## 4. Atributos de Calidad (Norma ISO 25010)
Los Atributos de Calidad son un subconjunto de los requerimientos no funcionales que miden la excelencia del software. La norma ISO 25010 define las siguientes características clave:
1. **Adecuación Funcional:** Que el software haga exactamente lo que se necesita.
2. **Eficiencia de Desempeño:** Velocidad de respuesta y optimización de recursos.
3. **Compatibilidad:** Capacidad de coexistir e interactuar con otros sistemas.
4. **Usabilidad:** Facilidad de uso y experiencia de usuario satisfactoria.
5. **Fiabilidad (Confiabilidad):** Mantener un nivel especificado de rendimiento bajo condiciones dadas.
6. **Seguridad:** Protección de la información y datos contra accesos no autorizados.
7. **Mantenibilidad:** Facilidad con la que el código puede ser modificado, corregido o mejorado.
8. **Portabilidad:** Facilidad para transferir el sistema de un entorno a otro (hardware/software).

---

## 5. Ciclo de Vida y Evaluación del Aprendizaje
* **Ciclo de vida de un requerimiento:** Pasa por las etapas de Elicitación (captura), Análisis, Especificación (documentación) y Validación.
* **Sección Práctica (Módulos de Quizzes):** Las imágenes muestran cuestionarios interactivos de opción múltiple y de Verdadero/Falso diseñados para evaluar la comprensión del estudiante sobre:
  * Diferenciación exacta entre lo funcional (el "qué") y lo no funcional (el "cómo").
  * Identificación de atributos de calidad específicos en casos de estudio prácticos.