from mysql import connector 

class Model:
# ++++++++++++++++++++++++++++++++ MODELO DE DATOS MYSQL PARA CINE_DB ++++++++++++++++++++++++++++++++++
    #CONSTRUCTOR DE LA CLASE, DONDE CONTIEN EL ARCHIVO DE CONFIGURACION PARA CONECTAR LA BD 
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    #DICCIONARIO PARA LEER EL ARCHIVO DE CONFIGURACION 
    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
            return d

    #CONECCION PARA LA BD 
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    #FUNCION PARA CERRAR EL CONECTOR DE LA BD 
    def close_db(self):
        self.cnx.close()
    
    # ++++++++++++++++++++++++ METODO USUARIO ++++++++++++++++++++++++ 
    def create_usuario(self, Nombre, Apellido_Paterno, Apellido_Materno, Correo_Electronico, Contrasenia): #CREAR
        try:
            sql = 'INSERT INTO Usuarios (`Nombre`, `Apellido_Paterno`, `Apellido_Materno`, `Correo_Electronico`, `Contrasenia`) VALUES (%s, %s, %s, %s, %s)'
            vals = (Nombre, Apellido_Paterno, Apellido_Materno, Correo_Electronico, Contrasenia)
            self.cursor.execute(sql, vals) #EJECUTAR LA INSTRUCCION 
            self.cnx.commit() #ASEGURAR/VERIFICAR QUE LOS CAMBIOS SE HICIERON 
            return True
        except connector.Error as err:
            self.cnx.rollback () #DESHACER POSIBLES CAMBIOS 
            return err

    def read_a_usuario(self, ID_Usuario): #LEER/CONSULTAR SOLO PARA UN USUARIO POR ID 
        try:
            sql =  'SELECT * FROM Usuarios WHERE ID_Usuario = %s'
            #sql = 'SELECT Usuarios.*,Usuarios.Nombre FROM Usuarios JOIN Usuarios ON Usuarios.Nombre = Usuarios.Nombre AND Usuarios.ID_Usuario = %s'
            vals = (ID_Usuario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone() #RECUPERA UN UNICO REGISTRO
            return record
        except connector.Error as err:
            return err

    def read_all_usuario(self): #CONSULTAR/LEER TODOS LOS DATOS DE ESA TABLA, HAY QUE TENER CUIDADO, PORQUE SI SON MUCHOS SE PUEDE SATURAR 
        try:
            sql = 'SELECT * FROM Usuarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_usuario_nombre(self,nombre): #CONSULTAR/LEER A UN USUARIO CON UN NOMBRE EN ESPECIFICO 
        try:
            sql = 'SELECT * FROM Usuarios WHERE Nombre = %s'
            #sql = 'SELECT Usuarios.*,Usuarios.Nombre FROM Usuarios JOIN Usuarios ON Usuarios.Nombre = Usuarios.Nombre AND Usuarios.ID_Usuario = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_usuario(self, fields, vals): #ACTUALIZAR INFORMACION DE UN CLIENTE
        try:
            sql = 'UPDATE Usuarios SET '+','.join(fields)+' WHERE ID_Usuario = %s' #USUARIO QUE SE QUIERE MODIFICAR
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_usuario(self, ID_Usuario): #BORRAR A UN USUARIOS
        try:
            sql = 'DELETE FROM Usuarios WHERE ID_Usuario= %s' #USUARIO A BORRAR 
            vals = (ID_Usuario,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount #SE RECUPERA EL NUMERO DE REGISTROS QUE FUERON MODIFICADOS 
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    # ++++++++++++++++++++++++ METODO ADMINISTRADOR ++++++++++++++++++++++++ 
    def create_admin(self, Contrasenia, Nombre, Apellido_Paterno, Apellido_Materno, Puesto):
        try:
            sql = 'INSERT INTO Administradores (`Contrasenia`, `Nombre`, `Apellido_Paterno`, `Apellido_Materno`, `Puesto`) VALUES (%s, %s, %s, %s, %s)'
            vals = (Contrasenia, Nombre, Apellido_Paterno, Apellido_Materno, Puesto)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback ()
            return err
    
    def read_a_admin(self, ID_Administrador):
        try:
            sql =  'SELECT * FROM Administradores WHERE ID_Administrador = %s'
            vals = (ID_Administrador,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admin(self):
        try:
            sql = 'SELECT * FROM Administradores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_admin_nombre(self,nombre):
        try:
            sql = 'SELECT * FROM Administradores WHERE Nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE Administradores SET '+','.join(fields)+' WHERE ID_Administrador = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_admin(self, ID_Administrador):
        try:
            sql = 'DELETE FROM Administradores WHERE ID_Administrador= %s'
            vals = (ID_Administrador,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    # ++++++++++++++++++++++++ METODO PELICULAS ++++++++++++++++++++++++ 
    def create_pelicula(self, Nombre, Clasificacion, Duracion, Genero, Sinopsis):
        try:
            sql = 'INSERT INTO Peliculas (`Nombre`, `Clasificacion`, `Duracion`, `Genero`, `Sinopsis`) VALUES (%s, %s, %s, %s, %s)'
            vals = (Nombre, Clasificacion, Duracion, Genero, Sinopsis)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback ()
            return err
    
    def read_a_pelicula(self, ID_Pelicula):
        try:
            sql =  'SELECT * FROM Peliculas WHERE ID_Pelicula = %s'
            vals = (ID_Pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_pelicula(self):
        try:
            sql = 'SELECT * FROM Peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_pelicula_nombre(self,nombre):
        try:
            sql = 'SELECT * FROM Peliculas WHERE Nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE Peliculas SET '+','.join(fields)+' WHERE ID_Pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_pelicula(self, ID_Pelicula):
        try:
            sql = 'DELETE FROM Peliculas WHERE ID_Pelicula= %s'
            vals = (ID_Pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    # ++++++++++++++++++++++++ METODO HORARIOS ++++++++++++++++++++++++ 
    def create_horario(self, ID_Pelicula, Hora, Fecha):
        try:
            sql = 'INSERT INTO Horarios (`ID_Pelicula`, `Hora`, `Fecha`) VALUES (%s, %s, %s)'
            vals = (ID_Pelicula, Hora, Fecha)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback ()
            return err
    
    def read_a_horario(self, ID_Horario):
        try:
            sql =  'SELECT * FROM Horarios WHERE ID_Horario = %s'
            vals = (ID_Horario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_horario(self): #LEER TODOS LOS HORARIOS 
        try:
            sql = 'SELECT * FROM Horarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_horario(self, fields, vals):
        try:
            sql = 'UPDATE Horarios SET '+','.join(fields)+' WHERE ID_Horario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_horario(self, ID_Horario):
        try:
            sql = 'DELETE FROM Horarios WHERE ID_Horario= %s'
            vals = (ID_Horario,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    # ++++++++++++++++++++++++ METODO SALAS ++++++++++++++++++++++++ 
    def create_sala(self, ID_Pelicula, Numero_Sala, Total_Asientos, Numero_Asiento, Letra_Asiento):
        try:
            sql = 'INSERT INTO Salas (`ID_Pelicula`, `Numero_Sala`, `Total_Asientos`, `Numero_Asiento`, `Letra_Asiento`) VALUES (%s, %s, %s, %s, %s)'
            vals = (ID_Pelicula, Numero_Sala, Total_Asientos, Numero_Asiento, Letra_Asiento)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback ()
            return err
    
    def read_a_sala(self, ID_Sala):
        try:
            sql =  'SELECT * FROM Salas WHERE ID_Sala = %s'
            vals = (ID_Sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_sala(self):
        try:
            sql = 'SELECT * FROM Salas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_sala_numero(self,numero):
        try:
            sql = 'SELECT * FROM Salas WHERE Numero = %s'
            vals = (numero,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_sala(self, fields, vals):
        try:
            sql = 'UPDATE Salas SET '+','.join(fields)+' WHERE ID_Sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_sala(self, ID_Sala):
        try:
            sql = 'DELETE FROM Salas where ID_Sala= %s'
            vals = (ID_Sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 