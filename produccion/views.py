from django.forms import formset_factory
from django.views.generic.edit import FormView 
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import ProductionForm
from .models import Product, Production
from .sincronizarProductos import sincronizarProductos
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


class AddProduction(FormView):
    template_name = 'produccion/add_produccion.html'
    success_url = "/produccion/list"  
    form_class = formset_factory(ProductionForm, extra=0)
    def get_initial_data(self):
        return [{'id': producto.id} for producto in Product.objects.filter(is_deleted=False)]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_dict'] = {producto.id: producto.product_key for producto in Product.objects.all()}
        context['formset'] = kwargs.get('formset', self.get_form())
        return context

    def get_form(self):
        return self.form_class(initial=self.get_initial_data())

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():  
            for form in formset:
                if form.cleaned_data.get('cantidad', 0) != 0:
                    form.save()
            return HttpResponseRedirect(self.success_url)

        # Si hay errores, renderiza con el formset inválido
        return self.render_to_response(self.get_context_data(formset=formset))


class ListProduccion(ListView):
    model = Production
    template_name = 'produccion/list_produccion.html'
    ordering = ['-date']
    paginate_by = 15
    context_object_name = 'object_list'  # Esto es opcional si ya usas 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el diccionario de nombres de productos al contexto
        productos_dict = {producto.id: producto.product_key for producto in Product.objects.all()}
        context['productos_dict'] = productos_dict

        return context

def sincronizar_productos(request):
    try:
        # Llamar a la función de sincronización
        sincronizarProductos()
        # Añadir un mensaje de éxito
        messages.success(request, "Sincronización completa.")
        print("Sincronización completada correctamente.")
    except Exception as e:
        # Añadir un mensaje de error
        messages.error(request, f"Error al sincronizar los productos: {e}")
        return HttpResponse(f"Error al sincronizar los productos: {e}", status=500)
    
    # Redirigir a la vista deseada después de la sincronización
    return redirect('produccion_add')  # Cambia el nombre si necesitas redirigir a otro lugar