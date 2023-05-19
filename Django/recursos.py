#############################################
# Configuraciones comunes de Django
#############################################

##########################################################################
# Incorporar la carpeta media para manejar las imagenes del sitio
##########################################################################

# PRIMER PASO: En settings.py colocar: #################################################

# Arriba de todo
import os

# Al final del archivo settings.py
# Definimos la carpeta Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# SEGUNDO PASO: En urls.py del proyecto colocar: #######################################

from django.conf import settings  # <===== Colocar esto encima de todo

urlpatterns = [
    # rutas del proyecto
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##########################################################################
# Cambiar el nombre de la sección administración por algo más lógico
##########################################################################

# En admin.py colocar encima de todo: #################################################

admin.site.site_header = 'Administración de [NOMBRE APLICACION]'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = '[APLICACION]'

##########################################################################
# Conectar Django 4.1 a una base de datos de MySQL
##########################################################################

# PRIMER PASO: instalamos la librería mysqlclient desde la terminal

pip install mysqlclient

# SEGUNDO PASO: Si estamos en Windows, instalamos un servidor de MySQL. Hay varios
# que podemos elegir. Entre ellos: XAMPP, WampServer o Laragon
# XAMPP: https://www.apachefriends.org/es/index.html
# WampServer: https://www.wampserver.com/en/
# Laragon: https://laragon.org/
# En todos los casos se descarga un ejecutable que varía en tamaño de acuerdo al que elijamos
# y su instalación es un siguiente-siguiente-siguiente
# Una vez instalado cualquiera de estos programas, debemos iniciar el servidor de MySQL y conf
# él funcionando, debemos crear la base de datos de nuestro proyecto.

# TERCER PASO: Configuramos nuestro settings.py. Es muy importante el orden que mostramos a continuación

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',       # NOMBRE DE LA BASE DE DATOS QUE CREAMOS EN EL SERVIDOR
        'USER': 'root',         # NOMBRE DE USUARIO DE MySQL
        'PASSWORD': '',         # PASSWORD DE USUARIO DE MySQL
        'HOST': 'localhost',    # DIRECCION DEL SERVIDOR DE MySQL - En nuestra PC esta dirección suele ser localhost
        'PORT': 3306,           # PUERTO QUE USA MySQL - Suele ser siempre el mismo: 3306
    }
}

# NOTA IMPORTANTE: Trabajar con una base de datos de MySQL, requiere que nuestro servidor MySQL en nuestra PC, permanezca activo.
# Generalmente, se trabaja con Sqlite3 durante el desarrollo, y a la hora de publicar el proyecto en internet, recién ahí se
# realiza la conexión final al sistema de bases de datos que tendrá el proyecto: sea MySQL o PostgreSQL

##########################################################################
# Conectar Django 4.1 a una base de datos de PostgreSQL
##########################################################################

# PRIMER PASO: instalamos la librería psycopg2 desde la terminal

pip install psycopg2

# SEGUNDO PASO: Si estamos en Windows, instalamos un servidor de PostgreSQL. En comparación a MySQL, tenemos que descargar
# desde la página oficial de PostgreSQL el instalador para windows.
# Link de descarga: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
# Una vez instalado, debemos iniciar el servidor de PostgreSQL abriendo la aplicación PgAdmin4 que se encuentra en el
# menú de inicio. Con el PgAdmin4 corriendo, creamos una base de datos nueva. Este nombre de base de datos es el que usaremos
# en el settings.py

# TERCER PASO: Configuramos nuestro settings.py. Es muy importante el orden que mostramos a continuación

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',    # DIRECCION DEL SERVIDOR DE PostgreSQL - En nuestra PC esta dirección suele ser localhost
        'PORT': 5432,           # PUERTO QUE USA PostgreSQL - Suele ser siempre el mismo: 5432
        'NAME': 'django',       # NOMBRE DE LA BASE DE DATOS QUE CREAMOS EN EL SERVIDOR
        'USER': 'postgres',     # NOMBRE DE USUARIO DE PostgreSQL - Suele ser postgres
        'PASSWORD': 'password', # PASSWORD QUE COLOCAMOS DURANTE LA INSTALACION DE PostgreSQL EN LA PC
    }
}

# NOTA IMPORTANTE: Trabajar con una base de datos de PostgreSQL, requiere que nuestra aplicación PgAdmin4, permanezca activa.
# Generalmente, se trabaja con Sqlite3 durante el desarrollo, y a la hora de publicar el proyecto en internet, recién ahí se
# realiza la conexión final al sistema de bases de datos que tendrá el proyecto: sea MySQL o PostgreSQL

##########################################################################
# Conectar Django 4.1 a una base de datos de Squlite3 VIENE POR DEFECTO
##########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

##########################################################################
# COMO USAR CKEDITOR EN NUESTROS PROYECTOS DE DJANGO
##########################################################################

# PRIMER PASO: Instalamos django-ckeditor

pip install django-ckeditor

# SEGUNDO PASO: en settings.py registrar la aplicación en INSTALLED_APPS:

INSTALLED_APPS: [
    ...
    'ckeditor',
]

# TERCER PASO: En models.py importamos ckeditor

from ckeditor.models import RichTextField

# y en los modelos donde hay campos del tipo models.TextField() reemplazamos por

body = RichTextField(blank=True, null=True)

# CUARTO PASO: Se realizan las migraciones desde la linea de comandos

python manage.py makemigrations
python manage.py migrate

##########################################################################
# COLOCAR IDIOMA ESPAÑOL COINCIDENTE CON NUESTRA ZONA HORARIA
##########################################################################

# En settings.py modificar la constante LANGUAGE_CODE

LANGUAGE_CODE = 'es-ar'

# en la constante TIME_ZONE colocar la ciudad en la que nos encontramos

TIME_ZONE = 'America/Buenos_Aires'
