class View:
    # +++++++++++++++++++++ VISTA PARA CINE_DB +++++++++++++++++++++
    def start(self): 
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                            ¡ ¡   B I E N V E N I D O   ! !                                     = = = = = = = =')
        print('==============================================================================================================================')

    def end(self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                          ¡ ¡   V U E L V A   P R O N T O   ! !                                = = = = = = = = ')
        print('==============================================================================================================================')
        print('\n\n')    

    # +++++++++++++++++ MENU PRINCIPAL ++++++++++++++++++ 
    def main_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                                 M E N U    P R I N C I P A L                                  = = = = = = = = ')
        print('==============================================================================================================================')
        print(' 1. PELICULAS ')
        print(' 2. HORARIOS ')
        print(' 3. SALAS ')
        print(' 4. TICKETS ')
        print(' 5. USUARIOS ')
        print(' 6. ADMINISTRADOR ')
        print(' 7. SALIR ')
   
    def option(self, last):
        print('SELECCIONA UNA OPCION (1 - ' + last + '): ', end='')

    def not_valid_option(self):
        print('OPCION NO VALIDA - INTENTA DE NUEVO \n')
    
    def ask(self, output): #PREGUNTA ALGO 
        print(output, end='')
    
    def msg(self,output): #MUESTRA RESULTADO EN PANTALLA SIN TENER ALGO DE ENTRADA 
        print(output)

    def ok(self, id, op): #LA OPERACION SE REALIZO BIEN 
        print('+' *(len(str(id))+len(op)+24))
        print('+ ¡' +str(id)+ ' SE ' +op+ ' CORRECTAMENTE! + ')
        print('+' *(len(str(id))+len(op)+24))

    def error(self,err): #LA OPERACION NO SE PUDO REALIZAR 
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- ' +err+ ' -')
        print('-' *(len(err)+4))
    
    # +++++++++++++++++ MENU USUARIO ++++++++++++++++++ 
    def usuario_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                                  M E N U    U S U A R I O S                                   = = = = = = = = ')
        print('==============================================================================================================================')
        print(' 1. AGREGAR USUARIO ')
        print(' 2. LEER USUARIO POR ID')
        print(' 3. LEER TOOS LOS USUARIOS ')
        print(' 4. LEER USUARIO POR NOMBRE ')
        print(' 5. ACTUALIZAR USUARIO ')
        print(' 6. BORRAR USUARIO ')
        print(' 7. REGRESAR ')
    
    def show_a_usuario(self, record): #PARTE CENTRAL DE LOS DATOS 
        print('ID:', record[0])
        print('NOMBRE:', record[1])
        print('APELLIDO PATERNO:', record[2])
        print('APELLIDO MATERNO:', record[3])
        print('CORREO ELECTRONICO:', record[4])
        print('CONTRASENIA:', record[5])

    def show_a_usuario_brief(self, record): #SE PASAN LOS REGISTROS DEL USUARIO 
        print('ID:', record[0])
        print('NOMBRE:', record[1]+' '+record[2]+' '+record[3]) #SE JUNTA EL NOMBRE Y APELLIDOS DEL USUARIO 
        print('CORREO ELECTRONICO:', record[4])
        print('CONTRASENIA:', record[5])

    def show_usuario_header(self, header): #CABEZERA QUE MUESTRA EL INICIO DE LA INFORMAION 
        print(header.center(180,'*'))
        print('-'*180)

    def show_usuario_midder(self): #SEPARADOR INTERMEDIO
        print('-'*180)
    
    def show_usuario_footer(self): #PIE DE TEXTO PARA INDICAR QUE LA INFORMACION FINALIZO 
        print('*'*180)
    
    # +++++++++++++++++ MENU ADMINISTRADOR ++++++++++++++++++ 
    def admin_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                           M E N U    A D M I N I S T R A D O R E S                            = = = = = = = = ')
        print('==============================================================================================================================')
        print(' 1. AGREGAR ADMINISTRADOR ')
        print(' 2. LEER ADMINISTRADOR POR ID ')
        print(' 3. LEER TOOS LOS ADMINISTRADORES ')
        print(' 4. LEER ADMINISTRADOR POR NOMBRE ')
        print(' 5. ACTUALIZAR ADMINISTRADOR ')
        print(' 6. BORRAR ADMINISTRADOR ')
        print(' 7. REGRESAR ')
    
    def show_a_admin(self, record): 
        print('ID:', record[0])
        print('NOMBRE:', record[2])
        print('APELLIDO PATERNO:', record[3])
        print('APELLIDO MATERNO:', record[4])
        print('PUESTO:', record[5])
        print('CONTRASENIA:', record[1])

    def show_a_admin_brief(self, record): 
        print('ID:', record[0])
        print('NOMBRE:', record[2]+' '+record[3]+' '+record[4]) 
        print('PUESTO:', record[5])
        print('CONTRASENIA:', record[1])

    def show_admin_header(self, header): 
        print(header.center(180,'*'))
        print('-'*180)

    def show_admin_midder(self): 
        print('-'*180)
    
    def show_admin_footer(self):  
        print('*'*180)
    
    # +++++++++++++++++ MENU PELICULAS ++++++++++++++++++ 
    def pelicula_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                                M E N U     P E L I C U L A S                                  = = = = = = = = ')
        print('==============================================================================================================================')
        print(' 1. AGREGAR PELICULA ')
        print(' 2. LEER PELICULA POR ID ')
        print(' 3. LEER TODAS LAS PELICULAS ')
        print(' 4. LEER PELICULA POR NOMBRE ')
        print(' 5. ACTUALIZAR PELICULA ')
        print(' 6. BORRAR PELICULA ')
        print(' 7. REGRESAR ')

    def show_a_pelicula(self,record):
        print('ID:',record[0])
        print('NOMBRE:',record[1])
        print('CLASIFICACION:',record[2])
        print('DURACION:',record[3])
        print('GENERO:',record[4])
        print('SINOPSIS:',record[5])
    
    def show_a_pelicula_brief(self, record): 
        print('ID:', record[0])
        print('NOMBRE:', record[1])
        print('CLASIFICACION:', record[2]+' '+record[3]+' '+record[4]) 
        print('SINOPSIS:', record[5])

    def show_pelicula_header(self, header): 
        print(header.center(180,'*'))
        print('-'*180)

    def show_pelicula_midder(self):
        print('-'*180)
    
    def show_pelicula_footer(self): 
        print('*'*180)
    
    # +++++++++++++++++ MENU HORARIOS ++++++++++++++++++ 
    def horario_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                                  M E N U     H O R A R I O S                                   = = = = = = = =')
        print('==============================================================================================================================')
        print(' 1. AGREGAR HORARIO ')
        print(' 2. LEER HORARIO POR ID')
        print(' 3. LEER TODOS LOS HORARIO ')
        print(' 4. ACTUALIZAR HORARIO ')
        print(' 5. BORRAR HORARIO ')
        print(' 6. REGRESAR ')

    def show_a_horario(self,record):
        print('ID:',record[0])
        print('ID PELICULA:',record[1])
        print('HORA:',record[2])
        print('FECHA:',record[3])
        
    def show_a_horario_brief(self, record): 
        print('ID:', record[0])
        print('ID PELICULA:', record[1]+' '+record[2]+' '+record[3])

    def show_horario_header(self, header): 
        print(header.center(180,'*'))
        print('-'*180)

    def show_horario_midder(self):
        print('-'*180)
    
    def show_horario_footer(self): 
        print('*'*180)
    
    # +++++++++++++++++ MENU SALAS ++++++++++++++++++ 
    def sala_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                                     M E N U    S A L A S                                      = = = = = = = = ')
        print('==============================================================================================================================')
        print(' 1. AGREGAR SALA ')
        print(' 2. LEER SALA POR ID')
        print(' 3. LEER TODAS LAS SALAS ')
        print(' 4. LEER SALA POR NUMERO ')
        print(' 5. ACTUALIZAR SALA ')
        print(' 6. BORRAR SALA ')
        print(' 7. REGRESAR ')

    def show_a_sala(self,record):
        print('ID:',record[0])
        print('ID PELICULA:',record[1])
        print('NUMERO DE SALA:',record[2])
        print('TOTAL DE ASIENTOS:',record[3])
        print('NUMERO DE ASIENTO:',record[4])
        print('LETRA DE ASIENTO:',record[5])
        
    def show_a_sala_brief(self, record): 
        print('ID:', record[0])
        print('ID PELICULA:',record[1])
        print('NUMERO DE SALA:', record[2]+' '+record[3]+' '+record[4]+' '+record[5]) 

    def show_sala_header(self, header):
        print(header.center(180,'*'))
        print('-'*180)

    def show_sala_midder(self):
        print('-'*180)

    def show_sala_footer(self):
        print('*'*180)
    
    # +++++++++++++++++ MENU TICKETS ++++++++++++++++++ 
    def ticket_menu (self):
        print('\n\n')
        print('==============================================================================================================================')
        print('= = = = = = = =                          ¡ ¡  E N     C O N S T R U C C I Ó N   ! !                           = = = = = = = = ')
        print('==============================================================================================================================')