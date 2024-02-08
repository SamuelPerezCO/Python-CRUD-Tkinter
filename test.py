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

def modifica_cuidad(Id , ISO3 , CountryName , Capital , CurrencyCode):
    cur = cnn.cursor()
    sql = f'''UPDATE countries set ISO3='{ISO3}' , CountryName = '{CountryName}' , Capital = '{Capital}' ,
    CurrencyCode = '{CurrencyCode}' WHERE Id = '{Id}'
    '''
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n
