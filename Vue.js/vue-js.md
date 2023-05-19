# APUNTES DE VUE.js

En este documento, vamos a explicar pasos básicos para instalar VUE Cli y los pasos para crear aplicaciones que luego integraremos con nuestras aplicaciones de Django REST Framework.

1. Se necesita primero que todo, tener instalado Node.js (https://nodejs.org/es/).
    a. En Windows, es descargar un instalable y con las opciones siguiente-siguiente-siguiente queda instalado. 

    lo que nos arrojaría la versión que quedó instalada. Se recomienda la instalación de la versión más actualizada del instalador.

    b. En Linux, la instalación de Node.js depende de la versión de linux que estemos usando. Por eso vamos a hacer un resumen, de las diferentes versiones que podemos encontrar.
    BASADAS EN DEBIAN (como ser: Debian, Unbuntu, Linux Mint): En línea de comandos tipear:

        sudo apt-get install -y nodejs npm

    FEDORA: 

        sudo dnf install nodejs npm

    OPEN SUSE:

        zypper install nodejs4

    c. Luego de la instalación, independientemente si lo hicimos en Windows o Linux, para corroborar si todo ha salido bien, en consola ejecutamos:

            node --version

    y nos debería devolver la versión de node.js que está instalada.

2. Después de tener instalado node.js podemos instalar Vue de forma global en el sistema (https://cli.vuejs.org/). Para instalar vue a nivel global, tenemos que ejecutar en la consola:

        npm install -g @vue/cli

Una vez instalado, desde la consola podemos verificar la versión instalada con el siguiente comando:

        vue --version

y nos debería devolver la versión de vue que quedó instalada en el sistema.

3. Acto seguido podemos crear un proyecto de vue. Para lo cual desde consola ejecutamos:

        vue create [NOMBRE DEL PROYECTO]

Esto nos creará una carpeta con el nombre del proyecto, y dentro, todos los archivos y carpetas que formarán parte del proyecto.