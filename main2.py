import sys

from PySide6.QtWidgets import QApplication

from servicio.persona_principal import PersonaPrincipal

app = QApplication()
Vtn_principal = PersonaPrincipal()
Vtn_principal.show()
sys.exit(app.exec())