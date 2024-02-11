from fastapi import FastAPI, File, UploadFile, HTTPException
import Functions
from Functions import *


#http://127.0.0.1:8000
#https://fastapi-app-vf4c.onrender.com

app = FastAPI()

@app.get(path='/developer',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br>
                4. Sugerencia de usuarios: Valve, Ubisoft, Capcom, Epic Games, Rockstar Games, Sega.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Consultas Developer"])

def Developer(desarrollador):
    resultadodeveloper = Functions.Developer(desarrollador)
    return resultadodeveloper
developer = Developer('Valve')
print(developer)

@app.get(path = '/userdata',
          description=""" 
    <html>
        <body>
            <h1>INSTRUCCIONES</h1>
            <h3>
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. Observe el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo.<br>
                4. Sugerencia de usuarios: BrainsAccount, 76561197970982479, UTNerd24, AVATAR715, tarjla.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Consultas de UserData"])
def UserData(User_id):
    resultado = Functions.UserData(User_id)
    return resultado
User_id = UserData('BrainsAccount')

@app.get(path='/UserForGenre',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. El usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br>
                4. Sugerencia de usuarios: Action, Strategy, Simulation, Racing.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Consultas User For Genre"])
def UserForGenre(genero_especificado):
    resultadoReview = Functions.UserForGenre(genero_especificado)
    return resultadoReview
ufg = UserForGenre('Strategy')


@app.get(path='/best_developer_year',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado<br>
                4. Ingrese un año para obtener el resultado.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Consultas Best Developer Year"])
def best_developer_year(año):
    resultadoReview = Functions.best_developer_year(año)
    return resultadoReview

años = best_developer_year(2005)
print(años)

@app.get(path='/developer_reviews_analysis',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave<br>
                   y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados<br> 
                   con un análisis de sentimiento como valor positivo o negativo.<br>
                4. Sugerencia de usuarios: Valve, Ubisoft, Capcom, Epic Games, Rockstar Games.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Consultas Developer Reviews Analysis"])
def developer_reviews_analysis(desarrolladora):
    resultadoReview = Functions.developer_reviews_analysis(desarrolladora)
    return resultadoReview
dra = developer_reviews_analysis('Valve')

@app.get(path = '/Recomendacion',
          description=""" 
    <html>
        <body>
            <h1>INSTRUCCIONES</h1>
            <h3>
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. Observe el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo.<br>
                4. Sugerencia de usuarios: obscenedagger, rrbr, howsitgoinaz, halofan360, mailiam123, neochuah94, fui312<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Recomendacion"])
def recomendacion_usuario(id_de_usuario):
    resultadotop_game = Functions.recomendacion_usuario(id_de_usuario)
    return resultadotop_game
dra = recomendacion_usuario('obscenedagger')