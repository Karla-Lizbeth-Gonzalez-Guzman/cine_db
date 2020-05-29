from model.model import Model
from view.view import View
from datetime import date #LIBRERIA PARA LAS FECHAS 

class Controller: 
    def __init__(self): #CONSTRUCTOR 
        self.model = Model()
        self.view = View()

    def start(self): #METODO PARA INICIALIZAR EL SISTEMA 
        self.view.start()
        self.main_menu()

    # +++++++++++++++++++++++++++ CONTROLADOR GENERAL PARA MENU PRINCIPAL +++++++++++++++++++++++++++
    def main_menu (self):
        o  = '0'
        while o != '7':
            self.view.main_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.pelicula_menu()
            elif o == '2':
                self.horario_menu()
            elif o == '3':
                self.sala_menu()
            elif o == '4':
                self.ticket_menu()
            elif o == '5':
                self.usuario_menu()
            elif o == '6':
                self.admin_menu()
            elif o == '7':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self,fs,vs): #ACTUALIZACIONES, QUITA LOS CAMPOS EN LOS QUE NO SE QUIERA MODIFICAR ALGO (STRING VACIO) 
        fields = []
        vals = []
        for f,v in zip(fs,vs): #UNE EL VALOR DE CADA UNA DE LAS LISTAS 
            if(v!= ''):
                fields.append(f + ' = %s')
                vals.append(v)
        return fields, vals
    
    # ++++++++++++++++++++++++++++ CONTROLADOR PARA USUARIOS ++++++++++++++++++++++++++++
    def usuario_menu(self):
        o = '0'
        while(o != '7'):
            self.view.usuario_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_usuario()
            elif(o == '2'):
                self.read_a_usuario()
            elif(o == '3'):
                self.read_all_usuario()
            elif(o == '4'):
                self.read_usuario_nombre()
            elif(o == '5'):
                self.update_usuario()
            elif(o == '6'):
                self.delete_usuario()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_usuario(self): #PREGUNTA LA INFORMACION 
        self.view.ask('NOMBRE: ')
        Nombre = input()
        self.view.ask('APELLIDO PATERNO: ')
        Apellido_Paterno = input()
        self.view.ask('APELLIDO MATERNO: ')
        Apellido_Materno = input()
        self.view.ask('CORREO ELECTRONICO: ')
        Correo_Electronico = input()
        self.view.ask('CONTRASENIA: ')
        Contrasenia =  input()
        return [Nombre,Apellido_Paterno,Apellido_Materno,Correo_Electronico,Contrasenia]

    def create_usuario(self): #RECIBE LA INFORMACION (SE CREA)
        Nombre, Apellido_Paterno, Apellido_Materno,Correo_Electronico,Contrasenia = self.ask_usuario()
        out = self.model.create_usuario(Nombre, Apellido_Paterno, Apellido_Materno,Correo_Electronico,Contrasenia) #EJECUTAR LAS OPERACIONES 
        if out == True:
            self.view.ok(Nombre+' '+Apellido_Paterno+' '+Apellido_Materno, 'AGREGO')
        else: 
            self.view.error('NO SE PUDO AGREGAR EL USUARIO')
        return
    
    def read_a_usuario(self):
        self.view.ask('ID USUARIO: ')
        ID_Usuario = input()
        usuario = self.model.read_a_usuario(ID_Usuario)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' DATOS DEL USUARIO ' +ID_Usuario+ ' ')
            self.view.show_a_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('ERROR AL LEER EL USUARIO')
        return

    def read_all_usuario(self):
        usuario = self.model.read_all_usuario()
        if type(usuario) == list:
            self.view.show_usuario_header(' TODOS LOS USUARIOS ')
            for usuario in usuario:
                self.view.show_a_usuario(usuario)
                self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            self.view.error('ERROR AL LEER EL USUARIO') 
        return
    
    def read_usuario_nombre(self):
        self.view.ask('USUARIO A BUSCAR: ')
        nombre = input()
        usuario = self.model.read_usuario_nombre(nombre)
        if type(usuario) == list:
            self.view.show_usuario_header(' Usuario ' +nombre+ ' ')
            for usuario in usuario:
                self.view.show_a_usuario(usuario)
                self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            self.view.error('ERROR AL LEER EL USUARIO') 
        return
    
    def update_usuario(self):
        self.view.ask('ID DEL USUARIO A MODIFICAR: ')
        ID_Usuario = input()
        usuario = self.model.read_a_usuario(ID_Usuario)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' DATOS DEL USUARIO ' +ID_Usuario+ ' ')
            self.view.show_a_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('ERROR AL LEER EL USUARIO')
            return
        self.view.msg('INGRESA LOS VALORES A MODIFICAR (VACIO PARA DEJARLO IGUAL):')
        whole_vals = self.ask_usuario()
        fields, vals = self.update_lists(['Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Correo_Electronico', 'Contrasenia'], whole_vals)
        vals.append(ID_Usuario)
        vals = tuple(vals)
        out = self.model.update_usuario(fields, vals)
        if out == True:
            self.view.ok(ID_Usuario, 'ACTUALIZO')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO')
        return
    
    def delete_usuario(self):
        self.view.ask('ID DEL USUARIO A BORRAR: ')
        ID_Usuario = input()
        count = self.model.delete_usuario(ID_Usuario)
        if count != 0:
            self.view.ok(ID_Usuario, 'BORRO')
        else: 
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('ERROR AL BORRAR EL USUARIO')
        return
    
    # ++++++++++++++++++++++++++++ CONTROLADOR PARA ADMINISTRADORES ++++++++++++++++++++++++++++
    def  admin_menu (self):
        o = '0'
        while(o != '7'):
            self.view.admin_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_admin()
            elif(o == '2'):
                self.read_a_admin()
            elif(o == '3'):
                self.read_all_admin()
            elif(o == '4'):
                self.read_admin_nombre()
            elif(o == '5'):
                self.update_admin()
            elif(o == '6'):
                self.delete_admin()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_admin(self): 
        self.view.ask('CONTRASENIA: ')
        Contrasenia =  input()
        self.view.ask('NOMBRE: ')
        Nombre = input()
        self.view.ask('APELLIDO PATERNO: ')
        Apellido_Paterno = input()
        self.view.ask('APELLIDO MATERNO: ')
        Apellido_Materno = input()
        self.view.ask('PUESTO: ')
        Puesto = input()
        return [Contrasenia,Nombre,Apellido_Paterno,Apellido_Materno,Puesto]

    def create_admin(self): 
        Contrasenia,Nombre,Apellido_Paterno,Apellido_Materno,Puesto = self.ask_admin()
        out = self.model.create_usuario(Contrasenia,Nombre,Apellido_Paterno,Apellido_Materno,Puesto) 
        if out == True:
            self.view.ok(Nombre+' '+Apellido_Paterno+' '+Apellido_Materno, 'AGREGO')
        else: 
            self.view.error('NO SE PUDO AGREGAR EL ADMINISTRADOR')
        return
    
    def read_a_admin(self):
        self.view.ask('ID ADMINISTRADOR: ')
        ID_Administrador = input()
        admin = self.model.read_a_admin(ID_Administrador)
        if type(admin) == tuple:
            self.view.show_admin_header(' DATOS DEL ADMINISTRADOR ' +ID_Administrador+ ' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('ERROR AL LEER EL ADMINISTRADOR')
        return

    def read_all_admin(self):
        admin = self.model.read_all_admin()
        if type(admin) == list:
            self.view.show_admin_header(' TODOS LOS ADMINISTRADORES ')
            for admin in admin:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('ERROR AL LEER EL ADMINISTRADOR') 
        return
    
    def read_admin_nombre(self):
        self.view.ask('ADMINISTRADOR A BUSCAR: ')
        nombre = input()
        admin = self.model.read_admin_nombre(nombre)
        if type(admin) == list:
            self.view.show_admin_header(' Administrador ' +nombre+ ' ')
            for admin in admin:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('ERROR AL LEER EL ADMINISTRADOR') 
        return

    def update_admin(self):
        self.view.ask('ID DEL ADMINISTRADOR A MODIFICAR: ')
        ID_Administrador = input()
        admin = self.model.read_a_admin(ID_Administrador)
        if type(admin) == tuple:
            self.view.show_admin_header(' DATOS DEL ADMINISTRADOR ' +ID_Administrador+ ' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('ERROR AL LEER EL ADMINISTRADOR')
            return
        self.view.msg('INGRESA LOS VALORES A MODIFICAR (VACIO PARA DEJARLO IGUAL):')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['Contrasenia', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Puesto'], whole_vals)
        vals.append(ID_Administrador)
        vals = tuple(vals)
        out = self.model.update_admin(fields, vals)
        if out == True:
            self.view.ok(ID_Administrador, 'ACTUALIZO')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR')
        return
    
    def delete_admin(self):
        self.view.ask('ID DEL ADMINISTRADOR A BORRAR: ')
        ID_Administrador = input()
        count = self.model.delete_admin(ID_Administrador)
        if count != 0:
            self.view.ok(ID_Administrador, 'BORRO')
        else: 
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('ERROR AL BORRAR EL ADMINISTRADOR')
        return
    
    # ++++++++++++++++++++++++++++ CONTROLADOR PARA PELICULAS ++++++++++++++++++++++++++++
    def pelicula_menu (self):
        o = '0'
        while(o != '7'):
            self.view.pelicula_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_pelicula()
            elif(o == '2'):
                self.read_a_pelicula()
            elif(o == '3'):
                self.read_all_pelicula()
            elif(o == '4'):
                self.read_pelicula_nombre()
            elif(o == '5'):
                self.update_pelicula()
            elif(o == '6'):
                self.delete_pelicula()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_pelicula(self):
        self.view.ask('NOMBRE: ')
        Nombre = input() 
        self.view.ask('CLASIFICACION: ')
        Clasificacion =  input()
        self.view.ask('DURACION: ')
        Duracion = input()
        self.view.ask('GENERO: ')
        Genero = input()
        self.view.ask('SINOPSIS: ')
        Sinopsis = input()
        return [Nombre,Clasificacion,Duracion,Genero,Sinopsis]

    def create_pelicula(self): 
        Nombre,Clasificacion,Duracion,Genero,Sinopsis = self.ask_pelicula()
        out = self.model.create_pelicula(Nombre,Clasificacion,Duracion,Genero,Sinopsis) 
        if out == True:
            self.view.ok(Nombre, 'AGREGO')
        else: 
            self.view.error('NO SE PUDO AGREGAR LA PELICULA')
        return
    
    def read_a_pelicula(self):
        self.view.ask('ID PELICULA: ')
        ID_Pelicula = input()
        pelicula = self.model.read_a_pelicula(ID_Pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header('DATOS DE LA PELICULA ' +ID_Pelicula+ ' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('ERROR AL LEER LA PELICULA')
        return

    def read_all_pelicula(self):
        pelicula = self.model.read_all_pelicula()
        if type(pelicula) == list:
            self.view.show_pelicula_header(' TODAS LAS PELICULAS ')
            for pelicula in pelicula:
                self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('ERROR AL LEER LA PELICULA') 
        return
    
    def read_pelicula_nombre(self):
        self.view.ask('PELICULA A BUSCAR: ')
        nombre = input()
        pelicula = self.model.read_pelicula_nombre(nombre)
        if type(pelicula) == list:
            self.view.show_pelicula_header('Pelicula' +nombre+ ' ')
            for pelicula in pelicula:
                self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('ERROR AL LEER LA PELICULA') 
        return

    def update_pelicula(self):
        self.view.ask('ID DE LA PELICULA A MODIFICAR: ')
        ID_Pelicula = input()
        pelicula = self.model.read_a_pelicula(ID_Pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' DATOS DE LA PELICULA ' +ID_Pelicula+ ' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('ERROR AL LEER LA PELICULA')
            return
        self.view.msg('INGRESA LOS VALORES A MODIFICAR (VACIO PARA DEJARLO IGUAL):')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['Nombre', 'Clasificacion', 'Duracion', 'Genero', 'Sinopsis'], whole_vals)
        vals.append(ID_Pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields, vals)
        if out == True:
            self.view.ok(ID_Pelicula, 'ACTUALIZO')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA')
        return
    
    def delete_pelicula(self):
        self.view.ask('ID DE LA PELICULA A BORRAR: ')
        ID_Pelicula = input()
        count = self.model.delete_pelicula(ID_Pelicula)
        if count != 0:
            self.view.ok(ID_Pelicula, 'BORRO')
        else: 
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('ERROR AL BORRAR LA PELICULA')
        return
    
    # ++++++++++++++++++++++++++++ CONTROLADOR PARA HORARIOS ++++++++++++++++++++++++++++
    def horario_menu (self):
        o = '0'
        while(o != '6'):
            self.view.horario_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_horario()
            elif(o == '2'):
                self.read_a_horario()
            elif(o == '3'):
                self.read_all_horario()
            elif(o == '4'):
                self.update_horario()
            elif(o == '5'):
                self.delete_horario()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_horario(self):
        self.view.ask('ID PELICULA: ')
        ID_Pelicula = input() 
        self.view.ask('HORA: ')
        Hora = input() 
        self.view.ask('FECHA: ')
        Fecha =  input()
        return [ID_Pelicula, Hora, Fecha]

    def create_horario(self): 
        ID_Pelicula, Hora, Fecha = self.ask_horario()
        out = self.model.create_horario(ID_Pelicula, Hora, Fecha) 
        if out == True:
            self.view.ok(Hora, 'AGREGO')
        else: 
            self.view.error('NO SE PUDO AGREGAR EL HORARIO')
        return
    
    def read_a_horario(self):
        self.view.ask('ID HORARIO: ')
        ID_Horario = input()
        horario = self.model.read_a_horario(ID_Horario)
        if type(horario) == tuple:
            self.view.show_horario_header('DATOS DEL HORARIO ' +ID_Horario+ ' ')
            self.view.show_a_horario(horario)
            self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            if horario == None:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('ERROR AL LEER EL HORARIO')
        return

    def read_all_horario(self):
        horario = self.model.read_all_horario()
        if type(horario) == list:
            self.view.show_horario_header(' TODOS LOS HORARIOS ')
            for horario in horario:
                self.view.show_a_horario(horario)
            self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            self.view.error('ERROR AL LEER EL HORARIO') 
        return

    def update_horario(self):
        self.view.ask('ID DEL HORARIO A MODIFICAR: ')
        ID_Horario = input()
        horario = self.model.read_a_horario(ID_Horario)
        if type(horario) == tuple:
            self.view.show_horario_header(' DATOS DEL HORARIO ' +ID_Horario+ ' ')
            self.view.show_a_horario(horario)
            self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            if horario == None:
                self.view.error('LA HORA NO EXISTE')
            else:
                self.view.error('ERROR AL LEER LA HORA')
            return
        self.view.msg('INGRESA LOS VALORES A MODIFICAR (VACIO PARA DEJARLO IGUAL):')
        whole_vals = self.ask_horario()
        fields, vals = self.update_lists(['Hora', 'Fecha'], whole_vals)
        vals.append(ID_Horario)
        vals = tuple(vals)
        out = self.model.update_horario(fields, vals)
        if out == True:
            self.view.ok(ID_Horario, 'ACTUALIZO')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR LA HORA')
        return
    
    def delete_horario(self):
        self.view.ask('ID DEL HORARIO A BORRAR: ')
        ID_Horario = input()
        count = self.model.delete_horario(ID_Horario)
        if count != 0:
            self.view.ok(ID_Horario, 'BORRO')
        else: 
            if count == 0:
                self.view.error('LA HORA NO EXISTE')
            else:
                self.view.error('ERROR AL BORRAR LA HORA')
        return
    
    # ++++++++++++++++++++++++++++ CONTROLADOR PARA SALAS ++++++++++++++++++++++++++++
    def  sala_menu (self):
        o = '0'
        while(o != '7'):
            self.view.sala_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_sala()
            elif(o == '2'):
               self.read_a_sala()
            elif(o == '3'):
                self.read_all_sala()
            elif(o == '4'):
                self.read_sala_numero()
            elif(o == '5'):
                self.update_sala()
            elif(o == '6'):
                self.delete_sala()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_sala(self): 
        self.view.ask('ID DE PELICULA: ')
        ID_Pelicula =  input()
        self.view.ask('NUMERO DE SALA: ')
        Numero_Sala =  input()
        self.view.ask(' TOTAL DE ASIENTOS: ')
        Total_Asientos =  input()
        self.view.ask('NUMERO DE ASIENTO: ')
        Numero_Asiento =  input()
        self.view.ask(' LETRA DE ASIENTO: ')
        Letra_Asiento =  input()
        return [ID_Pelicula,Numero_Sala, Total_Asientos, Numero_Asiento,Letra_Asiento]

    def create_sala(self): 
        ID_Pelicula, Numero_Sala, Total_Asientos, Numero_Asiento, Letra_Asiento = self.ask_sala()
        out = self.model.create_sala(ID_Pelicula, Numero_Sala, Total_Asientos, Numero_Asiento, Letra_Asiento) 
        if out == True:
            self.view.ok(Numero_Sala, 'AGREGO')
        else: 
            self.view.error('NO SE PUDO AGREGAR LA SALA')
        return 
    
    def read_a_sala(self):
        self.view.ask('ID SALA: ')
        ID_Sala = input()
        salas = self.model.read_a_sala(ID_Sala)
        if type(salas) == tuple:
            self.view.show_sala_header('DATOS DE LA SALA ' +ID_Sala+ ' ')
            self.view.show_a_sala(salas)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if salas == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('ERROR AL LEER LA SALA')
        return 

    def read_all_sala(self):
        salas = self.model.read_all_sala()
        if type(salas) == list:
            self.view.show_sala_header(' TODAS LAS SALAS ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('ERROR AL LEER LA SALA') 
        return
    
    def read_sala_numero(self):
        self.view.ask('SALA A BUSCAR: ')
        numero = input()
        salas = self.model.read_sala_numero(numero)
        if type(salas) == list:
            self.view.show_sala_header(' SALA' +numero+ ' ')
            for sala in sala:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('ERROR AL LEER LA SALA') 
        return

    def update_sala(self):
        self.view.ask('ID DE LA SALA A MODIFICAR: ')
        ID_Sala= input()
        salas = self.model.read_a_sala(ID_Sala)
        if type(salas) == tuple:
            self.view.show_sala_header(' DATOS DE LA SALA ' +ID_Sala+ ' ')
            self.view.show_a_sala(salas)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if salas == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('ERROR AL LEER LA SALA')
            return
        self.view.msg('INGRESA LOS VALORES A MODIFICAR (VACIO PARA DEJARLO IGUAL):')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['ID_Pelicula', 'Numero_Sala', 'Total_Asientos', 'Numero_Asiento', 'Letra_Asiento'], whole_vals)
        vals.append(ID_Sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields, vals)
        if out == True:
            self.view.ok(ID_Sala, 'ACTUALIZO')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA')
        return
    
    def delete_sala(self):
        self.view.ask('ID DE LA SALA A BORRAR: ')
        ID_Sala = input()
        count = self.model.delete_sala(ID_Sala)
        if count != 0:
            self.view.ok(ID_Sala, 'BORRO')
        else: 
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('ERROR AL BORRAR LA SALA')
        return
    
    # +++++++++++++++++ MENU TICKETS ++++++++++++++++++ 
    def ticket_menu (self):
        print('\n\n')
        print('========================================================================================================')
        print('= = = = =                   ¡ ¡  E N   C O N S T R U C C I Ó N   ! !                           = = = = =')
        print('========================================================================================================')