from pyodbc import IntegrityError, ProgrammingError

from datos.conexion import Conexion
from dominio.Estudiante import Estudiante

class EstudianteDao:
    _INSERTAR ="insert into Estudiante (cedula,nombre,apellido,email,carrera,activo) values (?,?,?,?,?,?)"
    _SELECCIONAR_X_CEDULA = "select id,cedula,nombre,apellido,email,carrera,activo from Estudiante where cedula = ?"

    @classmethod
    def insertar_estudiante(cls, estudiante):
        respuesta = {"exito": False, "mensaje": ""}
        flag_exito = False
        mensaje = ""
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera, estudiante.activo)
                cursor.execute(cls._INSERTAR, datos)
                flag_exito = True
                mensaje = "INGRESO EXITOSO"
        except IntegrityError as e:
            flag_exito = False
            if e.__str__().find("Cedula") > 0:
                print("CEDULA YA INGRESADA.")
                mensaje = "cedula ya ingresada"
            elif e.__str__().find("Email") > 0:
                print("EMAIL YA INGRESADA.")
                mensaje = "email ya ingresada"
            else:
                print("ERROR DE INTEGRIDAD")
                mensaje = "Error de integridad"
        except ProgrammingError as e:
            flag_exito = False
            print("Los datos Ingresados no son del tamaño permitido")
            mensaje = "Los datos Ingresados no son del tamaño permitido"
        except Exception as e:
            flag_exito = False
            print(e)
        finally:
            respuesta["exito"] = flag_exito
            respuesta["mensaje"] = mensaje
            return respuesta

    @classmethod
    def seleccionar_por_cedula(cls,estudiante):
        persona_encontrada = None
        try:
         with Conexion.obtenerConexion() as cursor:
             datos = (estudiante.cedula,)
             resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
             persona_encontrada=resultado.fetchone()
             estudiante.email = persona_encontrada[4]
             estudiante.nombre = persona_encontrada[2]
             estudiante.apellido = persona_encontrada[3]
             estudiante.carrera = persona_encontrada[5]
             estudiante.activo = persona_encontrada[6]
             estudiante.cedula = persona_encontrada[1]
             estudiante.id = persona_encontrada[0]
        except Exception as e:
            print(e)
        finally:
            return estudiante


if __name__=='__main__':
    e1= Estudiante()
    e1.cedula='0934843339'
    e1.nombre='Juan'
    e1.apellido='Cruz'
    e1.email='jceuz@gmail.com'
    e1.carrera='ADN'
    e1.activo= True
    #EstudianteDao.insertar_estudiante(e1)
    persona_encontrada = EstudianteDao.seleccionar_por_cedula(e1)
    print(persona_encontrada)