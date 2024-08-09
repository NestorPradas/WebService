# WebService

# Configurador de Archivos y Servicio de Subida

Este proyecto consiste en una aplicación de escritorio y un servicio web desarrollado en Python. La aplicación permite a los usuarios configurar carpetas y patrones de archivos para su posterior subida a un servidor. El servicio web procesa estas configuraciones, sube los archivos periódicamente y los organiza.

## Componentes del Proyecto

1. **Aplicación de Configuración**
2. **Servicio Web de Subida**

### 1. Aplicación de Configuración

La aplicación de configuración está desarrollada usando Tkinter y permite a los usuarios:

- Seleccionar carpetas de origen.
- Definir nombres de archivo y extensiones opcionales.
- Configurar un tiempo de espera entre subidas.
- Guardar estas configuraciones en un archivo `config.yaml`.

#### Características

- **Interfaz Moderna**: Se utiliza el estilo `clam` de Tkinter para una apariencia más moderna.
- **Edición Directa**: Los usuarios pueden editar directamente las entradas de nombre de archivo y extensión en la tabla.
- **Persistencia**: La configuración se guarda en un archivo YAML, que se carga al inicio de la aplicación.

#### Uso

1. **Instalación de Dependencias**

   Asegúrate de tener Python instalado. Las dependencias se pueden instalar con pip:
   pip install pyyaml
   
Ejecución de la Aplicación

Ejecuta el script de configuración para abrir la aplicación de interfaz gráfica:

Copiar código
python configurador.py
Uso de la Aplicación

Añade filas haciendo clic en "Añadir Fila" y seleccionando carpetas.
Edita el nombre de archivo y extensión haciendo doble clic en las celdas correspondientes.
Configura el tiempo de espera entre subidas usando el selector.
Guarda la configuración haciendo clic en "Guardar Configuración".

2. Servicio Web de Subida
El servicio web está desarrollado con Flask y se encarga de recibir y almacenar archivos. Un script de cliente sube archivos periódicamente basándose en la configuración especificada.

Características
Servicio Continuo: Ejecuta continuamente y sube archivos según las configuraciones.
Organización: Mueve archivos procesados a una subcarpeta enviados.
Flexibilidad: Usa patrones para nombres de archivo y extensiones, permitiendo el uso de comodines (*).
Uso
Instalación de Flask

Instala Flask si no lo tienes aún:

bash
Copiar código
pip install flask requests
Ejecución del Servidor

Ejecuta el servidor Flask para iniciar el servicio web:

bash
Copiar código
python server.py
Ejecución del Script de Subida

Ejecuta el script que lee las configuraciones y sube los archivos al servidor:

bash
Copiar código
python upload_service.py
Scripts
configurador.py: Interfaz gráfica para configurar carpetas y patrones de archivos.
server.py: Servidor Flask que maneja las solicitudes de subida de archivos.
upload_service.py: Script que sube archivos al servidor periódicamente basado en configuraciones.
Personalización
Puedes personalizar el proyecto modificando los scripts según tus necesidades. Cambia los estilos, añade nuevas funcionalidades o ajusta los patrones de búsqueda de archivos.

Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o pull request si tienes ideas para mejoras.

Licencia
Libre de uso
