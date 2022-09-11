from rest_framework.viewsets import ModelViewSet
from sentidos.models import Food,Opinion,Usuario,Mesa,Reserva
from sentidos.api.serializers import FoodSerializer,OpinionSerializer,UsuarioSerializer,MesaSerializer,ReservaSerializer


class FoodApiViewSet(ModelViewSet):
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            print(name)
            queryset = queryset.filter(name = name)
        return queryset


class OpinionApiViewSet(ModelViewSet):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()


class UsuarioApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class MesasApiViewSet(ModelViewSet):
    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()

class ReservasApiViewSet(ModelViewSet):
    serializer_class = ReservaSerializer
    def get_queryset(self):  
        queryset = Reserva.objects.all()
        horario = self.request.query_params.get('horario')
        fecha = self.request.query_params.get('fecha')
        if horario is not None:
            print(horario)
            queryset = queryset.filter(horario = horario)
        if fecha is not None:
            print(fecha)
            queryset = queryset.filter(fecha = fecha)
        return queryset
