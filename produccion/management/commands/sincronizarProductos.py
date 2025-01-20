#from django.core.management.base import NoArgsCommand
from django.core.management.base import BaseCommand

import produccion.sincronizarProductos as sincronizarProductos

    #class Command(NoArgsCommand):
class Command(BaseCommand):

    #def handle_noargs(self, **options):
    def handle(self, *args, **options):
        sincronizarProductos.sincronizarProductos()