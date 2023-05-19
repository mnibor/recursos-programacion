# COMANDOS PARA LINUX

Linux, en general posee más de una versión de Python instalada. Pero la que necesitamos ejecutar es la versión 3 o superiores. En varias distribuciones de linux existe la posibilidad que si hacermos un 

    python --version

nos devuelva la versión 3.x.x pero en otros casos puede devolvernos un mensaje de error. En este último caso, deberíamos hacer en la consola:

    python3 --version

y nos devolverá la versión específica que está instalada. Teniendo en cuenta esta referencia, en el resto de la presente documentación, tendremos en cuenta que la versión de python que tenemos instalada, es necesario llamarla con el comando python3

1. **CREAR UN ENTORNO VIRTUAL:** Existen varios comandos con los que podemos crear un entorno virtual sobre Windows. Quizás el más utilizado sea: 
	
		python3 -m venv [NOMBRE DEL ENTORNO] 

	Por ejemplo: 
        python3 -m venv miEntornoVirtual

2. **ACTIVAR ENTORNO VIRTUAL:** Para activar el entorno virtual en Windows, debo acceder al directorio donde se creó el entorno virtual e ingresar a la carpeta del mismo y dentro a la carpeta Scripts y allí ejecutar el archivo "activate.bat"
	
		source [NOMBRE DEL ENTORNO]\bin\activate

    Por ejemplo: 
        
        source miEntornoVirtual\bin\activate

3. **DESACTIVAR ENTORNO VIRTUAL:** Para desactivar un entorno virtual, desde la linea de comandos basta con tipear "deactivate" no importa en qué directorio nos encontremos

4. **LISTADO DE TODAS LAS LIBRERIAS INSTALADAS EN EL ENTORNO VIRTUAL:** Para averiguar qué librerías están instaladas en el entorno virtual basta con ejecutar cualquiera de estos dos comandos:

		pip list / pip freeze

5. **GENERAR UN REGISTRO DE PAQUETES DEL PROYECTO:** Es conveniente ir llevando un registro de los paquetes que va a necesitar el proyecto. Podemos hacerlo llevando un registro a mano de cada paquete y su version, pero podemos automatizarlo ejecutando el siguiente comando:

	    pip freeze > requirements.txt

Esto generará un archivo con el nombre requirements.txt en el directorio donde nos encontremos en el momento de ejecutar el comando.

6. **INSTALAR PAQUETES DEPENDIENTES A TRAVES DE UN ARCHIVO REQUIREMENTS.TXT:** Podemos instalar en un solo paso, todas las librerías que utiliza el proyecto, solamente si éste dispone de un archivo requirements.txt para eso, primero tenemos que tener activo el entorno virtual, y a continuación ejecutar:

	    pip install -r requirements.txt

7. **INSTALAR DJANGO EN EL ENTORNO VIRTUAL:** Este comando instalará la última versión de Django disponible, teniendo en cuenta la versión de Python que tengamos instalada en el sistema.
	
	    pip install django

8. **INSTALAR VERSION ESPECIFICA DE DJANGO:** Para instalar una versión específica de Django, debemos ejecutar el siguiente comando

	    pip install django==3.2

9. **AVERIGUAR VERSION DE DJANGO INSTALADA:** Existen varios caminos para averiguar la versión de Django instalada. Podemos optar por cualquiera de estos tres comandos. Los dos primeros, van a mostrar la version de Django, puntualmente. Las dos últimas, mostrarán todos los paquetes instalados, entre ellos, Django.

	    django-admin --version
	    python3 -m django --version
	    pip freeze / pip list

10. **DESINSTALAR CUALQUIER LIBRERIA DEL ENTORNO VIRTUAL (o global):** Para desinstalar cualquier librería instalada en el entorno virtual basta ejectuar el siguiente comando, con el entorno virtual activado:
	
	    pip uninstall [NOMBRE DE LA LIBRERIA]

	    Por ejemplo: pip uninstall Django 
	
11. **CREAR UN PROYECTO DE DJANGO:** Con el entorno virtual activado, basta ejecutar el siguiente comando, teniendo en cuenta que los nombres de proyecto no deben contener espacios ni guiones medios. Si acepta guiones bajos:

	    django-admin startproject [NOMBRE DEL PROYECTO]

	Por ejemplo: 
    
        django-admin startproject blogNoticias

12. **INICIAR EL PROYECTO INSTALADO:** Es necesario tener el entorno virtual activado y estar dentro de la carpeta del proyecto, donde se encuentra el archivo manage.py. Allí ejecutamos el comando:

	    python3 [NOMBRE DEL PROYECTO] runserver

	Por ejemplo: 
        
        python3 blogNoticias runserver

Este comando ejecutará un servidor de pruebas de Django donde podremos desarrollar localmente nuestro proyecto.

13. **SALIR DEL SERVIDOR FUNCIONANDO:** Para salir del servidor de pruebas de Django hay que dirigirse a la terminal o la consola de comandos donde se está ejecutando el servidor y ejecutar la secuencia de teclas:

	    CTRL + C

14. **EJECUTAR LAS MIGRACIONES DESPUES DE CREAR EL PROYECTO:** Este comando creará la tabla de usuarios del sistema
	
	    python3 manage.py migrate

15. **CREAR UNA APLICACION EN EL PROYECTO:** Para crear una aplicación ejecutamos cualquiera de los dos comandos:

	    python3 manage.py startapp [NOMBRE DE APP]

        django-admin startapp [NOMBRE DE APP]

	    Por ejemplo: python3 manage.py startapp core

Una vez creada la aplicación, hay que registrarla en el archivo settings.py en el apartado INSTALLED_APPS para que queden integradas al proyecto. Si no la registramos, Django no sabrá que existe la aplicación que creamos y todo lo que hagamos en ella, no va a impactar en el proyecto.

16. **CREAR UN SUPERUSUARIO ADMINISTRADOR:** 

	    python3 manage.py createsuperuser

Luego de ejecutar este comando, nos aparecerá la posibilidad de definir un nombre de usuario al superusuario, su correo electrónico y la contraseña con la que accederemos a la parte administrativa del sistema.

17. **EJECUTAR LAS MIGRACIONES DESPUES DE CREAR MODELOS EN UNA APLICACION:** Luego de crear una aplicación, quizás definamos modelos en dicha aplicación. Para que éstas queden alojadas en la base de datos, tenemos que ejecutar estos dos comandos de manjera secuencial:

	    python3 manage.py makemigrations [NOMBRE DE LA APLICACION]
	    python3 manage.py migrate [NOMBRE DE LA APLICACION]

En ambos casos se puede omitir el nombre de la aplicación
