class Producto: 

    def __init__(self,id,nombre,descripcion,precio,categoria,inventario,) -> None:
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.categoria=categoria
        self.inventario=inventario
        self.carros_compa=[]

    
    def buscar_producto(self):
        pass

    def modificar_productos(self):
        pass

    def eliminar_producto(self):
        pass

    def __str__(self):
        return f"El producto:{self.nombre}, Descripcion:{self.descripcion}, Precio: {self.descripcion}, Categoria {self.categoria}, Cantidad:{self.precio}"

 