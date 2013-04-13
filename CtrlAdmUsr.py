from Usuario import Usuario, get_table 
from RolUsuario import RolUsuario, get_table 
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select

"""Controlador de Administrador de Usuario."""  
__author__ = 'Grupo 5'
__date__ = '04-04-2013'
__version__ = '1.0'
__text__ = 'Este modulo contiene funciones que permiten el control de administracion de usuarios'
__file__ = 'CtrlAdmUsr.py'      
    
engine = create_engine('postgresql+psycopg2://admin:admin@localhost/sgp')
metadata = MetaData(bind=engine)
usuario_table = get_table(metadata)
mapper(Usuario, usuario_table)
conn = engine.connect()

def getUsuarioList():
    """Funcion que retorna la lista de todos los usuarios en la base de datos."""
    s = select([usuario_table])
    result = s.execute()
    return result

def validarUsuario(username, password):
    """Funcion que retorna verdadero si el usuario y password son correctos."""
    usuarioList = getUsuarioList()
    for user in usuarioList:
        if username == user.username:
            if password == user.passwrd:
                return True
    return False

def buscarUsuario(username):
    """Funcion que retorna verdadero si el usuario se encuentra en la BD"""
    usuarioList = getUsuarioList()
    for user in usuarioList:
        if username == user.username:
            return True
    return False

def getMayorIdUsuario():
    """Funcion que retorna el mayor idusuario en la tabla usuarios"""
    lista = getUsuarioList()
    idusuariomax =0
    for user in lista:
        if idusuariomax < user.idusuario:
            idusuariomax = user.idusuario
    return idusuariomax   

def crearUsr(username,passwrd,nombre,apellido,telefono,ci):
    """Funcion que recibe los atributos de un usuario y lo periste en la base de datos."""
    idusuariomax=getMayorIdUsuario()
    result = usuario_table.insert().execute(idusuario=idusuariomax+1,
                                             username=username, 
                                             passwrd=passwrd,
                                             nombre=nombre, 
                                             apellido=apellido, 
                                             telefono=telefono, 
                                             ci=ci)

def elimUsr(iduser):
    """Funcion que recibe el Id de un Usuario y elimina de la base de datos"""
    conn.execute(usuario_table.delete().where(usuario_table.c.idusuario==iduser)) 
    
    
def modUsr(iduser,username,passwrd,nombre,apellido,telefono,ci):
    """Funcion que recibe los atributos de un usuario y lo modifica en la base de datos"""
    conn.execute(usuario_table.update().
                    where(usuario_table.c.idusuario==iduser).
                    values(username=username,
                           passwrd=passwrd,
                           nombre=nombre,
                           apellido=apellido,
                           telefono=telefono,
                           ci=ci)
                ) 
def getId(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['idusuario']
def getUsername(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['username']
def getPasswrd(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['passwrd']
def getNombre(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['nombre']
def getApellido(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['apellido']
def getTelefono(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['telefono']
def getCi(iduser):
    s = select([usuario_table],usuario_table.c.idusuario==iduser)
    result = conn.execute(s)
    row = result.fetchone()
    return row['ci']

def usr(iduser):
    """Funcion que recibe el Id de un Usuario y retorna el objeto usuario"""
    lista = getUsuarioList()
    for user in lista:
        if iduser == user.idusuario:
            return user