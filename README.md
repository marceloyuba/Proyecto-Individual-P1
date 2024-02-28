

<p align='center'>
<img src ="scr\HenryLogo.jpg">
<p>


<p align='center'>
<h2 style="text-align: center; border: none;">
 Proyecto integrador de Machine Learning y Endpoint en Fastapi
</h2>




 <h3 style="text-align: center; border: none;">
    Alumno Marcelo Yuba
</h3>




<h2 style="text-align: center; border: none;">
 <b>Análisis de Dataset Steam Australia </b>
</h2>


<p align='center'>
 <img src="scr/steam-logo-png-transparent.png" style="width: 30%;" alt="Steam Logo">
<p>


 <p style="text-align: left; border: none;">
<h3>
Steam pide que nos encarguemos de crear un sistema de recomendación de videojuegos para usuarios y se requieren funciones de filtrado(Endpoints), EDA, modelo de sentiment analysis NLP y modelo de ML para terminar con un MVP.<br>
Vamos a desarrollar este informe en los <b>4 pasos más importantes del desarrollo<b>
</h3>
</p>


 <h2 style="text-align: Left; border: none;">
    Primer Paso
</h2>
<h1>ETL y EDA</h1>
<p align='center'>
<img src ="scr\archivos.jpg">
<p>
<h3 style="text-align: left; border: none;">Se toman los 3 archivos JSON que nos fueron provistos, devido al tamaño y la complejidad de estos, lo siguiente fue convertirlos a archivos parquet, como se puede ver el el archivo <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/analisis/ETL.ipynb">ETL</a> que se encuentra en la carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/analisis">analisis</a>
<br>
</h3>
<p align='center'>
<img src ="scr\archivos2.jpg">
<p>


Como se pudo ver en el <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/analisis/ETL.ipynb">ETL</a>  de ahi creamos 3 archivos parquet, luego estos los convertimos en un archivo llamado df_merge.parquet y developer.parquet estos los almacenamos en la carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/data">data</a>, que son consumidos por las funciones y por el modelo de entrenamiento como vamos a pasar a mostrar luego.


<p style="text-align: left; border: none;">
<h3>Se hace un informe <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/analisis/EDA.ipynb">EDA</a>, que se encuentra en la carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/analisis">analisis</a>, tomando cada uno de los datasets provistos y analizando las variables de cada uno de los Endpoints, estos son:</h3><br>
<b>Developer<b> Nos muestra la cantidad de ítems y porcentaje de contenido Free por año según empresa desarrolladora.<br><br>
<b>UserData<b> Observa el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br><br>
<b>User For Genre<b> Observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de ítems que tiene el mismo. <br><br>
<b>Best Developer Year<b> Muestra el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. <br><br>
<b>Developer Reviews Analysis<b> Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave
y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados
con un análisis de sentimiento como valor positivo o negativo. <br><br>
<b>Recomendación<b> Es el modelo de Machine Learning que observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de ítems que tiene el mismo.
<br><br>
Para lograr los analisis, tomamos las columnas pertinentes que sean necesarias para la creacion de funciones y las analizamos individualmente y a efectos de poder ejecutar los Endpoints, se crean <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/Functions.py">funciones</a> para poder consumir los dataset y obtener las respuestas esperadas<br><br>


 <h2 style="text-align: Left; border: none;">
    Segundo Paso
</h2>
<h1>Creamos un entorno virtual en FastApi</h1>
<h4>La aplicación para el deploy elegida es FastApi, donde primero en un entorno virtual local, hacemos las comprobaciones de que las funciones ejecuten de manera correcta</h4><br>
</p>
<p align='center'>
<a href="https://marcelo-yuba-pi1.onrender.com/docs"><img alt="Fastapi" src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" style="display: inline-block; width: 200px;"></a>
</p>
<p align='center'>Click en la imagen para ir al deploy en Render</p>


<p align='center'>
<img src ="scr\fastapi.jpg" style="width: 60%;">
</p>


