import mysql.connector

cnn = mysql.connector.connect(host="localhost" , user="root",
passwd = "1234" , database="bdejemplopy")

def consulta_ciudades():
    cur = cnn.cursor()
    cur.execute("SELECT * FROM countries")
    datos = cur.fetchall()
    cur.close()
    cnn.close()
    return datos

def inserta_ciudad(ISO3 , CountryName , Capital , CurrencyCode):
    cur = cnn.cursor()
    sql = f'''INSERT INTO Countries(ISO3 , CountryName , Capital , CurrencyCode)
    VALUES('{ISO3}' , '{CountryName}' , '{Capital}', '{CurrencyCode}')'''
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n

def elimina_ciudad(Id):
    cur = cnn.cursor()
    sql = f'''DELETE FROM countries WHERE Id = {Id}'''
    cur.execute(sql)
    n = cur.rowcount
    cur.close()
    return n

print(elimina_ciudad(12))

dat = consulta_ciudades()

for fila in dat:
    print(fila)