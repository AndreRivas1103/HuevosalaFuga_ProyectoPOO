class Obstaculo:
    def __init__(self, x, y, tipo_obstaculo):
        if tipo_obstaculo == "sarten":
            super().__init__(x, y, 80, 30)
            self.letal = True
        elif tipo_obstaculo == "aceite":
            super().__init__(x, y, 50, 20)
            self.letal = False
        self.tipo = tipo_obstaculo

    def efecto(self, huevo):
        if self.tipo == "sarten" and not huevo.invulnerable:
            return "muerte"
        elif self.tipo == "aceite":
            huevo.vel_x *= 1.5
            if not huevo.aterrizaje_suave:
                huevo.recibir_daño()
            return None