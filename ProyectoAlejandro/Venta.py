class Venta:
    def __init__(self,ci_cliente,producto_comprado,cantidades,metodo_pago,metodo_envio) :
        self.ci_cliente=ci_cliente
        self.producto_comprado=producto_comprado
        self.cantidades=cantidades
        self.metodo_pago=metodo_pago
        self.metodo_envio=metodo_envio
        self.subtotal = self.calcular_subtotal()  # Subtotal de la compra
        self.descuento = self.calcular_descuento()  # Descuento aplicado
        self.iva = self.calcular_iva()  # IVA del 16%
        self.igtf = self.calcular_igtf()  # IGTF del 3% si aplica
        self.total = self.calcular_total()  # Total final de la compra
        
    def calcular_subtotal(self):
        subtotal = 0
        for producto, cantidad in zip(self.producto_comprado, self.cantidades):
            subtotal += producto.precio * cantidad
        return subtotal

    def calcular_descuento(self):
        if self.ci_cliente.tipo == 'jurídico' and self.metodo_pago == 'contado':
            return self.subtotal * 0.05  # 5% de descuento
        return 0

    def calcular_iva(self):
        return self.subtotal * 0.16  # 16% de IVA

    def calcular_igtf(self):
        if self.metodo_pago == 'divisas':
            return self.subtotal * 0.03  # 3% de IGTF si es en divisas
        return 0

    def calcular_total(self):
        return self.subtotal - self.descuento + self.iva + self.igtf