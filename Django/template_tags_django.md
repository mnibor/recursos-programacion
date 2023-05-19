## TEMPLATE TAGS DE DJANGO

Se crean usando la combinación **{% [TEMPLATE TAG] %}**. Algunos template tags necesitan un cierre, otros no.

1. **INSERTAR URLS PROPIAS DEL SITIO:** Para insertar urls que fueron definidas en en el archivo **urls.py**

        {% url ‘[NOMBRE DE LA URL DEFINIDA EN urls.py]’ %}

2. **CREAR UN BLOQUE DE INSERCIÓN DE CODIGO:**

        {% block [NOMBRE DEL BLOQUE] %} {% endblock %}

El bloque que se inserta desde otra plantilla se debe encerrar dentro de la misma estructura:

        {% block [NOMBRE DEL BLOQUE] %}
            ...
            ...
            ...
            [código a insertar]
        {% endblock %}

3. **INSERTAR ARCHIVOS ESTATICOS DEL PROYECTO (ARCHIVOS DE IMAGEN, CSS, JS):** Se crea en la aplicación, la carpeta static y dentro el nombre de la aplicación. Luego, en el HTML, antes de los links se introduce el template tag:

        {% load static %}

Y cada link se reemplaza por:

        {% static ‘[NOMBRE DE LA APP/URL AL ELEMENTO ESTATICO]’ %}

4. **BUCLE FOR - ENDFOR:** Para recorrer una lista de registros en el frontend

        {% for [VARIABLE] in [QUERYSET QUE TRAE LOS DATOS] %}
            ...
            ...
            se utiliza dentro del bucle: [VARIABLE].[CAMPO DE LA TABLA]
        {% endfor %}

5. **SENTENCIA IF - ELSE - ENDIF:** Para ejecutar condicionales

        {% if [CONDICION] %}
            [código en el caso que se cumpla la condición]
        {% else %} (opcional)
            [código en el caso que NO se cumpla la condición]
        {% endif %}

6. **CREAR UN BLOQUE DE TEXTO ALEATORIO:**

        {% lorem %}

7. **COMENTAR UN TRAMO DEL CODIGO HTML DE UN TEMPLATE:**

        {% comment %}
            ...
            ...
            ...
        {% endcomment %}

8. **EXTENDER EL USO DE LA PLANTILLA BASE:** Cuando en los templates queremos utilizar los estilos definidos en el archivo base de nuestra aplicación, vamos a nuestro template específico y por encima de todo definimos el extends:

        {% extends 'base.html' %}

9. **INCLUIR OTROS RECURSOS HTML DEFINIDOS:** Cuando separamos partes de nuestra página, en otros archivos html más específicos, podemos incorporarlos a la plantilla que deseemos personalizar, utilizando el template tag include:

        {% include 'footer.html' %}

10. **SEGURIDAD EN FORMULARIOS:** Para proteger los datos del formulario que enviamos

        {% csrf_token %}