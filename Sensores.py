from flask import Flask, jsonify, request
import psycopg2
from datetime import datetime

URL="postgresql://hermis:SafXTy1bkJBJjBMCcoeAqWsVOa6CRA2X@dpg-d0d4vvruibrs73du1ts0-a.oregon-postgres.render.com/pokemones_x8xh"

app= Flask(__name__)

app.route("/")
def introduccion():
    return(
        "Esta es una api de mi estacion meteorologica"
    )

@app.route("/RecibirDatos", methods=["POST"])
def recibir_datos_sensores():
    data=request.get_json()
    #fecha = data.get("fecha")#La del ESP32
    fecha = datetime.now()#La de mi servidor
    temp1 = data.get("Temperatura1")
    temp2 = data.get("Temperatura2")
    Hum1 = data.get("Humedad1")
    Hum2 = data.get("Humedad2")
    dist = data.get("Distancia")

    conn = psycopg2.connect(URL)
    cursor= conn.cursor()

    cursor.execute(
    "INSERT INTO Sensores1(fecha,Temperatura1, Temperatura2, Humedad1, Humedad2, Distancia) VALUES (%s,%s,%s,%s,%s,%s)", (fecha, temp1,temp2,Hum1,Hum2,dist))
    conn.commit()
    cursor.close()
    conn.close()
    return "Dato recibido"

if __name__=="__main__":
    app.run()