<p>
Para llegar a este resultado, en primer lugar creamos el entorno virtual en una carpeta separada del proyecto que se sube a Github, esto para, por error, no subir la carpeta ya que el espacio es limitado en el Push y puede fallar.<br>
Además cada vez que hacemos un deploy en render si falla, cancela el mismo, lo que consume mucho tiempo.
</p>
<p align='center'>
<img src ="scr\entorno.jpg" style="width: 30%;">
</p>
<p>
En este se cargan los archivos necesarios para correr la API, es una manera más ordenada de trabajar y optimizar recursos.
</p>
<p>
Se crea un archivo <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/main.py">main.py</a> que es el que maneja el entorno de FastApi, este importa las funciones de <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/Functions.py">Functions.py</a> donde en este archivo hacemos las consultas unicamente, dejando mas simple de leer el archivo
</p>


<p align='center'>
<img src ="scr\enpoint.jpg" style="width: 60%;">
</p>


 <h2 style="text-align: Left; border: none;">
    Tercer Paso
</h2>
<p>
<h1>Creamos un web service en Render</h1>
</p>
<h4>La aplicación para el deploy en la nube elegida es Render, lugar donde se pueden hacer las consultas definitivas</h4><br>
<p align='center'>
<a href="https://marcelo-yuba-pi1.onrender.com"><img alt="Fastapi" src="https://intellyx.com/wp-content/uploads/2019/08/Render-cloud-intellyx-BC-logo.png" style="display: inline-block; width: 300px;"></a>
</p>
<p align='center'>Click en la imagen para ir al deploy en Render</p>
<p align='center'>
<img src ="scr\render.jpg" style="width: 60%;">
</p>
<h4>Se crea una página de inicio donde se puede ingresar a la API o a este repositorio</h4><br>
<p align='center'>
<img src ="scr\home.jpg" style="width: 60%;">
</p>
<h4>La metodología de uso es la misma que en el deploy local, dentro de cada endpoint hay instrucciones de como usar cada uno y una lista de sugerencias para probarlos.</h4><br>
<p align='center'>
<img src ="scr\consultas.jpg" style="width: 60%;">
</p>


 <h2 style="text-align: Left; border: none;">
    Cuarto Paso
</h2>
<p>
<h1>Creamos un video explicando el funcionamiento del deploy y el proyecto en sí</h1>
<p align='center'>
<a href="https://drive.google.com/drive/folders/11dskMeZRd7JQwkoNWF0th1oVGVPE9L4B?usp=drive_link"><img alt="Fastapi" src="https://logowik.com/content/uploads/images/google-drive-new9328.logowik.com.webp" style="display: inline-block; width: 300px;"></a>
</p>
<p align='center'>Click en la imagen para ir al drive del video</p>


 <h2 style="text-align: Left; border: none;">
    Aclaraciones
</h2>
<p>
<h1>Explicación GitHub</h1>
<p align='center'>
<img src ="scr\github.jpg" style="width: 60%;">
</p>
<p style="text-align: left; border: none;">
<h3>Como vemos la primer carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/analisis">analisis</a>, contiene los informes <b>EDA<b> y <b>ETL<b> </h3>
<h3>La segunda carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/data">data</a>, contiene los datasets necearios para el funcionamiento de la API</h3>
<h3>La tercer carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/scr">scr</a>, contiene las imagenes usadas en este README</h3>
<a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/.gitignore"><b>.gitignore</b> </a> es un archivo de uso interno de Git que nos permite usar archivos en nuestra computadora, pero, ser ignorados para subir al repositorio (git push), ya que lo que tenemos local funciona en sincronía con lo que se encuentra online<br><br>
<a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/Functions.py"><b>Functions.py</b></a> Es el archivo que contiene las funciones para las consultas, se mantiene en el main para que pueda operar de mejor manera la API.<br><br>
<a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/README.md"><b>README.md</b></a> Es el archivo que estamos leyendo en este momento, este tipo de archivo sirve para hacer explicaciones y presentaciones del repositorio. <br><br>
<a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/main.py">main.py</a> Es el archivo que hace que FastApi para pueda funcionar, donde colecciona las funciones y hace el deploy. <br><br>
<a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/render.yaml"><b>render.yaml</b></a> Archivo de procesamiento de render que hace la conexión entre el repositorio y la nube. <br><br>
<a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/requirements.txt"><b>requirements.txt</b></a> Carga las librerías de python y FastApi necesarias para poder correr el deploy en Render  .<br><br>
