# =====================================================
# CLASE SISTEMA DE GESTIÓN
# =====================================================

class SistemaGestion:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        logging.info(
            f"Cliente agregado: {cliente.nombre}"
        )

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
        logging.info(
            f"Servicio agregado: {servicio.nombre}"
        )

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        logging.info(
            "Reserva registrada correctamente"
        )

    def mostrar_servicios(self):
        for servicio in self.servicios:
            print(servicio.descripcion())
      
      
