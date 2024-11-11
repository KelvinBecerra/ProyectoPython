class Venta:
    def __init__(self, ci_cliente, metodo_pago, metodo_envio, producto_comprado=None, cantidades=None):
        self.ci_cliente = ci_cliente  
        self.metodo_pago = metodo_pago  
        self.metodo_envio = metodo_envio  
        self.producto_comprado = producto_comprado  
        self.cantidades = cantidades  

        # Cálculos de desglose
        self.subtotal = self.calcular_subtotal()  # Subtotal de la compra
        self.descuento = self.calcular_descuento()  # Descuento aplicado si aplica
        self.iva = self.calcular_iva()  # IVA del 16%
        self.igtf = self.calcular_igtf()  # IGTF del 3% si aplica
        self.total = self.calcular_total()  # Total final de la compra

    def calcular_subtotal(self):
        subtotal = 0
        for producto, cantidad in zip(self.producto_comprado, self.cantidades):
            subtotal += producto.precio * cantidad
        return subtotal

    def calcular_descuento(self):
        # Aplica un 5% de descuento si el cliente es jurídico y paga de contado
        if self.ci_cliente.tipo == 'juridico' and self.metodo_pago == 'dolares':
            return self.subtotal * 0.05
        else:
            return 0

    def calcular_iva(self):
        return self.subtotal * 0.16  # 16% de IVA

    def calcular_igtf(self):
        # Aplica el 3% de IGTF si el método de pago es en divisas
        if self.metodo_pago == 'dolares':
            return self.subtotal * 0.03
        return 0

    def calcular_total(self):
        # Calcula el total final sumando y restando los componentes necesarios
        return self.subtotal - self.descuento + self.iva + self.igtf

    def mostrar_desglose(self):
        # Muestra un desglose detallado de la compra
        print("Desglose de la compra:")
        print(f"Cliente: {self.ci_cliente.nombre}")  # Asume que ci_cliente tiene un atributo 'nombre'
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Descuento: -${self.descuento:.2f}")
        print(f"IVA (16%): +${self.iva:.2f}")
        print(f"IGTF (3%): +${self.igtf:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")
