from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView,View
from django.shortcuts import render

from .utils import render_to_pdf
from .models import Food
# Create your views here.


class ListaComidaListView(ListView):
    model=Food
    template_name = "home/comidas.html"
    context_object_name = 'comidas'

class ListComidasPdf(View):
    def get(self,request,*args,**kwargs):
        comidas = Food.objects.all
        data = {
            'comidas':comidas
        }
        pdf = render_to_pdf('home/lista.html',data)
        return HttpResponse(pdf,content_type ='application/pdf')
