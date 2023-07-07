from django.shortcuts import render,redirect
from.forms import PedidosForm
from django.core.mail import EmailMessage #importar para lo de gmail
from django.urls import reverse
from carro.carro import Carro
from carro.context_processor import importe_total_carro


    
def pedidos(request):
        
    pedido_form = PedidosForm()
    carro = Carro(request)
    total = importe_total_carro(request)

    if request.method == "POST":
        pedido_form =PedidosForm(data=request.POST)
        if pedido_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')    
            telefono = request.POST.get('telefono','')    
            entregas = request.POST.get('entregas','')    
            direccion = request.POST.get('direccion','')    
            indicaciones = request.POST.get('indicaciones','')    
            pagos = request.POST.get('pagos','')
             
            cart_items = carro.carro.values()
            
            
            message = f"""Email: {email}\n\nEscribió:\n\n telefono:{telefono}\n\n tipo de entrega:{entregas}\n\n direccion:{direccion}\n\n indicaciones adiccionales:{indicaciones}\n\n tipo de pago: {pagos}"""  
            
            message += "\n\nProductos en el carrito:\n"
            
            total_pagar= f"Debe pagar: {total['importe_total_carro']:.3f} $"

            for item in cart_items:
                message += f"- {item['nombre']}: Cantidad: {item['cantidad']}, Precio: {float(item['precio']):.3f} $ \n"
            email=EmailMessage(
                "PEDIDOS: Nuevo Mensaje",
                "De {} <{}>\n\n TOTAL DE TODO:\n\n{}".format(name,message,total_pagar),
                
                "sandbox.smtp.mailtrap.io",
                ["yenniferadrada@gmail.com","yenyadrada@misena.edu.co"],
                reply_to=[email]
            )   
            
            try:#excepcion
                email.send()
                #mensaje de envio en el caso que todo este bien
                return redirect(reverse('pedido')+"?ok")
            except:
                #error que direcciona a fail
                return redirect(reverse('pedido')+"?fail")
    #return redirect(reverse('pedido')+"?Enviado Correctamente")
    return render(request, "pedidos/finalizar_compra.html",{'form':pedido_form})