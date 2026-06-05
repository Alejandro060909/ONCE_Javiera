# Guía Completa de Backend y Desarrollo de APIs

## 1. Lenguajes de Programación y Fundamentos

El primer paso fundamental es elegir un lenguaje de programación. Las opciones varían según el propósito:

### Populares y versátiles
- **Java** → Muy utilizado en entornos empresariales.
- **C#** → Común en aplicaciones corporativas y ecosistemas .NET.
- **Go** → Destaca por su simplicidad y rendimiento.
- **PHP** → Muy usado en desarrollo web tradicional.
- **Ruby** → Popular por su productividad y sintaxis amigable.

### Específicos
- **Python** → Muy común por su relación con el *data science* e inteligencia artificial.

### Alto rendimiento
- **C++** → Utilizado cuando se requiere eficiencia extrema y control de memoria.
- **Rust** → Enfocado en seguridad y alto rendimiento.

### Lenguajes de nicho
- **Haskell**
- **Elixir**

---

### Fundamentos esenciales

Independientemente del lenguaje elegido, es vital dominar las bases:

- Variables
- Funciones
- Objetos
- Listas
- Clases

---



# 2. Protocolo HTTP y Clientes REST

Para crear servidores web, es obligatorio entender el **protocolo HTTP**, incluyendo:

- Métodos
- Peticiones
- Respuestas
- Códigos de estado
- Cabeceras
- Cookies

---

## Clientes REST para pruebas

Se utilizan clientes REST para probar el servidor.

### Herramienta más popular
- **Postman**

### Alternativas
- **Insomnia**
- **cURL**
- **Thunder Client** (extensión de VS Code)

---

## Comunicación desde el frontend

Desde el lado del cliente, se suelen usar bibliotecas como:

- **Fetch**
- **Axios**

Estas permiten comunicarse con el servidor backend.

---

# 3. Frameworks: Minimalistas vs. Opinionados

Los frameworks optimizan el desarrollo al evitar repetir código común.

## Frameworks minimalistas

Dan libertad para configurar todo desde cero.

### Ejemplos
- **Express** (Node.js)
- **Flask** (Python)
- **Fiber** (Go)

### Características
- Más flexibilidad
- Menos estructura impuesta
- Mayor control manual

---

## Frameworks opinionados

Ya incluyen una estructura definida y módulos preconfigurados.

### Ejemplos
- **Laravel** (PHP)
- **Django** (Python)
- **Spring** (.NET/Java)
- **Ruby on Rails**

### Características
- Desarrollo más rápido
- Arquitectura definida
- Menor libertad estructural

---

# 4. Arquitecturas de API y Documentación

Dependiendo de la necesidad, existen diversas formas de estructurar la comunicación.

---

## REST API

La arquitectura más común.

### Características
- Basada en intercambio de datos en formato **JSON**
- Muy utilizada en aplicaciones web y móviles

---

## SOAP

### Características
- Utiliza **XML**
- Más lenta
- Mayor enfoque en seguridad

### Uso común
- Sistemas gubernamentales
- Sistemas bancarios

---

## GraphQL

### Características
- Arquitectura más moderna
- Permite unificar distintas APIs en un solo punto

---

## gRPC

### Características
- Protocolo de Google
- Basado en binarios
- Diseñado para comunicación rápida entre microservicios

---

## WebSockets

### Características
- Comunicación en tiempo real

### Casos de uso
- Chats
- Paneles de control
- Aplicaciones en vivo

---

## Documentación de APIs

Herramientas comunes:

- **Swagger**
- **API Docs**

---

# 5. Bases de Datos y ORMs

El backend debe gestionar datos mediante dos grandes tipos de bases de datos.

---

## Bases de datos relacionales (SQL)

### Recomendación inicial
- **PostgreSQL**

### Motivos
- Código abierto
- Fácil de desplegar

### Otras opciones
- **MySQL**
- **MariaDB**

---

## ORMs

Permiten interactuar con la base de datos sin escribir SQL puro.

### Ejemplos
- **Prisma**
- **TypeORM** → Node.js
- **Eloquent** → Laravel
- **SQLAlchemy** → Python

---

## Bases de datos no relacionales (NoSQL)

Organizan los datos de forma distinta (*Not Only SQL*).

### Recomendación principal
- **MongoDB**

### Motivo
- Uso de formato JSON

### Otras opciones
- **Redis**
- **Cassandra**
- **Firebase**
- **DynamoDB**

---

# 6. Testing, Validación y Seguridad

## Testing

Es esencial para asegurar que los cambios no rompan funcionalidades.

### Tipos principales

#### Unit Testing
Prueba partes pequeñas del sistema.

#### End-to-End Testing
Prueba flujos completos de la aplicación.

---

## Motores de plantillas

Permiten renderizar HTML desde el servidor con lógica dinámica.

### Herramientas
- **PUG**
- **Handlebars**

### Uso común
- Envío de correos
- Generación dinámica de vistas

---

## Validación

Los datos recibidos del frontend deben validarse.

### Herramientas
- **Zod**
- **Express Validator**

---

## Seguridad

Es crucial conocer:

### OWASP Top 10
Lista de ataques y vulnerabilidades comunes.

### JSON Web Tokens (JWT)
Utilizados para:
- Credenciales
- Sesiones
- Autenticación

### Protocolos adicionales
- **OAuth**
- **2FA** (Segundo factor de autenticación)

---

# 7. Despliegue y Cloud Computing

Una vez creada la API, debe subirse a la nube.

---

## PaaS (Platform as a Service)

Permite desplegar aplicaciones fácilmente conectando GitHub.

### Ejemplos
- **Render**
- **Railway**
- **Vercel**
- **Fly**

---

## IaaS (Infrastructure as a Service)

Grandes plataformas cloud donde se administran servicios manualmente.

### Proveedores
- **AWS**
- **Azure**
- **Google Cloud**

### Servicios mencionados
- **S3** → Archivos
- **RDS** → Bases de datos
- **VPC** → Redes

---

## Contenedores

### Docker
Fundamental para crear entornos aislados.

### Orquestadores
- **Kubernetes**
- **Docker Swarm**

### Función
- Escalar
- Administrar contenedores

---

## Servicios adicionales

### Gestión de secretos
- **AWS Secret Manager**

### Autenticación externa
- **Auth0**
- **Firebase Auth**

---

# 8. Conceptos Avanzados y Seniority

Al avanzar, el desarrollador se enfoca en el **Diseño de Sistemas**.

---

## Microservicios

Consiste en dividir un monolito en múltiples backends distribuidos.

---

## Infraestructura avanzada

Incluye:

- API Gateways
- Proxy Servers
- Funciones Serverless
- Cronjobs

---

## Comunicación asíncrona

Permite manejar tareas pesadas mediante colas (*Queues*).

### Herramientas
- **RabbitMQ**
- **Apache Kafka**