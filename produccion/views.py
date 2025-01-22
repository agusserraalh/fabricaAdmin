from django.forms import formset_factory
from django.views.generic.edit import FormView 
from django.views.generic import ListView
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ProductionForm
from .models import Product, Production
from .sincronizarProductos import sincronizarProductos
from django.shortcuts import redirect
from django.contrib import messages
from datetime import date
from django.db.models import Sum


class AddProduction(FormView):
    template_name = 'produccion/add_produccion.html'
    success_url = "/produccion/list"  
    form_class = formset_factory(ProductionForm, extra=0)
    def get_initial_data(self):
        return [{'id': producto.id} for producto in Product.objects.filter(is_deleted=False).order_by('-product_key')]
    
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
        return self.render_to_response(self.get_context_data(formset=formset))

class ListProduccion(ListView):
    model = Production
    template_name = 'produccion/list_produccion.html'
    ordering = ['-date']
    paginate_by = 15
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Diccionario de productos para la tabla
        productos_dict = {producto.id: producto.product_key for producto in Product.objects.all()}
        context['productos_dict'] = productos_dict
        
        # Totales de producción del mes actual
        current_month = date.today().month
        current_year = date.today().year
        produccion_mensual = (
            Production.objects.filter(date__year=current_year, date__month=current_month)
            .values('id')
            .annotate(total_cantidad=Sum('cantidad'))
            .order_by('id')
        )
        context['produccion_mensual'] = produccion_mensual
        context['current_month'] = current_month
        context['current_year'] = current_year

        return context

def sincronizar_productos(request):
    try:
        sincronizarProductos()
        messages.success(request, "Sincronización completa.")
    except Exception as e:
        messages.error(request, f"Error al sincronizar los productos: {e}")
        return HttpResponse(f"Error al sincronizar los productos: {e}", status=500)
    
    return redirect('produccion_add')  