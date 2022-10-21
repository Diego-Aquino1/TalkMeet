from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()


    def get_rate(self, Idrateus):
        params = {'Idrateus' : Idrateus}
        rv = self.mysql_pool.execute("SELECT * from rateus where Idrateus=%(Idrateus)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'Idrateus': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Email': result[3], 'Mensaje': result[4], 'Calificacion': result[5]}
            data.append(content)
            content = {}
        return data

    def get_rates(self):  
        rv = self.mysql_pool.execute("SELECT * from rateus")  
        data = []
        content = {}
        for result in rv:
            content = {'Idrateus': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Email': result[3], 'Mensaje': result[4], 'Calificacion': result[5]}
            data.append(content)
            content = {}
        return data

    def add_rate(self, Apellidos, Nombres, Email, Mensaje, Calificacion):    
        params = {
            'Apellidos' : Apellidos,
            'Nombres' : Nombres,
            'Email' : Email,
            'Mensaje' : Mensaje,
            'Calificacion' : Calificacion
        }
        query = """INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) 
            values (%(Apellidos)s, %(Nombres)s, %(Email)s, %(Mensaje)s, %(Calificacion)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'Idrateus': cursor.lastrowid, 'Apellidos': Apellidos, 'Nombres': Nombres, 'Email': Email, 'Mensaje': Mensaje, 'Calificacion' : Calificacion}
        return data

    def delete_rate(self, Idrateus):    
        params = {'Idrateus' : Idrateus}      
        query = """delete from rateus where Idrateus = %(Idrateus)s"""    
        self.mysql_pool.execute(query, params, commit=True) 

        data = {'result': 1}
        return data


###################################################


    def get_form(self, Idcontactus):
        params = {'Idcontactus' : Idcontactus}
        rv = self.mysql_pool.execute("SELECT * from contactus where Idcontactus=%(Idcontactus)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'Idcontactus': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Email': result[3], 'Mensaje': result[4]}
            data.append(content)
            content = {}
        return data

    def get_forms(self):  
        rv = self.mysql_pool.execute("SELECT * from contactus")  
        data = []
        content = {}
        for result in rv:
            content = {'Idcontactus': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Email': result[3], 'Mensaje': result[4]}
            data.append(content)
            content = {}
        return data

    def add_form(self, Apellidos, Nombres, Email, Mensaje):    
        params = {
            'Apellidos' : Apellidos,
            'Nombres' : Nombres,
            'Email' : Email,
            'Mensaje' : Mensaje,
        } 
        query = """INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) 
            values (%(Apellidos)s, %(Nombres)s, %(Email)s, %(Mensaje)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'Idcontactus': cursor.lastrowid, 'Apellidos': Apellidos, 'Nombres': Nombres, 'Email': Email, 'Mensaje': Mensaje}
        return data

    def delete_form(self, Idcontactus):    
        params = {'Idcontactus' : Idcontactus}      
        query = """delete from contactus where Idcontactus = %(Idcontactus)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


###################################################


    def get_guest1(self, ID):
        params = {'ID' : ID}
        rv = self.mysql_pool.execute("SELECT * from guests_h1 where ID=%(ID)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Email': result[3], 'Celular': result[4], 'Habitaciones': result[5], 'Descripcion': result[6]}
            data.append(content)
            content = {}
        return data

    def get_guests1(self):  
        rv = self.mysql_pool.execute("SELECT * from guests_h1")  
        data = []
        content = {}
        for result in rv:
            content = {'ID': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Email': result[3], 'Celular': result[4], 'Habitaciones': result[5]}
            data.append(content)
            content = {}
        return data

    def add_guest1(self, Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion):    
        params = {
            'Apellidos' : Apellidos,
            'Nombres' : Nombres,
            'Email' : Email,
            'Celular' : Celular,
            'Habitaciones' : Habitaciones,
            'Descripcion' : Descripcion,
        } 
        query = """INSERT INTO guests_h1 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) 
            values (%(Apellidos)s, %(Nombres)s, %(Email)s, %(Celular)s, %(Habitaciones)s, %(Descripcion)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'ID': cursor.lastrowid, 'Apellidos': Apellidos, 'Nombres': Nombres, 'Email': Email, 'Celular': Celular, 'Habitaciones': Habitaciones, 'Descripcion': Descripcion}
        return data

    def delete_guest1(self, ID):    
        params = {'ID' : ID}      
        query = """delete from guests_h1 where ID = %(ID)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

###################################################


if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(tm.delete_task(67))
    print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))