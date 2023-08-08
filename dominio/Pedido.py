# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL

from datetime import date

class Pedido:
    contador_pedido = 0

    def __init__(self, solicitante, lista_material, materia, fecha_devolucion):
        self.id = Pedido.contador_pedido + 1
        self.solicitante = solicitante
        self.lista_material = lista_material
        self.materia = materia
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = fecha_devolucion
        Pedido.contador_pedido += 1

    def get_id(self):
        return self.id

    def get_solicitante(self):
        return self.solicitante

    def set_solicitante(self, solicitante):
        self.solicitante = solicitante

    def get_lista_material(self):
        return self.lista_material

    def set_lista_material(self, lista_material):
        self.lista_material = lista_material

    def get_materia(self):
        return self.materia

    def set_materia(self, materia):
        self.materia = materia

    def get_fecha_prestamo(self):
        return self.fecha_prestamo

    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def get_fecha_devolucion(self):
        return self.fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion

    def pedir_material(self, solicitante, lista_material, materia):
        self.solicitante = solicitante
        self.lista_material = lista_material
        self.materia = materia
        self.fecha_prestamo = date.today()

    def devolver_material(self):
        self.fecha_devolucion = date.today()

    def __str__(self):
        material_nombre = self.lista_material.__class__.__name__
        return f"ID: {self.id}\nSolicitante: {self.solicitante}\nLista de material: {material_nombre}\nMateria: {self.materia}\nFecha de préstamo: {self.fecha_prestamo}\nFecha de devolución: {self.fecha_devolucion}"