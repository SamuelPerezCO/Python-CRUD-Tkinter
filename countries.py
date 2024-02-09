import mysql.connector

class Countries:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost" , user="root",
        passwd = "1234" , database="bdejemplopy")

    def __str__(self):
        datos = self.consulta_paises()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_paises(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM countries")
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def buscar_pais(self , Id):
        cur = self.cnn.cursor()
        sql = f"SELECT * FROM countries WHERE Id = '{Id}'"
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    
    def inserta_pais(self ,ISO3 , CountryName , Capital , CurrencyCode):
        cur = self.cnn.cursor()
        sql = f'''INSERT INTO Countries(ISO3 , CountryName , Capital , CurrencyCode)
        VALUES('{ISO3}' , '{CountryName}' , '{Capital}', '{CurrencyCode}')'''
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_pais(self, Id):
        cur = self.cnn.cursor()
        try:
            sql = f'''DELETE FROM countries WHERE Id = '{Id}' '''
            cur.execute(sql)
            n = cur.rowcount
            self.cnn.commit()
            cur.close()
            return n
        except Exception as e:
            print("Error al eliminar el registro:", e)
            return -1
    
    def modifica_pais(self , Id , ISO3 , CountryName , Capital , CurrencyCode):
        cur = self.cnn.cursor()
        sql = f'''UPDATE countries set ISO3='{ISO3}' , CountryName = '{CountryName}' , Capital = '{Capital}' ,
        CurrencyCode = '{CurrencyCode}' WHERE Id = '{Id}'
        '''
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

