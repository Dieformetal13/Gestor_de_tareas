# **INSTRUCCIONES PARA LA APLICACIÓN DE GESTIÓN DE TAREAS**
=================================================

# **DESCRIPCIÓN GENERAL**
Este proyecto es una aplicación web simple para la gestión de tareas, desarrollada con Flask y SQLAlchemy. Permite crear, marcar como completadas y eliminar tareas de una lista.

# **REQUISITOS**
Python 3.6 o superior

**Bibliotecas requeridas** (instaladas automáticamente mediante requirements.txt):

Flask

SQLAlchemy

# **ESTRUCTURA DE ARCHIVOS**

**main.py:** Archivo principal de la aplicación Flask

**models.py:** Define el modelo de datos para las tareas

**db.py:** Configuración de la base de datos SQLite

**requirements.txt:** Lista de dependencias

**templates/index.html:** Plantilla HTML para la interfaz de usuario

**static/main.css:** Hoja de estilos CSS

# **INSTRUCCIONES DE EJECUCIÓN**

**Instalación:**

Instala las dependencias: pip install -r requirements.txt

**Ejecución:**

**Inicia la aplicación:** python main.py

La aplicación estará disponible en: http://localhost:5000

**Uso:**

Añade tareas escribiendo en el campo de texto y pulsando "Guardar"

Marca tareas como completadas haciendo clic en el icono verde (✓)

Elimina tareas haciendo clic en el icono rojo (🗑️)

# **DESCRIPCIÓN DE LOS ARCHIVOS**

**main.py**

Configura la aplicación Flask

Define las rutas principales:

/: Muestra todas las tareas

/crear-tarea: Crea una nueva tarea

/eliminar-tarea/<id>: Elimina una tarea específica

/tarea-hecha/<id>: Marca/desmarca una tarea como completada

**models.py**

Define el modelo Tarea con:

id: Identificador único (primary key)

contenido: Texto de la tarea (máx. 200 caracteres)

hecha: Booleano que indica si está completada

**db.py**

Configura la conexión a la base de datos SQLite (database/tareas.db)

Crea la sesión de base de datos

Define la base declarativa para los modelos

**templates/index.html**

Interfaz de usuario con:

Formulario para añadir tareas

Lista de tareas con opciones para marcar/completar y eliminar

Usa Bootstrap para el diseño

Incluye iconos de Font Awesome

**static/main.css**

Estilos CSS personalizados:

Fuente especial para el título

Gradiente de fondo

Estilo para tareas completadas (tachado)

# **CARACTERÍSTICAS PRINCIPALES**

**CRUD de Tareas:**

Crear nuevas tareas

Marcar como completadas/incompletas

Eliminar tareas

**Interfaz Responsiva:**

Diseño adaptado con Bootstrap

Iconos intuitivos

**Persistencia de Datos:**

Almacenamiento en base de datos SQLite

Los datos persisten entre sesiones

**Feedback Visual:**

Tareas completadas aparecen tachadas

Diseño atractivo con gradientes

# **POSIBLES PROBLEMAS Y SOLUCIONES**

**Error al iniciar la aplicación:**

Verifica que todas las dependencias estén instaladas

Asegúrate de tener permisos de escritura en el directorio

**Problemas con la base de datos:**

Verifica que exista el directorio database/

Elimina el archivo tareas.db si hay errores persistentes

**La aplicación no se actualiza:**

Asegúrate de tener debug=True en app.run()

Detén y reinicia el servidor manualmente si es necesario

# **NOTAS ADICIONALES**

La aplicación usa SQLite por defecto para facilitar las pruebas

El modo debug está activado por defecto (ideal para desarrollo)

Los estilos usan Bootstrap y una fuente personalizada de Google Fonts

Los iconos son de Font Awesome (versión gratuita)
