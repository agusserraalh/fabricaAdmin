from django.forms import formset_factory
from django.views.generic.edit import FormView 
from django.views.generic import ListView
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ProductionForm
from .models import Product, Production
from .sincronizarProductos import sincronizarProductos
from django.shortcuts import redirect, get_object_or_404,render
from django.contrib import messages
from datetime import date
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class AddProduction(LoginRequiredMixin, FormView):
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
    
@login_required
def sincronizar_productos(request):
    try:
        sincronizarProductos()
        messages.success(request, "Sincronización completa.")
    except Exception as e:
        messages.error(request, f"Error al sincronizar los productos: {e}")
        return HttpResponse(f"Error al sincronizar los productos: {e}", status=500)
    
    return redirect('produccion_add')  

@login_required
def produccion_edit(request, uuid):
    if request.method == 'POST':
        produccion = get_object_or_404(Production, uuid=uuid)
        nueva_cantidad = request.POST.get('cantidad')
        
        try:
            # Validar y actualizar la cantidad
            if nueva_cantidad is not None and nueva_cantidad.isdigit():
                produccion.cantidad = int(nueva_cantidad)
                produccion.save()
                messages.success(request, 'Cantidad actualizada correctamente.')
            else:
                messages.error(request, 'La cantidad debe ser un número válido.')
        except Exception as e:
            messages.error(request, f'Error al actualizar: {str(e)}')
    
    return redirect('produccion_list')


@login_required
def produccion_delete(request, uuid):
    produccion = get_object_or_404(Production, uuid=uuid)
    
    if request.method == 'POST':
        try:
            produccion.delete()
            messages.success(request, 'Producción eliminada correctamente.')
        except Exception as e:
            messages.error(request, f'Error al eliminar la producción: {str(e)}')
    
    # Redirigir a la lista de producción, independientemente de si es POST o GET
    return redirect('produccion_list')

class ListProduccion(LoginRequiredMixin, ListView):
    model = Production
    template_name = 'produccion/list_produccion.html'
    ordering = ['-date', '-created_at']
    paginate_by = 15
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        productos_dict = {producto.id: producto.product_key for producto in Product.objects.all()}
        context['productos_dict'] = productos_dict

        current_month = int(self.request.GET.get('mes', date.today().month))
        current_year = int(self.request.GET.get('anio', date.today().year))

        produccion_mensual = (
            Production.objects.filter(date__year=current_year, date__month=current_month)
            .values('id')
            .annotate(total_cantidad=Sum('cantidad'))
            .order_by('id')
        )
        context['produccion_mensual'] = produccion_mensual
        context['current_month'] = current_month
        context['current_year'] = current_year

        context['meses'] = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
            5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
            9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        anios_disponibles = (
            Production.objects.dates('date', 'year', order='DESC')
            .values_list('date__year', flat=True)
        )
        context['anios_disponibles'] = sorted(set(anios_disponibles), reverse=True)

        return context
