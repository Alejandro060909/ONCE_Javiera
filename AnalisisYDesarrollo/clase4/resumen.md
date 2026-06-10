# Resumen: Documentación de Requerimientos - Historias de Usuario

Este documento sintetiza la información clave sobre el uso de Historias de Usuario (User Stories) en entornos ágiles, los criterios de calidad INVEST y las dinámicas prácticas de este módulo.

---

## 1. ¿Qué es una Historia de Usuario?
* **Definición:** Es una explicación simple, informal y general de una característica de software escrita desde la perspectiva del usuario final o cliente. Su objetivo es centrar la conversación en el valor del negocio en lugar de los detalles técnicos.
* **La Estructura Clásica (Plantilla):**
  > **Como** [tipo de usuario / rol]  
  > **Quiero** [realizar una acción o funcionalidad]  
  > **Para** [obtener un beneficio, valor o resultado]
* **Ejemplo práctico:** *"Como cliente del banco, quiero ver el saldo de mi cuenta en la pantalla principal para saber cuánto dinero tengo disponible inmediatamente."*

---

## 2. Los Criterios INVEST
Para asegurar que una Historia de Usuario esté bien redactada y sea útil para el equipo de desarrollo, debe cumplir con el acrónimo **INVEST**:

* **I - Independiente (Independent):** No debe depender de otra historia; debe poder desarrollarse y entregarse por separado.
* **N - Negociable (Negotiable):** No es un contrato rígido; deja espacio para la discusión y el ajuste entre el cliente y los desarrolladores.
* **V - Valiosa (Valuable):** Debe aportar un valor claro y directo al usuario final o al negocio.
* **E - Estimable (Estimable):** El equipo de desarrollo debe ser capaz de calcular el esfuerzo o tiempo necesario para construirla.
* **S - Pequeña (Small):** Debe tener el tamaño adecuado para poder completarse dentro de una sola iteración o sprint (generalmente de 1 a 2 semanas).
* **T - Testeable (Testable):** Debe poder verificarse mediante pruebas claras para confirmar que funciona correctamente.

---

## 3. Criterios de Aceptación (El "Cómo saber si terminamos")
* **Definición:** Son las condiciones específicas que debe cumplir la Historia de Usuario para que sea considerada como "Completada" (Done) por el cliente.
* **Estructura común (Dado/Cuando/Entonces):**
  * **Dado (Given):** El contexto o estado inicial.
  * **Cuando (When):** La acción que realiza el usuario.
  * **Entonces (Then):** El resultado esperado en el sistema.

---

## 4. Comparativa: Historias de Usuario vs. Casos de Uso
El curso resalta las diferencias metodológicas para documentar:

| Característica | Historias de Usuario (Ágil) | Casos de Uso (Tradicional / UML) |
| :--- | :--- | :--- |
| **Enfoque** | Centrado en el valor del negocio y la conversación. | Centrado en el comportamiento detallado del sistema. |
| **Formato** | Breve, estructurado en una sola frase con criterios de aceptación. | Documento extenso con flujos principales, alternativos y técnicos. |
| **Audiencia** | Fácilmente comprensible por clientes y stakeholders de negocio. | Más técnico, orientado a diseñadores, arquitectos y desarrolladores. |

---

## 5. Sección Práctica (Quizzes del Módulo)
Las capturas muestran ejercicios interactivos donde el estudiante debe:
* Identificar si una Historia de Usuario cumple o rompe con los criterios INVEST (por ejemplo, detectar historias que son demasiado grandes o que no aportan valor).
* Clasificar correctamente los componentes de la plantilla (*Como / Quiero / Para*).
* Validar escenarios mediante la asignación correcta de criterios de aceptación de tipo Verdadero/Falso.