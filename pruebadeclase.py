from logging import exception


class Producto:
    Codigo= 0
    Nombre= ""
    Precio= 0

    def __init__(self, codigo, nombre, precio):
        self.Codigo=codigo
        self.Nombre=nombre
        self.Precio=precio
#---------------------------------------
    def get_Codigo(self):
        return self.Codigo

    def set_Codigo(self, codigo):
        self.Codigo=codigo
#--------------------------------------

    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, nombre):
        self.Codigo=nombre
#------------------------------------
    def get_Precio(self):
        return self.Precio

    def set_Precio(self, precio):
        self.Precio=precio
    
#------------------------------------

    def __str__(self):
        return ('El codigo del producto es '+ str(self.Codigo)+ 'Su nombre es'+ str(self.Nombre)+ 'El precio es'+ str(self.Precio))

    def Calcular_total(self, unidades):
        return (self.Precio * unidades)

#miPrimerProducto= producto

# miPrimerProducto.Codigo=15
# miPrimerProducto.Nombre='casa'
# miPrimerProducto.Precio=500

# resultado=miPrimerProducto.Calcular_total(miPrimerProducto, 2)
# print(resultado)

class Pedido:
    
    Producto=[]
    cantidades=[]
    
    def __init__(self):
        self.productos=[]
        self.cantidades=[]
        
    def añadir_productos(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise exception ('añadir_producto: producto debe ser de la clase producto')

        if not isinstance (cantidad, int):
            raise exception('añadir_producto: cantidades debe ser un numero entero')
        
        if cantidad<=0:
            raise exception ('añadir_producto: cantidades debe ser mayor que cero')
        
        if producto in self.productos :
            indice= self.productos.index(producto)
            self.cantidades[indice] += cantidad
            
        else:
            self.cantidades.append(cantidad)
            self.productos.append(producto)
            
    def eliminar_producto(self, producto):
        
        if not isinstance(producto, Producto):
            raise exception ('eliminar_producto: producto debe ser de la clase producto')
        
        if producto in self.productos:
            indice= self.productos.index(producto)
            del self.productos [indice]
            del self.cantidades[indice]
        else:
            raise exception ('eliminar_producto: el producto no existe')
        
    def total_pedido(self):
        total=0
        
        for (p,c) in zip(self.productos,self.cantidades):
            total += total + p.Calcular_total(c)
        return total 
    
    def mostrar_producto(self):
        for (p,c) in zip(self.productos,self.cantidades):
            print('Producto: '+ p.get_Nombre()+ ', Cantidad:' + str(c))
            


p1= Producto (1, 'producto 1 ', 5)
p2= Producto (2, 'producto 2', 15)
p3= Producto (3, 'producto 3', 25)

pedido= Pedido()
 
try:
    pedido.añadir_productos(p1,9)
    pedido.añadir_productos(p2, 5)
    pedido.añadir_productos(p3, 14)
    
    print('total pedido'+ str(pedido.total_pedido()))
    
    pedido.mostrar_producto()
    pedido.eliminar_producto(p2)
    
    pedido.mostrar_producto()

except Exception as e:
    print(e)    