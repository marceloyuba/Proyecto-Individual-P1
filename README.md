
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
 <b>Analisis de Dataset Steam Australia </b>
</h2>

<p align='center'>
 <img src="scr/steam-logo-png-transparent.png" style="width: 30%;" alt="Steam Logo">
<p>

 <p style="text-align: left; border: none;">
<h3>
Steam pide que nos encarguemos de crear un sistema de recomendación de videojuegos para usuarios y se requieren funciones de filtrado(Endpoints), EDA, modelo de sentient analysis NLP y modelo de ML para terminar con un MVP.<br>
Vamos a desarrollar este informe en los <b>4 pasos mas importantes del desarrollo<b>
</h3>
</p>

 <h2 style="text-align: Left; border: none;">
    Primer Paso
</h2>
<h1>ETL y EDA</h1>
<p align='center'>
<img src ="scr\archivos.jpg">
<p>
<h3 style="text-align: left; border: none;">Se toman los 3 archivos JSON que nos fueron provistos, devido al tamaño y la complejidad de estos, lo siguiente fue convertirlos a archivos parquet, como se puede ver el el archivo <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/documentacion/ETL.ipynb">ETL</a> que se encuentra en la carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/documentacion">documentacion</a>
<br>
</h3>
<p align='center'>
<img src ="scr\archivos2.jpg">
<p>

Como se pudo ver en el <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/documentacion/ETL.ipynb">ETL</a>  de ahi creamos 3 archivos parquet, luego estos los convertimos en un archivo llamado df_merge.parquet y developer.parquet estos los almacenamos en la carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/data">data</a>, que son consumidos por las funciones y por el modelo de entrenamiento como vamos a pasar a mostrar luego.

<p style="text-align: left; border: none;">
<h3>Se hace un informe <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/documentacion/EDA.ipynb">EDA</a>, que se encuentra en la carpeta <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/tree/main/documentacion">documentacion</a>, tomando cada uno de los datasets provistos y analizando las variables de cada uno de los Endpoints, estos son:</h3><br>
<b>Developer</b> Nos muestra la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br><br>
<b>UserData</b> Observa el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br><br>
<b>User For Genre</b> Observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo. <br><br>
<b>Best Developer Year</b> Muestra el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. <br><br>
<b>Developer Reviews Analysis</b> Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave
y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados
con un análisis de sentimiento como valor positivo o negativo. <br><br>
<b>Recomendacion</b> Es el modelo de Machine Learning que observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo.
<br><br>
Para lograr los analisis, tomamos las columnas pertinentes que sean necesarias para la creacion de funciones y las analizamos individualmente y a efectos de poder ejecutar los Endpoints, se crean <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/Functions.py">funciones</a> para poder consumir los dataset y obtener las respuestas esperadas<br><br>

 <h2 style="text-align: Left; border: none;">
    Segundo Paso
</h2>
<h1>Creamos las funciones y el modelo de entrenamiento</h1>

 <h2 style="text-align: Left; border: none;">
    Tercer Paso
</h2>
<h1>Creamos un entorno virtual en FastApi</h1>
<h4>La aplicacion para el deploy elegida es FastApi, donde primero en un entorno virtual local, hacemos las comprobaciones de que las funciones ejecuten de manera correcta</h4>
</p>
<p align='center'>
<img src ="scr\fastapi.jpg" style="width: 60%;">
</p>

<p>
Para llegar a este resultado, en primer lugar creamos el entorno virtual en una carpeta separada del proyecto que se sube a Github, esto para, por error, no subir la carpeta ya que el espacio es limitado en el Push y puede fallar.<br>
Ademas cada vez que hacemos un deploy en render si falla, cancela el mismo, lo que consume mucho tiempo.
</p>
<p align='center'>
<img src ="scr\entorno.jpg" style="width: 30%;">
</p>
<p>
En este se cargan los archivos necesarios para correr la API, es una manera mas ordenada de trabajar y optimizar recursos.
</p>
<p>
Se crea un archivo <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/main.py">main.py</a> que es el que maneja el entorno de FastApi, este importa las funciondes de <a href="https://github.com/marceloyuba/Proyecto-Individual-P1/blob/main/Functions.py">Functions.py</a> donde en este archivo hacemos las consultas unicamente, dejando mas simple de leer el archivo 
</p>

<p align='center'>
<img src ="scr\enpoint.jpg" style="width: 60%;">
</p>

 <h2 style="text-align: Left; border: none;">
    Cuarto Paso
</h2>
<p>
<h1>Creamos un web service en Render</h1>
</p>