from django.contrib import admin
from django.urls import path


from . import views

app_name = "comidas_app"

urlpatterns = [
    path('lista/',views.ListaComidaListView.as_view(),
    name='lista'),
    path('listar-comidas/',views.ListComidasPdf.as_view(),
    name='comidas__all')
]