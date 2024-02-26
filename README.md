
<p align='center'>
<img src ="scr\HenryLogo.jpg">
<p>

<p style="text-align: left; border: none;">
<h2 style="text-align: center; border: none;">
 Proyecto integrador de Machine Learning y Endpoint en Fastapi
</h2>
</p>
<p style="text-align: left; border: none;">
 <h3 style="text-align: center; border: none;">
    Alumno Marcelo Yuba
</h3>
</p>
<p style="text-align: left; border: none;">
<h2 style="text-align: center; border: none;">
 <b>Analisis de Dataset Steam Australia </b>
</h2>
</p>
<p align='center'>
 <img src="scr/steam-logo-png-transparent.png" style="width: 30%;" alt="Steam Logo">
<p>

 <p style="text-align: left; border: none;">
Steam pide que te encargues de crear un sistema de recomendación de videojuegos para usuarios Se requieren funciones de filtrado(Endpoints), EDA, modelo de sentient analysis NLP y modelo de ML.<br>
</p>

 <h3 style="text-align: Left; border: none;">
    Primer Paso
</h3>
<p align='center'>
<img src ="scr\archivos.jpg">
<p>
<h3 style="text-align: left; border: none;">
Se toman los 3 archivos JSON que nos fueron provistos, devido al tamaño y la complejidad de estos, lo siguiente fue convertirlos a archivos parquet, como se puede ver el el archivo ETL que se encuentra en la carpeta principal<br>
</h3>
<p align='center'>
<img src ="scr\archivos2.jpg">
<p>
<p style="text-align: left; border: none;">
<h3>Se hace un informe EDA, que se encuentra en la carpeta principal, tomando cada uno de los Endpoints solicitados y analizando las variables de cada uno, estos son:</h3><br>
<b>Developer</b> Nos muestra la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br><br>
<b>UserData</b> Observa el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br><br>
<b>User For Genre</b> Observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo. <br><br>
<b>Best Developer Year</b> Muestra el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. <br><br>
<b>Developer Reviews Analysis</b> Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave
y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados
con un análisis de sentimiento como valor positivo o negativo. <br><br>
<b>Recomendacion</b> Es el modelo de Machine Learning que observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo.
<br><br>
A efectos de poder ejecutar los mismos, se crean funciones para poder consumir los dataset y obtener las respuestas esperadas<br><br>

 <h3 style="text-align: Left; border: none;">
    Segundo Paso
</h3>

<h4>La aplicacion para el deploy elegida es FastApi, donde primero en un entorno virtual local, hacemos las comprobaciones de que las funciones ejecuten de manera correcta</h4>
</p>
<p align='center'>
<img src ="scr\fastapi.jpg" style="width: 60%;">
</p>

<p>
Para llegar a este resultado, en primer lugar creamos el entorno virtual en una carpeta separada del proyecto que se sube a Github, esto para, por error, no subir la carpeta ya que el espacio es limitado en el Push y puede fallar.
</p>
<p align='center'>
<img src ="scr\entorno.jpg" style="width: 20%;">
</p>
<p>
Este es una copia exacta del proyecto original, es una manera mas ordenada de trabajar y optimizar recursos.
</p>
<p>
Se crea un archivo main.py que es el que maneja el entorno de FastApi, este importa las funciondes de Functions.py, donde en este archivo hacemos las consultas unicamente, dejando mas simple de leer el archivo 
</p>

<p align='center'>
<img src ="scr\enpoint.jpg" style="width: 60%;">
</p>