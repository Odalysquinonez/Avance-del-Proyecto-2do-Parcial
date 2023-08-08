# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from dominio.Docente import Docente
from dominio.Estudiante import Estudiante
from dominio.Pedido import Pedido
from dominio.Revista import Revista
from dominio.Libro import Libro


if __name__ == '__main__':


    libro1 = Libro("L001", "Autor 1", "Título 1", 2022, "Editorial 1", True, 3, 1, "Tapa dura")
    libro2 = Libro("L002", "Autor 2", "Título 2", 2021, "Editorial 2", True, 2, 2, "Tapa blanda")
    libro3 = Libro("L003", "Autor 3", "Título 3", 2023, "Editorial 3", False, 0, 3, "Tapa dura")
    libro4 = Libro("L004", "Autor 4", "Título 4", 2020, "Editorial 4", True, 1, 4, "Tapa blanda")
    libro5 = Libro("L005", "Autor 5", "Título 5", 2022, "Editorial 5", True, 4, 5, "Tapa dura")

    revista1 = Revista("R001", "Autor 1", "Título 1", 2022, "Editorial 1", True, 3, 1, "Tipo 1")
    revista2 = Revista("R002", "Autor 2", "Título 2", 2021, "Editorial 2", True, 2, 2, "Tipo 2")
    revista3 = Revista("R003", "Autor 3", "Título 3", 2023, "Editorial 3", False, 0, 3, "Tipo 3")
    revista4 = Revista("R004", "Autor 4", "Título 4", 2020, "Editorial 4", True, 1, 4, "Tipo 4")
    revista5 = Revista("R005", "Autor 5", "Título 5", 2022, "Editorial 5", True, 4, 5, "Tipo 5")

    alumno1 = Estudiante("1234567890", "Juan", "Pérez", "juan@example.com", "123456789", "Calle 123", 0, True,
                         "Ingeniería", 1, "Primero")
    alumno2 = Estudiante("9876543210", "María", "Gómez", "maria@example.com", "987654321", "Avenida 456", 0, True,
                         "Ciencias", 2, "Segundo")

    docente1 = Docente("5432109876", "Pedro", "Sánchez", "pedro@example.com", "543210987", "Plaza 789", 0, True,
                       "Matemáticas", 1, "Maestría en Educación", "Doctorado en Matemáticas")
    docente2 = Docente("0123456789", "Laura", "Torres", "laura@example.com", "012345678", "Ruta 321", 0, True,
                       "Literatura", 2, "Maestría en Literatura", "Doctorado en Literatura")

    pedido1 = Pedido(alumno1, libro1, "Matemáticas", "2023-08-20")
    pedido2 = Pedido(alumno2, revista1, "Ciencias", "2023-08-20")
    pedido3 = Pedido(docente1, libro2, "Literatura", "2023-09-15")

    print(pedido3.__str__())

