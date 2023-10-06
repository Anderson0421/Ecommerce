class Cart:
    def __init__(self,request):
        self.request = request #Para crear un objeto request
        self.session = request.session #Para obtener la session del navegador
        
        cart = self.session.get("cart") #Con esto obtenemos el nombre de la VARIABLE DE LA SESION
        montoTotal = self.session.get("cartMontoTotal")
        if not cart: 
            cart = self.session['cart'] = {}
            montoTotal = self.session['cartMontoTotal'] = "0"
            
            #El cart sera el nombre de la session
        
        self.cart = cart
        self.montoTotal = float(montoTotal)

    def add(self,producto,cantidad):
        if str(producto.id) not in self.cart.keys(): #Con esto preguntamos si el producto no esta en el carrito
            self.cart[producto.id] = {
            "producto_id":producto.id,
            "nombre":producto.nombre,
            "cantidad":cantidad,
            "precio":str(producto.precio),
            "imagen":producto.imagen.url,
            "categoria":producto.categoria.nombre,
            "subtotal":str(cantidad * producto.precio),
        }
        else:
            #actualizamos el carrito
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value['cantidad'] = str(int(value['cantidad']) + cantidad)
                    value['subtotal'] = str(float(value['cantidad'])* float(value['precio']))
                    break

        self.save() #Con esto llamamos al metodo save de abajo
    
    def delete(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session['cartMontoTotal'] = "0"

    def save(self):
        
        montoTotal = 0

        for key,value in self.cart.items():
            montoTotal += float(value['subtotal'])
            
        """Guardar cambios en el carrito de compras"""
        self.session['cartMontoTotal'] = montoTotal
        self.session['cart'] = self.cart
        self.session.modified = True

        #Con esto creamos una variable de sesion que inicializa el carrito de compras
        