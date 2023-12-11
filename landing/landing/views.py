from django.shortcuts import render, redirect
from .models import Product
from django.views.decorators.http import require_POST

def landing_page(request):
    if request.method == 'POST':
        # Recuperar los datos del formulario
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

        # Crear y guardar el nuevo producto
        Product.objects.create(marca=marca, descripcion=descripcion, precio=precio)
        return redirect('landing_page')  # Redirigir a la misma página para ver el producto añadido

    products = Product.objects.all()
    return render(request, 'landing/landing_page.html', {'products': products})

@require_POST
def eliminar_producto(request, codigo):
    producto = Product.objects.get(codigo=codigo)
    producto.delete()
    return redirect('landing_page')
